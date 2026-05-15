# Spec-Code KG Late Binding Design

## Decision

Keep the graph stores separate and integrate them at query time.

| Store | Role | Why Keep Separate |
|---|---|---|
| Custom code KG | Primary RTL retrieval engine | It has module, port, instance, label, and IP-block structure tuned for Verilog questions. |
| Graphify | Code exploration and architecture graph | It captures broad cross-file communities and inferred architecture links, but is too broad to be the primary retrieval index. |
| OpenKB | Spec/document wiki graph | It is optimized for document compilation, summaries, concepts, and wiki navigation. |

The integration layer should not physically merge all nodes and edges. Instead,
it should late-bind records by stable shared keys:

- `module_name`
- `ip_block`
- `spec_section`
- `doc_anchor`
- `approved_label`

## Operating Policy

For this spec-code integration workflow, Graphify is treated as a stored
architecture snapshot unless the user explicitly asks to rebuild it.

Do not run `graphify update .` just because the late-binding evaluator or
spec-code design notes changed. The evaluator reads the persisted Graphify
artifacts when architecture context is needed:

```text
graphify-out/GRAPH_REPORT.md
graphify-out/graph.json
```

Run the lightweight late-binding evaluator instead:

```powershell
.\.venv-graphify\Scripts\python.exe .\platform\eval\evaluate_spec_code_late_binding.py
```

Use a full Graphify update only after substantial codebase changes, after
Graphify extraction logic changes, or when fresh community/architecture results
are specifically needed.

## Query-Time Flow

1. Run the user query against the custom code KG.
2. Convert top code KG modules to binding keys:
   - module name
   - project
   - IP block inferred from path
   - approved labels
   - child/parent module names
3. Fetch matching OpenKB document anchors by `ip_block`, `module_name`, and `approved_label`.
4. Add Graphify context only when the query is architectural, cross-module, or asks how blocks relate.
5. Return a merged answer with provenance from each source instead of returning a physically merged graph.

## Binding Confidence

| Confidence | Condition | Use |
|---|---|---|
| High | Spec text/path mentions an exact `module_name` | Strong source-code grounding. |
| Medium | Spec path or text maps to an `ip_block` | Default bridge for IP documentation. |
| Low | Spec text only matches an `approved_label` | Recall expansion; should not be the only evidence. |
| None | No shared key found | Keep as doc-only content. |

## Current Evaluation

Latest evaluation output:

```text
out/spec_code_late_binding_eval/
```

Summary:

- Spec docs scanned: 986
- Docs with any late-binding key: 925, 93.81%
- RTL/spec-like docs linked: 422/426, 99.06%
- Code modules scanned after generic-name filtering: 1383
- Modules with any doc link: 1325, 95.81%
- IP blocks with docs: 56/56, 100.00%

Interpretation:

The spec set connects very well at IP-block level. Exact module-name links are
useful but should be treated as high-confidence evidence, not as the only join
mechanism. Some generic terms such as bus or timer can over-link if treated as
module names, so the integration layer should rank exact module links by
project/path/IP context, not by raw token match alone.

## Recommended Data Contracts

Code KG module card:

```json
{
  "project": "opentitan",
  "module_name": "aes_core",
  "ip_block": "aes",
  "path": ".../hw/ip/aes/rtl/aes_core.sv",
  "approved_labels": ["aes", "crypto"],
  "ports": ["clk_i", "rst_ni"],
  "instances": ["aes_cipher_core"]
}
```

OpenKB spec anchor:

```json
{
  "project": "opentitan",
  "doc_anchor": "opentitan/hw/ip/aes/doc/theory_of_operation.md#aes_operation",
  "ip_block": "aes",
  "spec_section": "theory_of_operation",
  "module_mentions": ["aes_core"],
  "approved_label_mentions": ["crypto"]
}
```

Late-binding edge:

```json
{
  "source": "doc_anchor",
  "target": "module_name",
  "binding_key": "ip_block:aes",
  "confidence": "medium",
  "evidence": "spec path under hw/ip/aes/doc"
}
```

## Next Step

Use `platform/eval/evaluate_spec_code_late_binding.py` as a regression check
whenever spec docs, code KG seed, or approved labels change. The target should
be:

- RTL/spec doc link rate above 95%
- IP-block coverage near 100%
- exact module-name links used only after generic-name filtering
