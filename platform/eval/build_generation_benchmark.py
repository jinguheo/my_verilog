#!/usr/bin/env python3
"""Build a 150-problem Verilog generation benchmark with realistic RTL tasks.

The generated JSONL keeps VerilogEval-compatible fields:

- prompt: module header used to compose a candidate
- canonical_solution: reference implementation body plus endmodule
- test: self-checking testbench comparing candidate top_module to reference_module

The tasks intentionally move beyond single-expression examples.  They cover
decode logic, masks, handshake stages, FSMs, arbiters, small storage blocks,
stream control, and controller-style RTL.  A matching canonical candidate file
is emitted to sanity-check the verifier path; real model results can replace it.
"""
from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUT = ROOT / "out" / "generation_benchmark"
LEVELS = ("L1", "L2", "L3", "L4", "L5")
InputSpec = tuple[str, int]
OutputSpec = tuple[str, int, bool]


def width_range(width: int) -> str:
    return "" if width == 1 else f"[{width - 1}:0] "


def port(direction: str, name: str, width: int = 1, reg: bool = False) -> str:
    reg_text = "reg " if reg else ""
    return f"{direction} {reg_text}{width_range(width)}{name}"


def out(name: str, width: int = 1, reg: bool = False) -> OutputSpec:
    return (name, width, reg)


def decl(kind: str, name: str, width: int = 1) -> str:
    return f"  {kind} {width_range(width)}{name};"


def module_header(inputs: list[InputSpec], outputs: list[OutputSpec]) -> str:
    ports = [port("input", name, width) for name, width in inputs]
    ports += [port("output", name, width, reg=reg) for name, width, reg in outputs]
    return f"module top_module({', '.join(ports)});"


def reference_header(prompt: str) -> str:
    return prompt.replace("module top_module", "module reference_module", 1)


def body_without_endmodule(solution: str) -> str:
    return re.sub(r"\s*endmodule\s*$", "", solution.strip(), flags=re.IGNORECASE)


def indent_body(body: str) -> str:
    return "\n".join(f"  {line}" if line else "" for line in body.splitlines())


def compare_outputs(outputs: list[OutputSpec], indent: str = "    ") -> str:
    dut = ", ".join(f"{name}_dut" for name, _width, _reg in outputs)
    ref = ", ".join(f"{name}_ref" for name, _width, _reg in outputs)
    if len(outputs) == 1:
        dut_expr = f"{outputs[0][0]}_dut"
        ref_expr = f"{outputs[0][0]}_ref"
    else:
        dut_expr = "{" + dut + "}"
        ref_expr = "{" + ref + "}"
    return f"{indent}if ({dut_expr} !== {ref_expr}) errors = errors + 1;"


def make_testbench(
    prompt: str,
    solution: str,
    inputs: list[InputSpec],
    outputs: list[OutputSpec],
    stimulus_lines: list[str],
) -> str:
    ref_maps = [f".{name}({name})" for name, _width in inputs]
    dut_maps = list(ref_maps)
    for name, _width, _reg in outputs:
        ref_maps.append(f".{name}({name}_ref)")
        dut_maps.append(f".{name}({name}_dut)")

    lines = [
        reference_header(prompt),
        indent_body(body_without_endmodule(solution)),
        "endmodule",
        "",
        "module tb;",
    ]
    lines += [decl("reg", name, width) for name, width in inputs]
    for name, width, _reg in outputs:
        lines.append(decl("wire", f"{name}_ref", width))
        lines.append(decl("wire", f"{name}_dut", width))
    lines += [
        "  integer i;",
        "  integer errors;",
        f"  reference_module ref_i({', '.join(ref_maps)});",
        f"  top_module dut({', '.join(dut_maps)});",
        "  initial begin",
        "    errors = 0;",
        *stimulus_lines,
        "    if (errors == 0) $display(\"PASS\");",
        "    else $display(\"Mismatches: %0d\", errors);",
        "    $finish;",
        "  end",
        "endmodule",
    ]
    return "\n".join(lines)


def comb_stimulus(inputs: list[InputSpec], outputs: list[OutputSpec], cycles: int = 64) -> list[str]:
    lines = [f"    for (i = 0; i < {cycles}; i = i + 1) begin"]
    for idx, (name, width) in enumerate(inputs):
        if width == 1:
            lines.append(f"      {name} = i[{idx % 8}];")
        else:
            lines.append(f"      {name} = (i * {idx + 3}) + {idx + 1};")
    lines += [
        "      #1;",
        compare_outputs(outputs, "      "),
        "    end",
    ]
    return lines


def clock_compare(outputs: list[OutputSpec], indent: str = "    ") -> list[str]:
    return [
        f"{indent}clk = 0; #1;",
        f"{indent}clk = 1; #1;",
        compare_outputs(outputs, indent),
    ]


def seq_stimulus(inputs: list[InputSpec], outputs: list[OutputSpec], cycles: int = 80) -> list[str]:
    names = {name for name, _width in inputs}
    lines = ["    clk = 0;"]
    if "rst" in names:
        lines.append("    rst = 1;")
    for name, _width in inputs:
        if name not in {"clk", "rst"}:
            lines.append(f"    {name} = 0;")
    if "rst" in names:
        lines += clock_compare(outputs)
        lines.append("    rst = 0;")
    lines.append(f"    for (i = 0; i < {cycles}; i = i + 1) begin")
    for idx, (name, width) in enumerate(inputs):
        if name in {"clk", "rst"}:
            continue
        if width == 1:
            lines.append(f"      {name} = i[{(idx + 1) % 8}];")
        elif name == "period":
            lines.append(f"      {name} = ((i * {idx + 4}) + 8) | 1;")
        elif name == "duty":
            lines.append(f"      {name} = (i * {idx + 2}) + 1;")
        else:
            lines.append(f"      {name} = (i * {idx + 5}) + {idx + 1};")
    lines += clock_compare(outputs, "      ")
    lines.append("    end")
    if "rst" in names:
        lines.append("    rst = 1;")
        lines += clock_compare(outputs)
    return lines


