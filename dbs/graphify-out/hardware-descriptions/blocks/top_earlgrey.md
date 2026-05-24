# Hardware Description: top_earlgrey

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `top_earlgrey`
- `bridge_edge_count`: 40
- Spec categories: component: 41
- Code categories: rtl: 14, sva: 13, dv: 13
- Bridge relations: spec_component_matches_code: 40

## Spec Anchors

- `component:top_earlgrey` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**RTL** (14)
  - `top_earlgrey_rnd_cnst_pkg.sv`:L1 — `opentitan\hw\top_earlgrey\rtl\autogen\testing\top_earlgrey_rnd_cnst_pkg.sv`
  - `top_earlgrey_racl_pkg.sv`:L1 — `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey_racl_pkg.sv`
  - `top_earlgrey`:L1047 — `opentitan\hw\top_earlgrey\rtl\autogen\chip_earlgrey_cw340.sv`
  - `top_earlgrey_pkg.sv`:L1 — `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey_pkg.sv`
  - `top_earlgrey_pkg`:L249 — `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`
  - `top_earlgrey.sv`:L1 — `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`
  - `top_earlgrey`:L11 — `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`
  - `top_earlgrey_rnd_cnst_pkg`:L251 — `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`
  - `alert_handler_ping_timer.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_ping_timer.sv`
  - `alert_handler_ping_timer`:L24 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_ping_timer.sv`
  - `flash_ctrl_top_specific_pkg.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\flash_ctrl\rtl\flash_ctrl_top_specific_pkg.sv`
  - `alert_handler_esc_timer.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_esc_timer.sv`
  - `alert_handler_esc_timer`:L21 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_esc_timer.sv`
  - `rv_core_ibex_cfg_reg_top.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_cfg_reg_top.sv`
**DV** (13)
  - `alert_handler_ping_timer_bind_fpv.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\tb\alert_handler_ping_timer_bind_fpv.sv`
  - `alert_handler_ping_timer_bind_fpv`:L6 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\tb\alert_handler_ping_timer_bind_fpv.sv`
  - `alert_handler_esc_timer_bind_fpv.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\tb\alert_handler_esc_timer_bind_fpv.sv`
  - `alert_handler_esc_timer_bind_fpv`:L6 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\tb\alert_handler_esc_timer_bind_fpv.sv`
  - `alert_handler_ping_timer_tb.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\tb\alert_handler_ping_timer_tb.sv`
  - `alert_handler_ping_timer_tb`:L8 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\tb\alert_handler_ping_timer_tb.sv`
  - `alert_handler_esc_timer_tb.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\tb\alert_handler_esc_timer_tb.sv`
  - `alert_handler_esc_timer_tb`:L8 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\tb\alert_handler_esc_timer_tb.sv`
  - `alert_handler_base_test.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\dv\tests\alert_handler_base_test.sv`
  - `alert_handler_env_pkg`:L9 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\dv\tests\alert_handler_test_pkg.sv`
  - `alert_handler_test_pkg.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\dv\tests\alert_handler_test_pkg.sv`
  - `alert_handler_cov_bind.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv`
  - `alert_handler_cov_bind`:L7 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv`
