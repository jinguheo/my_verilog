# Hardware Description: top_darjeeling

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `top_darjeeling`
- `bridge_edge_count`: 40
- Spec categories: component: 41
- Code categories: dv: 15, rtl: 13, sva: 12
- Bridge relations: spec_component_matches_code: 40

## Spec Anchors

- `component:top_darjeeling` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**RTL** (13)
  - `top_darjeeling_rnd_cnst_pkg.sv`:L1 — `opentitan\hw\top_darjeeling\rtl\autogen\testing\top_darjeeling_rnd_cnst_pkg.sv`
  - `top_darjeeling_soc_dbg_pkg.sv`:L1 — `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling_soc_dbg_pkg.sv`
  - `top_darjeeling_soc_mbx_pkg.sv`:L1 — `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling_soc_mbx_pkg.sv`
  - `top_darjeeling_racl_pkg.sv`:L1 — `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling_racl_pkg.sv`
  - `top_darjeeling`:L1544 — `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv`
  - `top_darjeeling_pkg.sv`:L1 — `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling_pkg.sv`
  - `top_darjeeling_pkg`:L311 — `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
  - `top_darjeeling.sv`:L1 — `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
  - `top_darjeeling`:L13 — `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
  - `top_darjeeling_rnd_cnst_pkg`:L313 — `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
  - `top_darjeeling_racl_pkg`:L314 — `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
  - `alert_handler_ping_timer.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\rtl\alert_handler_ping_timer.sv`
  - `alert_handler_ping_timer`:L24 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\rtl\alert_handler_ping_timer.sv`
**DV** (15)
  - `alert_handler_ping_timer_bind_fpv.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_ping_timer_bind_fpv.sv`
  - `alert_handler_ping_timer_bind_fpv`:L6 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_ping_timer_bind_fpv.sv`
  - `alert_handler_esc_timer_bind_fpv.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_esc_timer_bind_fpv.sv`
  - `alert_handler_esc_timer_bind_fpv`:L6 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_esc_timer_bind_fpv.sv`
  - `ac_range_check_base_test.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_base_test.sv`
  - `alert_handler_ping_timer_tb.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_ping_timer_tb.sv`
  - `alert_handler_ping_timer_tb`:L8 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_ping_timer_tb.sv`
  - `ac_range_check_env_pkg`:L9 — `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv`
  - `ac_range_check_test_pkg.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv`
  - `alert_handler_esc_timer_tb.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_esc_timer_tb.sv`
  - `alert_handler_esc_timer_tb`:L8 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_esc_timer_tb.sv`
  - `alert_handler_base_test.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\tests\alert_handler_base_test.sv`
  - `alert_handler_test_pkg.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\tests\alert_handler_test_pkg.sv`
  - `alert_handler_cov_bind.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv`
  - `alert_handler_cov_bind`:L7 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv`
**SVA** (12)
  - `top_darjeeling_bind.sv`:L1 — `opentitan\hw\top_darjeeling\dv\sva\top_darjeeling_bind.sv`
  - `top_darjeeling_bind`:L5 — `opentitan\hw\top_darjeeling\dv\sva\top_darjeeling_bind.sv`
  - `alert_handler_ping_timer_assert_fpv.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\vip\alert_handler_ping_timer_assert_fpv.sv`
  - `alert_handler_ping_timer_assert_fpv`:L10 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\vip\alert_handler_ping_timer_assert_fpv.sv`
  - `alert_handler_esc_timer_assert_fpv.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\vip\alert_handler_esc_timer_assert_fpv.sv`
  - `alert_handler_esc_timer_assert_fpv`:L10 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\vip\alert_handler_esc_timer_assert_fpv.sv`
  - `clkmgr_lost_calib_ctrl_en_sva_if.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv`
  - `clkmgr_lost_calib_regwen_sva_if.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv`
  - `clkmgr_sec_cm_checker_assert.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv`
  - `clkmgr_sec_cm_checker_assert`:L7 — `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv`
  - `pwrmgr_sec_cm_checker_assert.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv`
  - `pwrmgr_sec_cm_checker_assert`:L7 — `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:top_darjeeling` | `top_darjeeling_rnd_cnst_pkg.sv` | `opentitan\hw\top_darjeeling\rtl\autogen\testing\top_darjeeling_rnd_cnst_pkg.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `top_darjeeling_soc_dbg_pkg.sv` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling_soc_dbg_pkg.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `top_darjeeling_soc_mbx_pkg.sv` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling_soc_mbx_pkg.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `top_darjeeling_racl_pkg.sv` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling_racl_pkg.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `top_darjeeling` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `top_darjeeling_pkg.sv` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling_pkg.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `top_darjeeling_bind.sv` | `opentitan\hw\top_darjeeling\dv\sva\top_darjeeling_bind.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `top_darjeeling_bind` | `opentitan\hw\top_darjeeling\dv\sva\top_darjeeling_bind.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `top_darjeeling_pkg` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `top_darjeeling.sv` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `top_darjeeling` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `top_darjeeling_rnd_cnst_pkg` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `top_darjeeling_racl_pkg` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `alert_handler_ping_timer_assert_fpv.sv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\vip\alert_handler_ping_timer_assert_fpv.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `alert_handler_ping_timer_assert_fpv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\vip\alert_handler_ping_timer_assert_fpv.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `alert_handler_esc_timer_assert_fpv.sv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\vip\alert_handler_esc_timer_assert_fpv.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `alert_handler_esc_timer_assert_fpv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\vip\alert_handler_esc_timer_assert_fpv.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `alert_handler_ping_timer_bind_fpv.sv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_ping_timer_bind_fpv.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `alert_handler_ping_timer_bind_fpv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_ping_timer_bind_fpv.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `alert_handler_esc_timer_bind_fpv.sv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_esc_timer_bind_fpv.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `alert_handler_esc_timer_bind_fpv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_esc_timer_bind_fpv.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `ac_range_check_base_test.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_base_test.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `alert_handler_ping_timer_tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_ping_timer_tb.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `alert_handler_ping_timer_tb` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_ping_timer_tb.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `ac_range_check_env_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `ac_range_check_test_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `alert_handler_esc_timer_tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_esc_timer_tb.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `alert_handler_esc_timer_tb` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_esc_timer_tb.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `alert_handler_base_test.sv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\tests\alert_handler_base_test.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `alert_handler_test_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\tests\alert_handler_test_pkg.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `alert_handler_cov_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `alert_handler_cov_bind` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `alert_handler_ping_timer.sv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\rtl\alert_handler_ping_timer.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `alert_handler_ping_timer` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\rtl\alert_handler_ping_timer.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `clkmgr_sec_cm_checker_assert` | `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `pwrmgr_sec_cm_checker_assert.sv` | `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv` |
| `spec_component_matches_code` | `component:top_darjeeling` | `pwrmgr_sec_cm_checker_assert` | `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv` |

## Retrieval Guidance

- For code-only queries mentioning `top_darjeeling`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `top_darjeeling`.