def add_problem(
    rows: list[dict[str, Any]],
    level: str,
    qtype: str,
    slug: str,
    inputs: list[InputSpec],
    outputs: list[OutputSpec],
    solution: str,
    stimulus_lines: list[str],
    description: str,
    tags: list[str],
) -> None:
    level_index = sum(1 for row in rows if row["level"] == level) + 1
    prompt = module_header(inputs, outputs)
    rows.append({
        "task_id": f"gen_{level.lower()}_{level_index:03d}_{slug}",
        "level": level,
        "type": qtype,
        "prompt": prompt,
        "description": description,
        "canonical_solution": solution,
        "test": make_testbench(prompt, solution, inputs, outputs, stimulus_lines),
        "tags": tags,
        "inputs": [{"name": name, "width": width} for name, width in inputs],
        "outputs": [{"name": name, "width": width, "reg": reg} for name, width, reg in outputs],
    })


def clog2(value: int) -> int:
    return max(1, math.ceil(math.log2(value)))


def build_l1(rows: list[dict[str, Any]]) -> None:
    widths = [8, 10, 12, 16, 24]
    packet_widths = [16, 24, 32, 40, 48]
    lanes = [4, 4, 8, 8, 16]
    req_widths = [3, 4, 5, 6, 8]
    for variant in range(5):
        width = widths[variant]
        inputs = [("valid", 1), ("addr", width)]
        outputs = [out("region", 2), out("hit"), out("high_half")]
        solution = (
            f"assign region = addr[{width - 1}:{width - 2}];\n"
            f"assign hit = valid && (addr[{width - 1}:{width - 3}] == 3'b101);\n"
            f"assign high_half = valid && addr[{width - 1}];\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L1",
            "generation_decode",
            f"address_region_decode_{width}w",
            inputs,
            outputs,
            solution,
            comb_stimulus(inputs, outputs),
            "Decode an address into region bits and hit/high-half status flags.",
            ["decode", "address", f"width_{width}"],
        )

        pwidth = packet_widths[variant]
        inputs = [("valid", 1), ("word", pwidth)]
        outputs = [out("opcode", 4), out("length", 8), out("last"), out("even_parity")]
        solution = (
            "assign opcode = word[3:0];\n"
            "assign length = word[15:8];\n"
            f"assign last = valid && word[{pwidth - 1}];\n"
            "assign even_parity = ~^word;\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L1",
            "generation_packet_fields",
            f"packet_field_extract_{pwidth}w",
            inputs,
            outputs,
            solution,
            comb_stimulus(inputs, outputs),
            "Extract fields and flags from a packed packet header word.",
            ["packet", "field_extract", f"width_{pwidth}"],
        )

        lane_count = lanes[variant]
        aw = clog2(lane_count)
        inputs = [("write", 1), ("size", 2), ("addr", aw)]
        outputs = [out("mask", lane_count)]
        half_mask = (1 << aw) - 2
        solution = (
            f"wire [{aw - 1}:0] half_addr;\n"
            f"assign half_addr = addr & {aw}'d{half_mask};\n"
            f"assign mask = !write ? {lane_count}'d0 :\n"
            f"              (size == 2'd0) ? ({lane_count}'d1 << addr) :\n"
            f"              (size == 2'd1) ? ({lane_count}'d3 << half_addr) :\n"
            f"              {{{lane_count}{{1'b1}}}};\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L1",
            "generation_masking",
            f"byte_lane_mask_{lane_count}lane",
            inputs,
            outputs,
            solution,
            comb_stimulus(inputs, outputs),
            "Generate a byte-lane write mask from write size and low address bits.",
            ["mask", "byte_lane", f"lanes_{lane_count}"],
        )

        req_width = req_widths[variant]
        iw = clog2(req_width)
        inputs = [("req", req_width)]
        outputs = [out("grant", req_width, True), out("valid", 1, True), out("index", iw, True)]
        solution = (
            "integer k;\n"
            "always @* begin\n"
            f"  grant = {req_width}'d0;\n"
            "  valid = 1'b0;\n"
            f"  index = {iw}'d0;\n"
            f"  for (k = {req_width - 1}; k >= 0; k = k - 1) begin\n"
            "    if (req[k]) begin\n"
            f"      grant = ({req_width}'d1 << k);\n"
            "      index = k;\n"
            "      valid = 1'b1;\n"
            "    end\n"
            "  end\n"
            "end\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L1",
            "generation_priority",
            f"priority_grant_{req_width}req",
            inputs,
            outputs,
            solution,
            comb_stimulus(inputs, outputs),
            "Build a fixed-priority one-hot grant encoder with valid and index outputs.",
            ["priority", "grant", f"req_{req_width}"],
        )

        inputs = [("op", 3), ("a", width), ("b", width)]
        outputs = [out("result", width, True), out("zero", 1, True), out("carry", 1, True)]
        solution = (
            f"reg [{width}:0] tmp;\n"
            "always @* begin\n"
            "  tmp = 0;\n"
            "  case (op)\n"
            f"    3'd0: tmp = {{1'b0, a}} + {{1'b0, b}};\n"
            f"    3'd1: tmp = {{1'b0, a}} - {{1'b0, b}};\n"
            f"    3'd2: tmp = {{1'b0, (a & b)}};\n"
            f"    3'd3: tmp = {{1'b0, (a | b)}};\n"
            f"    3'd4: tmp = {{1'b0, (a ^ b)}};\n"
            f"    default: tmp = {{1'b0, a}};\n"
            "  endcase\n"
            f"  result = tmp[{width - 1}:0];\n"
            f"  carry = tmp[{width}];\n"
            "  zero = (result == 0);\n"
            "end\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L1",
            "generation_datapath_flags",
            f"alu_flags_{width}w",
            inputs,
            outputs,
            solution,
            comb_stimulus(inputs, outputs),
            "Implement a small combinational ALU and produce zero/carry flags.",
            ["alu", "flags", f"width_{width}"],
        )

        inputs = [("valid_i", 1), ("ready_i", 1), ("flush", 1), ("data_i", width)]
        outputs = [out("accept"), out("stall"), out("data_o", width), out("odd_parity")]
        solution = (
            "assign accept = valid_i && ready_i && !flush;\n"
            "assign stall = valid_i && !ready_i;\n"
            f"assign data_o = accept ? data_i : {width}'d0;\n"
            "assign odd_parity = ^data_o;\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L1",
            "generation_handshake_comb",
            f"ready_valid_gate_{width}w",
            inputs,
            outputs,
            solution,
            comb_stimulus(inputs, outputs),
            "Generate ready/valid accept and stall decisions with gated data output.",
            ["ready_valid", "combinational", f"width_{width}"],
        )