**SVA** (13)
  - `top_earlgrey_bind.sv`:L1 — `opentitan\hw\top_earlgrey\dv\sva\top_earlgrey_bind.sv`
  - `top_earlgrey_bind`:L5 — `opentitan\hw\top_earlgrey\dv\sva\top_earlgrey_bind.sv`
  - `alert_handler_ping_timer_assert_fpv.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\vip\alert_handler_ping_timer_assert_fpv.sv`
  - `alert_handler_ping_timer_assert_fpv`:L10 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\vip\alert_handler_ping_timer_assert_fpv.sv`
  - `alert_handler_esc_timer_assert_fpv.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\vip\alert_handler_esc_timer_assert_fpv.sv`
  - `alert_handler_esc_timer_assert_fpv`:L10 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\vip\alert_handler_esc_timer_assert_fpv.sv`
  - `clkmgr_lost_calib_ctrl_en_sva_if.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv`
  - `clkmgr_lost_calib_regwen_sva_if.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv`
  - `clkmgr_sec_cm_checker_assert.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv`
  - `clkmgr_sec_cm_checker_assert`:L7 — `opentitan\hw\top_earlgrey\ip_autogen\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv`
  - `pwrmgr_sec_cm_checker_assert.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv`
  - `pwrmgr_sec_cm_checker_assert`:L7 — `opentitan\hw\top_earlgrey\ip_autogen\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv`
  - `pwrmgr_clock_enables_sva_if.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\pwrmgr\dv\sva\pwrmgr_clock_enables_sva_if.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:top_earlgrey` | `top_earlgrey_rnd_cnst_pkg.sv` | `opentitan\hw\top_earlgrey\rtl\autogen\testing\top_earlgrey_rnd_cnst_pkg.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `top_earlgrey_racl_pkg.sv` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey_racl_pkg.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `top_earlgrey` | `opentitan\hw\top_earlgrey\rtl\autogen\chip_earlgrey_cw340.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `top_earlgrey_pkg.sv` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey_pkg.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `top_earlgrey_bind.sv` | `opentitan\hw\top_earlgrey\dv\sva\top_earlgrey_bind.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `top_earlgrey_bind` | `opentitan\hw\top_earlgrey\dv\sva\top_earlgrey_bind.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `top_earlgrey_pkg` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `top_earlgrey.sv` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `top_earlgrey` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `top_earlgrey_rnd_cnst_pkg` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `alert_handler_ping_timer_assert_fpv.sv` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\vip\alert_handler_ping_timer_assert_fpv.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `alert_handler_ping_timer_assert_fpv` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\vip\alert_handler_ping_timer_assert_fpv.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `alert_handler_esc_timer_assert_fpv.sv` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\vip\alert_handler_esc_timer_assert_fpv.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `alert_handler_esc_timer_assert_fpv` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\vip\alert_handler_esc_timer_assert_fpv.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `alert_handler_ping_timer_bind_fpv.sv` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\tb\alert_handler_ping_timer_bind_fpv.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `alert_handler_ping_timer_bind_fpv` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\tb\alert_handler_ping_timer_bind_fpv.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `alert_handler_esc_timer_bind_fpv.sv` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\tb\alert_handler_esc_timer_bind_fpv.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `alert_handler_esc_timer_bind_fpv` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\tb\alert_handler_esc_timer_bind_fpv.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `alert_handler_ping_timer_tb.sv` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\tb\alert_handler_ping_timer_tb.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `alert_handler_ping_timer_tb` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\tb\alert_handler_ping_timer_tb.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `alert_handler_esc_timer_tb.sv` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\tb\alert_handler_esc_timer_tb.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `alert_handler_esc_timer_tb` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\tb\alert_handler_esc_timer_tb.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `alert_handler_base_test.sv` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\dv\tests\alert_handler_base_test.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\top_earlgrey\ip_autogen\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `alert_handler_env_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\dv\tests\alert_handler_test_pkg.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `alert_handler_test_pkg.sv` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\dv\tests\alert_handler_test_pkg.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\top_earlgrey\ip_autogen\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `alert_handler_cov_bind.sv` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `alert_handler_cov_bind` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `alert_handler_ping_timer.sv` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_ping_timer.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `alert_handler_ping_timer` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_ping_timer.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\top_earlgrey\ip_autogen\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `clkmgr_sec_cm_checker_assert` | `opentitan\hw\top_earlgrey\ip_autogen\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `flash_ctrl_top_specific_pkg.sv` | `opentitan\hw\top_earlgrey\ip_autogen\flash_ctrl\rtl\flash_ctrl_top_specific_pkg.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `pwrmgr_sec_cm_checker_assert.sv` | `opentitan\hw\top_earlgrey\ip_autogen\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `pwrmgr_sec_cm_checker_assert` | `opentitan\hw\top_earlgrey\ip_autogen\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `alert_handler_esc_timer.sv` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_esc_timer.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `alert_handler_esc_timer` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_esc_timer.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `pwrmgr_clock_enables_sva_if.sv` | `opentitan\hw\top_earlgrey\ip_autogen\pwrmgr\dv\sva\pwrmgr_clock_enables_sva_if.sv` |
| `spec_component_matches_code` | `component:top_earlgrey` | `rv_core_ibex_cfg_reg_top.sv` | `opentitan\hw\top_earlgrey\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_cfg_reg_top.sv` |

## Retrieval Guidance

- For code-only queries mentioning `top_earlgrey`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `top_earlgrey`.
