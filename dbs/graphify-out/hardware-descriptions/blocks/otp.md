# Hardware Description: otp

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **partitions**: //
- **items**: // a MEM file for preloading the OTP in FPGA synthesis or simulation.
- **partitions**: //

## Identity

- `ip_block`: `otp`
- `bridge_edge_count`: 208
- Spec categories: document: 344
- Code categories: rtl: 208, other_code: 59
- Bridge relations: spec_path_matches_code_path: 208

## Spec Excerpts

### partitions
_Source: `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_creator_sw_cfg.hjson`_

```
// SPDX-License-Identifier: Apache-2.0
//
// Use the gen-otp-img.py script to convert this configuration into
// a MEM file for preloading the OTP in FPGA synthesis or simulation.
//

{
    // The partition and item names must correspond with the OTP memory map.
    partitions: [
        {
            name:  "CREATOR_SW_CFG",
            items: [
                {
                    name:  "CREAT
…
```

### items
_Source: `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_creator_sw_cfg.hjson`_

```
// a MEM file for preloading the OTP in FPGA synthesis or simulation.
//

{
    // The partition and item names must correspond with the OTP memory map.
    partitions: [
        {
            name:  "CREATOR_SW_CFG",
            items: [
                {
                    name:  "CREATOR_SW_CFG_DIGEST",
                    value: "0x0",
                },
                {
…
```

### partitions
_Source: `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_dev.hjson`_

```
// SPDX-License-Identifier: Apache-2.0
//
// Use the gen-otp-img.py script to convert this configuration into
// a MEM file for preloading the OTP in FPGA synthesis or simulation.
//

{
    // The partition and item names must correspond with the OTP memory map.
    partitions: [
        {
            name:  "SECRET0",
            lock:  "True",
            items: [
                {
…
```

### lock
_Source: `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_dev.hjson`_

```
// a MEM file for preloading the OTP in FPGA synthesis or simulation.
//

{
    // The partition and item names must correspond with the OTP memory map.
    partitions: [
        {
            name:  "SECRET0",
            lock:  "True",
            items: [
                {
                    name:  "TEST_UNLOCK_TOKEN",
                    value: "<random>",
                }
                {
…
```

### items
_Source: `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_dev.hjson`_

```
//

{
    // The partition and item names must correspond with the OTP memory map.
    partitions: [
        {
            name:  "SECRET0",
            lock:  "True",
            items: [
                {
                    name:  "TEST_UNLOCK_TOKEN",
                    value: "<random>",
                }
                {
                    name:  "TEST_EXIT_TOKEN",
                    valu
…
```

### partitions
_Source: `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_hw_cfg.hjson`_

```
// SPDX-License-Identifier: Apache-2.0
//
// Use the gen-otp-img.py script to convert this configuration into
// a MEM file for preloading the OTP in FPGA synthesis or simulation.
//

{
    // The partition and item names must correspond with the OTP memory map.
    partitions: [
        {
            name:  "HW_CFG0",
            // If set to true, this computes the HW digest value
            //
…
```

### lock
_Source: `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_hw_cfg.hjson`_

```
{
    // The partition and item names must correspond with the OTP memory map.
    partitions: [
        {
            name:  "HW_CFG0",
            // If set to true, this computes the HW digest value
            // and locks the partition.
            lock:  "True",
            items: [
                {
                    name:  "DEVICE_ID",
                    value: "<random>",
…
```

### items
_Source: `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_hw_cfg.hjson`_

```
{
    // The partition and item names must correspond with the OTP memory map.
    partitions: [
        {
            name:  "HW_CFG0",
            // If set to true, this computes the HW digest value
            // and locks the partition.
            lock:  "True",
            items: [
                {
                    name:  "DEVICE_ID",
                    value: "<random>",
…
```

## Spec Anchors