def build_l2(rows: list[dict[str, Any]]) -> None:
    widths = [8, 12, 16, 24, 32]
    for variant, width in enumerate(widths):
        inputs = [("clk", 1), ("rst", 1), ("valid_i", 1), ("ready_i", 1), ("data_i", width)]
        outputs = [out("valid_o", 1, True), out("data_o", width, True), out("ready_o"), out("fire_o")]
        solution = (
            "assign ready_o = !valid_o || ready_i;\n"
            "assign fire_o = valid_o && ready_i;\n"
            "always @(posedge clk) begin\n"
            "  if (rst) begin\n"
            "    valid_o <= 1'b0;\n"
            "    data_o <= 0;\n"
            "  end else if (ready_o) begin\n"
            "    valid_o <= valid_i;\n"
            "    data_o <= data_i;\n"
            "  end\n"
            "end\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L2",
            "generation_pipeline_stage",
            f"ready_valid_stage_{width}w",
            inputs,
            outputs,
            solution,
            seq_stimulus(inputs, outputs),
            "Implement a one-entry ready/valid pipeline stage with backpressure.",
            ["pipeline", "ready_valid", f"width_{width}"],
        )

        inputs = [("clk", 1), ("rst", 1), ("sig", 1), ("clear", 1)]
        outputs = [out("rise", 1, True), out("fall", 1, True), out("sticky", 1, True)]
        solution = (
            "reg prev;\n"
            "always @(posedge clk) begin\n"
            "  if (rst) begin\n"
            "    prev <= 1'b0;\n"
            "    rise <= 1'b0;\n"
            "    fall <= 1'b0;\n"
            "    sticky <= 1'b0;\n"
            "  end else begin\n"
            "    rise <= sig & ~prev;\n"
            "    fall <= ~sig & prev;\n"
            "    prev <= sig;\n"
            "    if (clear) sticky <= 1'b0;\n"
            "    else if (sig & ~prev) sticky <= 1'b1;\n"
            "  end\n"
            "end\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L2",
            "generation_event_register",
            f"edge_sticky_{variant + 1}",
            inputs,
            outputs,
            solution,
            seq_stimulus(inputs, outputs),
            "Detect rising/falling edges and latch a sticky event until clear.",
            ["edge_detect", "sticky"],
        )

        limit = 4 + variant * 3
        cw = clog2(limit + 1)
        inputs = [("clk", 1), ("rst", 1), ("start", 1)]
        outputs = [out("busy", 1, True), out("done", 1, True), out("count", cw, True)]
        solution = (
            "always @(posedge clk) begin\n"
            "  if (rst) begin\n"
            "    busy <= 1'b0;\n"
            "    done <= 1'b0;\n"
            "    count <= 0;\n"
            "  end else begin\n"
            "    done <= 1'b0;\n"
            "    if (start && !busy) begin\n"
            "      busy <= 1'b1;\n"
            "      count <= 0;\n"
            f"    end else if (busy && count == {cw}'d{limit}) begin\n"
            "      busy <= 1'b0;\n"
            "      done <= 1'b1;\n"
            "    end else if (busy) begin\n"
            "      count <= count + 1'b1;\n"
            "    end\n"
            "  end\n"
            "end\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L2",
            "generation_timer",
            f"start_done_timer_{limit}",
            inputs,
            outputs,
            solution,
            seq_stimulus(inputs, outputs),
            "Create a start/busy/done timer that asserts done after a fixed count.",
            ["timer", "done_pulse", f"limit_{limit}"],
        )

        hold = 2 + variant
        cw = clog2(hold + 2)
        inputs = [("clk", 1), ("rst", 1), ("trig", 1)]
        outputs = [out("pulse", 1, True), out("remain", cw, True)]
        solution = (
            "always @(posedge clk) begin\n"
            "  if (rst) begin\n"
            "    remain <= 0;\n"
            "    pulse <= 1'b0;\n"
            "  end else begin\n"
            f"    if (trig) remain <= {cw}'d{hold};\n"
            "    else if (remain != 0) remain <= remain - 1'b1;\n"
            "    pulse <= trig || (remain != 0);\n"
            "  end\n"
            "end\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L2",
            "generation_pulse_control",
            f"pulse_stretcher_{hold}",
            inputs,
            outputs,
            solution,
            seq_stimulus(inputs, outputs),
            "Stretch a trigger into a multi-cycle pulse with a visible remaining count.",
            ["pulse", "timer", f"hold_{hold}"],
        )

        inputs = [("clk", 1), ("rst", 1), ("load", 1), ("en", 1), ("up", 1), ("value", width)]
        outputs = [out("count", width, True), out("zero"), out("terminal")]
        solution = (
            "assign zero = (count == 0);\n"
            f"assign terminal = (count == {{{width}{{1'b1}}}});\n"
            "always @(posedge clk) begin\n"
            "  if (rst) count <= 0;\n"
            "  else if (load) count <= value;\n"
            "  else if (en && up) count <= count + 1'b1;\n"
            "  else if (en) count <= count - 1'b1;\n"
            "end\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L2",
            "generation_counter",
            f"loadable_updown_counter_{width}w",
            inputs,
            outputs,
            solution,
            seq_stimulus(inputs, outputs),
            "Implement a loadable up/down counter with zero and terminal flags.",
            ["counter", "loadable", f"width_{width}"],
        )

        inputs = [("clk", 1), ("rst", 1), ("sample", 1), ("data_i", width)]
        outputs = [out("data_o", width, True), out("changed", 1, True)]
        solution = (
            "always @(posedge clk) begin\n"
            "  if (rst) begin\n"
            "    data_o <= 0;\n"
            "    changed <= 1'b0;\n"
            "  end else begin\n"
            "    changed <= sample && (data_i != data_o);\n"
            "    if (sample) data_o <= data_i;\n"
            "  end\n"
            "end\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L2",
            "generation_sample_hold",
            f"sample_hold_{width}w",
            inputs,
            outputs,
            solution,
            seq_stimulus(inputs, outputs),
            "Sample data on command and flag cycles where the sampled value changed.",
            ["sample_hold", f"width_{width}"],
        )


