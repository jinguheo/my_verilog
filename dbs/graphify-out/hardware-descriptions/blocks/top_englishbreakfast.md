# Hardware Description: top_englishbreakfast

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `top_englishbreakfast`
- `bridge_edge_count`: 40
- Spec categories: component: 41
- Code categories: rtl: 25, sva: 10, dv: 5
- Bridge relations: spec_component_matches_code: 40

## Spec Anchors

- `component:top_englishbreakfast` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**RTL** (25)
  - `top_englishbreakfast_rnd_cnst_pkg.sv`:L1 — `opentitan\hw\top_englishbreakfast\rtl\autogen\testing\top_englishbreakfast_rnd_cnst_pkg.sv`
  - `top_englishbreakfast_racl_pkg.sv`:L1 — `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast_racl_pkg.sv`
  - `top_englishbreakfast`:L957 — `opentitan\hw\top_englishbreakfast\rtl\autogen\chip_englishbreakfast_cw305.sv`
  - `top_englishbreakfast_pkg.sv`:L1 — `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast_pkg.sv`
  - `top_englishbreakfast_pkg`:L168 — `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv`
  - `top_englishbreakfast.sv`:L1 — `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv`
  - `top_englishbreakfast`:L11 — `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv`
  - `top_englishbreakfast_rnd_cnst_pkg`:L170 — `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv`
  - `flash_ctrl_pkg`:L11 — `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_top_specific_pkg.sv`
  - `flash_ctrl_top_specific_pkg.sv`:L1 — `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_top_specific_pkg.sv`
  - `tlul_socket_1n`:L107 — `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_cfg_reg_top.sv`
  - `rv_core_ibex_reg_pkg`:L27 — `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_cfg_reg_top.sv`
  - `rv_core_ibex_cfg_reg_top.sv`:L1 — `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_cfg_reg_top.sv`
  - `rv_core_ibex_cfg_reg_top`:L9 — `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_cfg_reg_top.sv`
  - `prim_arbiter_fixed`:L58 — `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv`
  - `rv_core_ibex_pkg`:L11 — `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv`
  - `rv_core_ibex_addr_trans.sv`:L1 — `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv`
  - `rv_core_ibex_addr_trans`:L11 — `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv`
  - `flash_mp_data_region_sel.sv`:L1 — `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_mp_data_region_sel.sv`
  - `flash_mp_data_region_sel`:L10 — `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_mp_data_region_sel.sv`
**DV** (5)
  - `flash_ctrl_base_test.sv`:L1 — `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\tests\flash_ctrl_base_test.sv`
  - `flash_ctrl_env_pkg`:L9 — `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\tests\flash_ctrl_test_pkg.sv`
  - `flash_ctrl_phy_cov_if.sv`:L1 — `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\cov\flash_ctrl_phy_cov_if.sv`
  - `flash_ctrl_test_pkg.sv`:L1 — `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\tests\flash_ctrl_test_pkg.sv`
  - `flash_ctrl_cov_bind.sv`:L1 — `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\cov\flash_ctrl_cov_bind.sv`
**SVA** (10)
  - `clkmgr_lost_calib_ctrl_en_sva_if.sv`:L1 — `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv`
  - `clkmgr_lost_calib_regwen_sva_if.sv`:L1 — `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv`
  - `clkmgr_sec_cm_checker_assert.sv`:L1 — `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv`
  - `clkmgr_sec_cm_checker_assert`:L7 — `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv`
  - `pwrmgr_sec_cm_checker_assert.sv`:L1 — `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv`
  - `pwrmgr_sec_cm_checker_assert`:L7 — `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv`
  - `pwrmgr_clock_enables_sva_if.sv`:L1 — `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\sva\pwrmgr_clock_enables_sva_if.sv`
  - `rstmgr_rst_en_track_sva_if.sv`:L1 — `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\sva\rstmgr_rst_en_track_sva_if.sv`
  - `clkmgr_gated_clock_sva_if.sv`:L1 — `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv`
  - `clkmgr_aon_cg_en_sva_if.sv`:L1 — `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:top_englishbreakfast` | `top_englishbreakfast_rnd_cnst_pkg.sv` | `opentitan\hw\top_englishbreakfast\rtl\autogen\testing\top_englishbreakfast_rnd_cnst_pkg.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `top_englishbreakfast_racl_pkg.sv` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast_racl_pkg.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `top_englishbreakfast` | `opentitan\hw\top_englishbreakfast\rtl\autogen\chip_englishbreakfast_cw305.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `top_englishbreakfast_pkg.sv` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast_pkg.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `top_englishbreakfast_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `top_englishbreakfast.sv` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `top_englishbreakfast` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `top_englishbreakfast_rnd_cnst_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `flash_ctrl_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_top_specific_pkg.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `clkmgr_sec_cm_checker_assert` | `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `flash_ctrl_top_specific_pkg.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_top_specific_pkg.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `pwrmgr_sec_cm_checker_assert.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `pwrmgr_sec_cm_checker_assert` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `tlul_socket_1n` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_cfg_reg_top.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `rv_core_ibex_reg_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_cfg_reg_top.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `pwrmgr_clock_enables_sva_if.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\sva\pwrmgr_clock_enables_sva_if.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `rv_core_ibex_cfg_reg_top.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_cfg_reg_top.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `rv_core_ibex_cfg_reg_top` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_cfg_reg_top.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `prim_arbiter_fixed` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `rv_core_ibex_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `flash_ctrl_base_test.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\tests\flash_ctrl_base_test.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `rstmgr_rst_en_track_sva_if.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\sva\rstmgr_rst_en_track_sva_if.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `rv_core_ibex_addr_trans.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `rv_core_ibex_addr_trans` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `flash_ctrl_env_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\tests\flash_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `flash_ctrl_phy_cov_if.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\cov\flash_ctrl_phy_cov_if.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `flash_ctrl_test_pkg.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\tests\flash_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `flash_mp_data_region_sel.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_mp_data_region_sel.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `flash_mp_data_region_sel` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_mp_data_region_sel.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `prim_subreg_shadow` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_core_reg_top.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `flash_ctrl_core_reg_top.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_core_reg_top.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `flash_ctrl_core_reg_top` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_core_reg_top.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `flash_ctrl_prim_reg_top.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_prim_reg_top.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `flash_ctrl_prim_reg_top` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_prim_reg_top.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_component_matches_code` | `component:top_englishbreakfast` | `flash_ctrl_cov_bind.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\cov\flash_ctrl_cov_bind.sv` |

## Retrieval Guidance

- For code-only queries mentioning `top_englishbreakfast`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `top_englishbreakfast`.