- `otp_ctrl_img_creator_sw_cfg.hjson` (L1) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_creator_sw_cfg.hjson`
- `partitions` (L11) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_creator_sw_cfg.hjson`
- `items` (L14) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_creator_sw_cfg.hjson`
- `otp_ctrl_img_dev.hjson` (L1) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_dev.hjson`
- `partitions` (L11) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_dev.hjson`
- `lock` (L14) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_dev.hjson`
- `items` (L15) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_dev.hjson`
- `state` (L58) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_dev.hjson`
- `count` (L61) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_dev.hjson`
- `otp_ctrl_img_hw_cfg.hjson` (L1) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_hw_cfg.hjson`
- `partitions` (L11) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_hw_cfg.hjson`
- `lock` (L16) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_hw_cfg.hjson`
- `items` (L17) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_hw_cfg.hjson`
- `otp_ctrl_img_owner_sw_cfg.hjson` (L1) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_owner_sw_cfg.hjson`
- `partitions` (L11) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_owner_sw_cfg.hjson`
- `items` (L14) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_owner_sw_cfg.hjson`
- `otp_ctrl_img_prod.hjson` (L1) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_prod.hjson`
- `partitions` (L11) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_prod.hjson`
- `lock` (L14) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_prod.hjson`
- `items` (L15) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_prod.hjson`
- `state` (L58) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_prod.hjson`
- `count` (L61) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_prod.hjson`
- `otp_ctrl_img_raw.hjson` (L1) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_raw.hjson`
- `partitions` (L11) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_raw.hjson`
- `state` (L16) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_raw.hjson`
- `count` (L19) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_raw.hjson`
- `otp_ctrl_img_rma.hjson` (L1) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_rma.hjson`
- `partitions` (L11) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_rma.hjson`
- `lock` (L14) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_rma.hjson`
- `items` (L15) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_rma.hjson`
- `state` (L58) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_rma.hjson`
- `count` (L61) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_rma.hjson`
- `otp_ctrl_img_test_locked0.hjson` (L1) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_test_locked0.hjson`
- `partitions` (L11) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_test_locked0.hjson`
- `items` (L14) — `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_test_locked0.hjson`

## Code Evidence

**OTHER_CODE** (50)
  - `alert_handler.rs`:L1 — `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
  - `AlertClassRegs`:L14 — `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
  - `AlertRegs`:L24 — `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
  - `AlertClass`:L48 — `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
  - `.index()`:L57 — `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
  - `.from_index()`:L67 — `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
  - `AlertEnable`:L80 — `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
  - `AlertEscalate`:L88 — `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
  - `AlertClassConfig`:L96 — `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
  - `.default()`:L105 — `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
  - `.default()`:L117 — `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
  - `.crc32()`:L133 — `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
  - `.try_new()`:L144 — `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
  - `.configure()`:L200 — `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
  - `.local_configure()`:L225 — `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
  - `.class_configure()`:L255 — `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
  - `Crc32Add`:L318 — `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
  - `u32`:L322 — `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
  - `.crc32_add()`:L323 — `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
  - `[T; N]`:L328 — `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`

## Neighbor Components

- `lowrisc_ibex` (2 refs; calls×2)
- `kmac` (2 refs; calls×2)
- `otp.rs` (2 refs; calls×2)
- `prim` (1 refs; calls×1)
- `riscv-tests` (1 refs; calls×1)
- `otbn` (1 refs; calls×1)
- `rom_ctrl` (1 refs; calls×1)
- `aes.c` (1 refs; calls×1)
- `aes_gcm` (1 refs; calls×1)
- `gpio.rs` (1 refs; calls×1)
- `uart` (1 refs; calls×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_path_matches_code_path` | `otp_ctrl_img_creator_sw_cfg.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_creator_sw_cfg.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_creator_sw_cfg.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_creator_sw_cfg.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_creator_sw_cfg.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_creator_sw_cfg.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_creator_sw_cfg.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_creator_sw_cfg.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_dev.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_dev.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_dev.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_dev.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_dev.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_dev.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_dev.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_dev.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_hw_cfg.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_hw_cfg.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_hw_cfg.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_hw_cfg.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_hw_cfg.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_hw_cfg.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_hw_cfg.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_hw_cfg.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_owner_sw_cfg.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_owner_sw_cfg.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_owner_sw_cfg.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_owner_sw_cfg.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_owner_sw_cfg.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_owner_sw_cfg.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_owner_sw_cfg.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_owner_sw_cfg.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_prod.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_prod.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_prod.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_prod.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_prod.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_prod.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_prod.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_prod.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_raw.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_raw.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_raw.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_raw.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_raw.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_raw.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_raw.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_raw.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_rma.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_rma.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_rma.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_rma.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_rma.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_rma.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_rma.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_rma.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_test_locked0.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_test_locked0.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_test_locked0.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_test_locked0.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |

## Retrieval Guidance

- For code-only queries mentioning `otp`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `otp`.