def build_l3(rows: list[dict[str, Any]]) -> None:
    widths = [4, 5, 6, 8, 10]
    for variant, width in enumerate(widths):
        inputs = [("clk", 1), ("rst", 1), ("valid_i", 1), ("bit_i", 1)]
        outputs = [out("match", 1, True), out("state", 2, True)]
        solution = (
            "always @(posedge clk) begin\n"
            "  if (rst) begin\n"
            "    state <= 2'd0;\n"
            "    match <= 1'b0;\n"
            "  end else begin\n"
            "    match <= 1'b0;\n"
            "    if (valid_i) begin\n"
            "      case (state)\n"
            "        2'd0: state <= bit_i ? 2'd1 : 2'd0;\n"
            "        2'd1: state <= bit_i ? 2'd1 : 2'd2;\n"
            "        2'd2: state <= bit_i ? 2'd3 : 2'd0;\n"
            "        default: begin\n"
            "          match <= bit_i;\n"
            "          state <= bit_i ? 2'd1 : 2'd2;\n"
            "        end\n"
            "      endcase\n"
            "    end\n"
            "  end\n"
            "end\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L3",
            "generation_fsm_sequence",
            f"sequence_1011_detector_{variant + 1}",
            inputs,
            outputs,
            solution,
            seq_stimulus(inputs, outputs),
            "Build an overlapping 1011 serial sequence detector with valid gating.",
            ["fsm", "sequence_detector"],
        )

        limit = 4 + variant * 2
        cw = clog2(limit + 2)
        inputs = [("clk", 1), ("rst", 1), ("start", 1), ("beat", 1), ("last", 1)]
        outputs = [out("active", 1, True), out("done", 1, True), out("error", 1, True), out("count", cw, True)]
        solution = (
            "always @(posedge clk) begin\n"
            "  if (rst) begin\n"
            "    active <= 1'b0;\n"
            "    done <= 1'b0;\n"
            "    error <= 1'b0;\n"
            "    count <= 0;\n"
            "  end else begin\n"
            "    done <= 1'b0;\n"
            "    error <= 1'b0;\n"
            "    if (start && !active) begin\n"
            "      active <= 1'b1;\n"
            "      count <= 0;\n"
            "    end else if (active && beat) begin\n"
            "      count <= count + 1'b1;\n"
            f"      if (last && count != {cw}'d{limit - 1}) begin\n"
            "        active <= 1'b0;\n"
            "        error <= 1'b1;\n"
            f"      end else if (count == {cw}'d{limit - 1}) begin\n"
            "        active <= 1'b0;\n"
            "        done <= last;\n"
            "        error <= !last;\n"
            "      end\n"
            "    end\n"
            "  end\n"
            "end\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L3",
            "generation_packet_fsm",
            f"packet_length_tracker_{limit}",
            inputs,
            outputs,
            solution,
            seq_stimulus(inputs, outputs),
            "Track a fixed-length packet and flag early/late end-of-packet errors.",
            ["fsm", "packet", f"limit_{limit}"],
        )

        timeout = 5 + variant * 3
        tw = clog2(timeout + 2)
        inputs = [("clk", 1), ("rst", 1), ("req", 1), ("ack", 1)]
        outputs = [out("busy", 1, True), out("done", 1, True), out("timeout", 1, True), out("timer", tw, True)]
        solution = (
            "always @(posedge clk) begin\n"
            "  if (rst) begin\n"
            "    busy <= 1'b0;\n"
            "    done <= 1'b0;\n"
            "    timeout <= 1'b0;\n"
            "    timer <= 0;\n"
            "  end else begin\n"
            "    done <= 1'b0;\n"
            "    timeout <= 1'b0;\n"
            "    if (req && !busy) begin\n"
            "      busy <= 1'b1;\n"
            "      timer <= 0;\n"
            "    end else if (busy && ack) begin\n"
            "      busy <= 1'b0;\n"
            "      done <= 1'b1;\n"
            f"    end else if (busy && timer == {tw}'d{timeout}) begin\n"
            "      busy <= 1'b0;\n"
            "      timeout <= 1'b1;\n"
            "    end else if (busy) begin\n"
            "      timer <= timer + 1'b1;\n"
            "    end\n"
            "  end\n"
            "end\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L3",
            "generation_timeout_fsm",
            f"request_ack_timeout_{timeout}",
            inputs,
            outputs,
            solution,
            seq_stimulus(inputs, outputs),
            "Control a request/ack transaction and timeout when ack is missing.",
            ["fsm", "timeout", f"timeout_{timeout}"],
        )

        threshold = 2 + variant
        cw = clog2(threshold + 2)
        inputs = [("clk", 1), ("rst", 1), ("noisy", 1)]
        outputs = [out("stable", 1, True), out("changed", 1, True), out("count", cw, True)]
        solution = (
            "always @(posedge clk) begin\n"
            "  if (rst) begin\n"
            "    stable <= 1'b0;\n"
            "    changed <= 1'b0;\n"
            "    count <= 0;\n"
            "  end else begin\n"
            "    changed <= 1'b0;\n"
            "    if (noisy == stable) begin\n"
            "      count <= 0;\n"
            f"    end else if (count == {cw}'d{threshold}) begin\n"
            "      stable <= noisy;\n"
            "      changed <= 1'b1;\n"
            "      count <= 0;\n"
            "    end else begin\n"
            "      count <= count + 1'b1;\n"
            "    end\n"
            "  end\n"
            "end\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L3",
            "generation_filter_fsm",
            f"debounce_filter_{threshold}",
            inputs,
            outputs,
            solution,
            seq_stimulus(inputs, outputs),
            "Debounce a noisy signal after several consecutive disagreeing samples.",
            ["debounce", "filter", f"threshold_{threshold}"],
        )

        max_credit = (1 << width) - 1
        inputs = [("clk", 1), ("rst", 1), ("consume", 1), ("return_credit", 1)]
        outputs = [out("can_send"), out("credits", width, True), out("overflow", 1, True)]
        solution = (
            "assign can_send = (credits != 0);\n"
            "always @(posedge clk) begin\n"
            "  if (rst) begin\n"
            f"    credits <= {width}'d{max_credit // 2};\n"
            "    overflow <= 1'b0;\n"
            "  end else begin\n"
            "    overflow <= 1'b0;\n"
            f"    if (return_credit && credits == {width}'d{max_credit}) overflow <= 1'b1;\n"
            f"    else if (return_credit && !consume) credits <= credits + {width}'d1;\n"
            f"    else if (consume && !return_credit && credits != 0) credits <= credits - {width}'d1;\n"
            "  end\n"
            "end\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L3",
            "generation_credit_control",
            f"credit_controller_{width}w",
            inputs,
            outputs,
            solution,
            seq_stimulus(inputs, outputs),
            "Maintain credits for a flow-control interface with overflow detection.",
            ["credit", "flow_control", f"width_{width}"],
        )

        inputs = [("clk", 1), ("rst", 1), ("valid_i", 1), ("sof", 1), ("eof", 1)]
        outputs = [out("in_frame", 1, True), out("frame_done", 1, True), out("frame_error", 1, True), out("bytes", width, True)]
        solution = (
            "always @(posedge clk) begin\n"
            "  if (rst) begin\n"
            "    in_frame <= 1'b0;\n"
            "    frame_done <= 1'b0;\n"
            "    frame_error <= 1'b0;\n"
            "    bytes <= 0;\n"
            "  end else begin\n"
            "    frame_done <= 1'b0;\n"
            "    frame_error <= 1'b0;\n"
            "    if (valid_i && sof && in_frame) frame_error <= 1'b1;\n"
            "    if (valid_i && sof) begin\n"
            "      in_frame <= 1'b1;\n"
            "      bytes <= 1;\n"
            "    end else if (valid_i && in_frame) begin\n"
            "      bytes <= bytes + 1'b1;\n"
            "    end\n"
            "    if (valid_i && eof) begin\n"
            "      frame_done <= in_frame;\n"
            "      frame_error <= frame_error || !in_frame;\n"
            "      in_frame <= 1'b0;\n"
            "    end\n"
            "  end\n"
            "end\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L3",
            "generation_stream_fsm",
            f"frame_parser_{width}w",
            inputs,
            outputs,
            solution,
            seq_stimulus(inputs, outputs),
            "Track start/end-of-frame events and count bytes in a stream.",
            ["stream", "frame", f"width_{width}"],
        )


def rr_update_cases(req_width: int) -> str:
    lines = []
    for idx in range(req_width):
        nxt = (idx + 1) % req_width
        lines.append(f"    if (grant[{idx}]) ptr <= {clog2(req_width)}'d{nxt};")
    return "\n".join(lines)


def build_l4(rows: list[dict[str, Any]]) -> None:
    widths = [8, 12, 16, 24, 32]
    req_widths = [2, 3, 4, 5, 6]
    for variant, width in enumerate(widths):
        req_width = req_widths[variant]
        pw = clog2(req_width)
        inputs = [("clk", 1), ("rst", 1), ("req", req_width), ("accept", 1)]
        outputs = [out("grant", req_width, True), out("valid"), out("ptr_o", pw)]
        solution = (
            f"reg [{pw - 1}:0] ptr;\n"
            "integer offset;\n"
            "integer idx;\n"
            "assign valid = |grant;\n"
            "assign ptr_o = ptr;\n"
            "always @* begin\n"
            f"  grant = {req_width}'d0;\n"
            f"  for (offset = 0; offset < {req_width}; offset = offset + 1) begin\n"
            f"    idx = (ptr + offset) % {req_width};\n"
            f"    if (req[idx] && grant == 0) grant = ({req_width}'d1 << idx);\n"
            "  end\n"
            "end\n"
            "always @(posedge clk) begin\n"
            "  if (rst) ptr <= 0;\n"
            "  else if (accept && valid) begin\n"
            f"{rr_update_cases(req_width)}\n"
            "  end\n"
            "end\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L4",
            "generation_arbiter",
            f"round_robin_arbiter_{req_width}req",
            inputs,
            outputs,
            solution,
            seq_stimulus(inputs, outputs),
            "Implement a round-robin arbiter with retained pointer and accept update.",
            ["arbiter", "round_robin", f"req_{req_width}"],
        )

        inputs = [("clk", 1), ("rst", 1), ("valid_i", 1), ("ready_i", 1), ("data_i", width)]
        outputs = [out("ready_o"), out("valid_o"), out("data_o", width)]
        solution = (
            f"reg [{width - 1}:0] data_q;\n"
            "reg full;\n"
            "assign ready_o = !full || ready_i;\n"
            "assign valid_o = full ? 1'b1 : valid_i;\n"
            "assign data_o = full ? data_q : data_i;\n"
            "always @(posedge clk) begin\n"
            "  if (rst) begin\n"
            "    full <= 1'b0;\n"
            "    data_q <= 0;\n"
            "  end else begin\n"
            "    if (valid_i && !ready_i && !full) begin\n"
            "      full <= 1'b1;\n"
            "      data_q <= data_i;\n"
            "    end else if (ready_i) begin\n"
            "      full <= 1'b0;\n"
            "    end\n"
            "  end\n"
            "end\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L4",
            "generation_elastic_buffer",
            f"skid_buffer_{width}w",
            inputs,
            outputs,
            solution,
            seq_stimulus(inputs, outputs),
            "Build a single-entry skid buffer for a ready/valid stream.",
            ["skid_buffer", "ready_valid", f"width_{width}"],
        )

        inputs = [("clk", 1), ("rst", 1), ("we", 1), ("waddr", 2), ("wdata", width), ("raddr", 2)]
        outputs = [out("rdata", width), out("write_seen", 1, True)]
        solution = (
            f"reg [{width - 1}:0] mem [0:3];\n"
            "integer j;\n"
            "assign rdata = mem[raddr];\n"
            "always @(posedge clk) begin\n"
            "  if (rst) begin\n"
            "    for (j = 0; j < 4; j = j + 1) mem[j] <= 0;\n"
            "    write_seen <= 1'b0;\n"
            "  end else begin\n"
            "    write_seen <= we;\n"
            "    if (we) mem[waddr] <= wdata;\n"
            "  end\n"
            "end\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L4",
            "generation_storage",
            f"regfile4_{width}w",
            inputs,
            outputs,
            solution,
            seq_stimulus(inputs, outputs),
            "Implement a 4-entry register file with synchronous writes and async reads.",
            ["regfile", "storage", f"width_{width}"],
        )

        inputs = [("clk", 1), ("rst", 1), ("push", 1), ("pop", 1), ("din", width)]
        outputs = [out("dout", width), out("full"), out("empty"), out("count", 2)]
        solution = (
            f"reg [{width - 1}:0] mem0;\n"
            f"reg [{width - 1}:0] mem1;\n"
            "reg [1:0] cnt;\n"
            "wire do_push;\n"
            "wire do_pop;\n"
            "assign full = (cnt == 2'd2);\n"
            "assign empty = (cnt == 2'd0);\n"
            "assign count = cnt;\n"
            "assign dout = mem0;\n"
            "assign do_push = push && !full;\n"
            "assign do_pop = pop && !empty;\n"
            "always @(posedge clk) begin\n"
            "  if (rst) begin\n"
            "    cnt <= 0;\n"
            "    mem0 <= 0;\n"
            "    mem1 <= 0;\n"
            "  end else begin\n"
            "    case ({do_push, do_pop})\n"
            "      2'b10: begin\n"
            "        if (cnt == 0) mem0 <= din;\n"
            "        else mem1 <= din;\n"
            "        cnt <= cnt + 1'b1;\n"
            "      end\n"
            "      2'b01: begin\n"
            "        if (cnt == 2) mem0 <= mem1;\n"
            "        cnt <= cnt - 1'b1;\n"
            "      end\n"
            "      2'b11: begin\n"
            "        if (cnt == 2) begin\n"
            "          mem0 <= mem1;\n"
            "          mem1 <= din;\n"
            "        end else begin\n"
            "          mem0 <= din;\n"
            "        end\n"
            "      end\n"
            "      default: begin end\n"
            "    endcase\n"
            "  end\n"
            "end\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L4",
            "generation_fifo",
            f"fifo2_{width}w",
            inputs,
            outputs,
            solution,
            seq_stimulus(inputs, outputs),
            "Implement a tiny two-entry FIFO with push/pop/full/empty/count behavior.",
            ["fifo", "queue", f"width_{width}"],
        )

        inputs = [("clk", 1), ("rst", 1), ("psel", 1), ("penable", 1), ("pwrite", 1), ("paddr", 2), ("pwdata", width)]
        outputs = [out("prdata", width, True), out("pready"), out("irq", 1, True)]
        solution = (
            f"reg [{width - 1}:0] control;\n"
            f"reg [{width - 1}:0] status;\n"
            "assign pready = psel && penable;\n"
            "always @(posedge clk) begin\n"
            "  if (rst) begin\n"
            "    control <= 0;\n"
            "    status <= 0;\n"
            "    prdata <= 0;\n"
            "    irq <= 1'b0;\n"
            "  end else begin\n"
            "    status <= status + 1'b1;\n"
            "    if (pready && pwrite && paddr == 2'd0) control <= pwdata;\n"
            "    if (pready && pwrite && paddr == 2'd1) irq <= 1'b0;\n"
            "    else if (status[3]) irq <= control[0];\n"
            "    if (pready && !pwrite) begin\n"
            "      case (paddr)\n"
            "        2'd0: prdata <= control;\n"
            "        2'd1: prdata <= status;\n"
            f"        default: prdata <= {width}'d0;\n"
            "      endcase\n"
            "    end\n"
            "  end\n"
            "end\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L4",
            "generation_bus_register",
            f"apb_status_block_{width}w",
            inputs,
            outputs,
            solution,
            seq_stimulus(inputs, outputs),
            "Implement a small APB-like status/control register block with IRQ clear.",
            ["apb", "csr", f"width_{width}"],
        )

        inputs = [("clk", 1), ("rst", 1), ("valid_i", 1), ("ready_i", 1), ("last_i", 1)]
        outputs = [out("in_packet", 1, True), out("packet_done", 1, True), out("beat_count", width, True), out("overflow", 1, True)]
        solution = (
            "wire fire;\n"
            "assign fire = valid_i && ready_i;\n"
            "always @(posedge clk) begin\n"
            "  if (rst) begin\n"
            "    in_packet <= 1'b0;\n"
            "    packet_done <= 1'b0;\n"
            "    beat_count <= 0;\n"
            "    overflow <= 1'b0;\n"
            "  end else begin\n"
            "    packet_done <= 1'b0;\n"
            "    overflow <= 1'b0;\n"
            "    if (fire) begin\n"
            "      in_packet <= !last_i;\n"
            "      packet_done <= last_i;\n"
            "      if (last_i) beat_count <= 0;\n"
            f"      else if (beat_count == {{{width}{{1'b1}}}}) overflow <= 1'b1;\n"
            "      else beat_count <= beat_count + 1'b1;\n"
            "    end\n"
            "  end\n"
            "end\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L4",
            "generation_stream_block",
            f"stream_packet_counter_{width}w",
            inputs,
            outputs,
            solution,
            seq_stimulus(inputs, outputs),
            "Track packet boundaries on a ready/valid stream and count beats.",
            ["stream", "packet_counter", f"width_{width}"],
        )


def build_l5(rows: list[dict[str, Any]]) -> None:
    widths = [8, 10, 12, 16, 24]
    for variant, width in enumerate(widths):
        cw = clog2(width + 1)
        inputs = [("clk", 1), ("rst", 1), ("start", 1), ("data_i", width)]
        outputs = [out("busy", 1, True), out("done", 1, True), out("mosi", 1, True), out("bit_count", cw, True)]
        solution = (
            f"reg [{width - 1}:0] shift;\n"
            "always @(posedge clk) begin\n"
            "  if (rst) begin\n"
            "    busy <= 1'b0;\n"
            "    done <= 1'b0;\n"
            "    mosi <= 1'b0;\n"
            "    bit_count <= 0;\n"
            "    shift <= 0;\n"
            "  end else begin\n"
            "    done <= 1'b0;\n"
            "    if (start && !busy) begin\n"
            "      busy <= 1'b1;\n"
            "      shift <= data_i;\n"
            "      bit_count <= 0;\n"
            f"      mosi <= data_i[{width - 1}];\n"
            "    end else if (busy) begin\n"
            "      shift <= shift << 1;\n"
            f"      mosi <= shift[{width - 2}];\n"
            f"      if (bit_count == {cw}'d{width - 1}) begin\n"
            "        busy <= 1'b0;\n"
            "        done <= 1'b1;\n"
            "      end else begin\n"
            "        bit_count <= bit_count + 1'b1;\n"
            "      end\n"
            "    end\n"
            "  end\n"
            "end\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L5",
            "generation_serial_controller",
            f"spi_shift_tx_{width}b",
            inputs,
            outputs,
            solution,
            seq_stimulus(inputs, outputs, 100),
            "Implement a serial transmit shifter with start, busy, done, and MOSI output.",
            ["spi", "serializer", f"width_{width}"],
        )

        inputs = [("clk", 1), ("rst", 1), ("enable", 1), ("period", width), ("duty", width)]
        outputs = [out("pwm", 1, True), out("rollover", 1, True), out("count", width, True)]
        solution = (
            "always @(posedge clk) begin\n"
            "  if (rst) begin\n"
            "    count <= 0;\n"
            "    pwm <= 1'b0;\n"
            "    rollover <= 1'b0;\n"
            "  end else begin\n"
            "    rollover <= 1'b0;\n"
            "    if (!enable) begin\n"
            "      count <= 0;\n"
            "      pwm <= 1'b0;\n"
            "    end else begin\n"
            "      pwm <= (count < duty);\n"
            "      if (count >= period) begin\n"
            "        count <= 0;\n"
            "        rollover <= 1'b1;\n"
            "      end else begin\n"
            "        count <= count + 1'b1;\n"
            "      end\n"
            "    end\n"
            "  end\n"
            "end\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L5",
            "generation_pwm_controller",
            f"pwm_controller_{width}w",
            inputs,
            outputs,
            solution,
            seq_stimulus(inputs, outputs, 100),
            "Implement a PWM controller with programmable period and duty cycle.",
            ["pwm", "controller", f"width_{width}"],
        )

        max_tokens = (1 << min(width, 12)) - 1
        token_width = min(width, 12)
        inputs = [("clk", 1), ("rst", 1), ("refill", 1), ("consume", 1)]
        outputs = [out("allow"), out("tokens", token_width, True), out("underflow", 1, True)]
        solution = (
            "assign allow = (tokens != 0);\n"
            "always @(posedge clk) begin\n"
            "  if (rst) begin\n"
            "    tokens <= 0;\n"
            "    underflow <= 1'b0;\n"
            "  end else begin\n"
            "    underflow <= 1'b0;\n"
            f"    if (refill && tokens != {token_width}'d{max_tokens}) tokens <= tokens + 1'b1;\n"
            "    if (consume && tokens != 0) tokens <= tokens - 1'b1;\n"
            "    else if (consume && tokens == 0) underflow <= 1'b1;\n"
            "  end\n"
            "end\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L5",
            "generation_rate_limiter",
            f"token_bucket_{token_width}w",
            inputs,
            outputs,
            solution,
            seq_stimulus(inputs, outputs, 100),
            "Implement a token-bucket rate limiter with underflow reporting.",
            ["rate_limiter", "token_bucket", f"width_{token_width}"],
        )

        length = 4 + variant * 2
        lw = clog2(length + 1)
        addr_width = max(width, 12)
        inputs = [("clk", 1), ("rst", 1), ("start", 1), ("ready", 1), ("base", addr_width)]
        outputs = [out("valid", 1, True), out("addr", addr_width, True), out("done", 1, True), out("beat", lw, True)]
        solution = (
            "always @(posedge clk) begin\n"
            "  if (rst) begin\n"
            "    valid <= 1'b0;\n"
            "    addr <= 0;\n"
            "    done <= 1'b0;\n"
            "    beat <= 0;\n"
            "  end else begin\n"
            "    done <= 1'b0;\n"
            "    if (start && !valid) begin\n"
            "      valid <= 1'b1;\n"
            "      addr <= base;\n"
            "      beat <= 0;\n"
            "    end else if (valid && ready) begin\n"
            f"      if (beat == {lw}'d{length - 1}) begin\n"
            "        valid <= 1'b0;\n"
            "        done <= 1'b1;\n"
            "      end else begin\n"
            "        beat <= beat + 1'b1;\n"
            "        addr <= addr + 4;\n"
            "      end\n"
            "    end\n"
            "  end\n"
            "end\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L5",
            "generation_dma_controller",
            f"dma_burst_ctrl_{length}beat",
            inputs,
            outputs,
            solution,
            seq_stimulus(inputs, outputs, 100),
            "Implement a DMA-like burst address generator with valid/ready and done.",
            ["dma", "burst", f"length_{length}"],
        )

        timeout = 8 + variant * 5
        tw = clog2(timeout + 2)
        inputs = [("clk", 1), ("rst", 1), ("enable", 1), ("kick", 1)]
        outputs = [out("expired", 1, True), out("count", tw, True)]
        solution = (
            "always @(posedge clk) begin\n"
            "  if (rst) begin\n"
            "    expired <= 1'b0;\n"
            "    count <= 0;\n"
            "  end else if (!enable || kick) begin\n"
            "    expired <= 1'b0;\n"
            "    count <= 0;\n"
            f"  end else if (count == {tw}'d{timeout}) begin\n"
            "    expired <= 1'b1;\n"
            "  end else begin\n"
            "    count <= count + 1'b1;\n"
            "  end\n"
            "end\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L5",
            "generation_watchdog",
            f"watchdog_{timeout}",
            inputs,
            outputs,
            solution,
            seq_stimulus(inputs, outputs, 100),
            "Implement a watchdog timer with enable, kick, and sticky expired output.",
            ["watchdog", "timeout", f"timeout_{timeout}"],
        )

        inputs = [("clk", 1), ("rst", 1), ("en", 1), ("data_i", 1)]
        outputs = [out("data_o", 1, True), out("lfsr", width, True)]
        solution = (
            "wire feedback;\n"
            f"assign feedback = lfsr[{width - 1}] ^ lfsr[{max(0, width - 3)}] ^ data_i;\n"
            "always @(posedge clk) begin\n"
            "  if (rst) begin\n"
            f"    lfsr <= {width}'h1;\n"
            "    data_o <= 1'b0;\n"
            "  end else if (en) begin\n"
            "    data_o <= feedback;\n"
            "    lfsr <= (lfsr << 1) | feedback;\n"
            "  end\n"
            "end\n"
            "endmodule"
        )
        add_problem(
            rows,
            "L5",
            "generation_scrambler",
            f"lfsr_scrambler_{width}w",
            inputs,
            outputs,
            solution,
            seq_stimulus(inputs, outputs, 100),
            "Implement a bit-serial LFSR scrambler with feedback and retained state.",
            ["lfsr", "scrambler", f"width_{width}"],
        )


def build_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    build_l1(rows)
    build_l2(rows)
    build_l3(rows)
    build_l4(rows)
    build_l5(rows)
    return rows


def build_candidates(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "task_id": row["task_id"],
            "completion": row["canonical_solution"],
            "candidate_source": "canonical_baseline",
        }
        for row in rows
    ]


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")


def md_escape(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def write_catalog(out_dir: Path, rows: list[dict[str, Any]]) -> None:
    lines = [
        "# Generation Benchmark Catalog",
        "",
        f"- Total tasks: {len(rows)}",
        "- Layout: 30 tasks per level, L1-L5",
        "- Difficulty target: realistic RTL generation, not single-expression smoke tests",
        "- Candidate file: canonical baseline completions for verifier sanity checks",
        "",
        "| Level | Type | Count |",
        "|---|---|---:|",
    ]
    by_pair = Counter((row["level"], row["type"]) for row in rows)
    for (level, qtype), count in sorted(by_pair.items()):
        lines.append(f"| {level} | {qtype} | {count} |")
    lines += [
        "",
        "## Tasks",
        "",
        "| Task | Level | Type | Tags | Description |",
        "|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['task_id']} | {row['level']} | {row['type']} | "
            f"{md_escape(', '.join(row['tags']))} | {md_escape(row['description'])} |"
        )
    (out_dir / "catalog.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_benchmark(out_dir: Path, rows: list[dict[str, Any]]) -> None:
    candidates = build_candidates(rows)
    write_jsonl(out_dir / "problems_all.jsonl", rows)
    write_jsonl(out_dir / "candidates_all.jsonl", candidates)
    for level in LEVELS:
        level_rows = [row for row in rows if row["level"] == level]
        level_ids = {row["task_id"] for row in level_rows}
        write_jsonl(out_dir / f"{level.lower()}.jsonl", level_rows)
        write_jsonl(out_dir / f"candidates_{level.lower()}.jsonl", [row for row in candidates if row["task_id"] in level_ids])
    summary = {
        "total": len(rows),
        "levels": dict(sorted(Counter(row["level"] for row in rows).items())),
        "types": dict(sorted(Counter(row["type"] for row in rows).items())),
        "candidate_source": "canonical_baseline",
        "difficulty_target": "realistic RTL generation",
    }
    write_json(out_dir / "summary.json", summary)
    write_catalog(out_dir, rows)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the 150-task realistic Verilog generation benchmark")
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    rows = build_rows()
    if len(rows) != 150:
        raise SystemExit(f"expected 150 rows, got {len(rows)}")
    write_benchmark(args.out_dir, rows)
    print(json.dumps({"status": "ok", "out_dir": str(args.out_dir), "total": len(rows)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
