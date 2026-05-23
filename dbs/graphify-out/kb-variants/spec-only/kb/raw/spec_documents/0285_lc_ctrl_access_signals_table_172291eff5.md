# Spec Document: opentitan/hw/ip/lc_ctrl/doc/lc_ctrl_access_signals_table.md

- Project: `opentitan`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\ip\lc_ctrl\doc\lc_ctrl_access_signals_table.md`
- Exported path: `D:\MyWork\verilog\out\spec_documents_20260514_204108\opentitan\hw\ip\lc_ctrl\doc\lc_ctrl_access_signals_table.md`
- Original extension: `.md`
- Original bytes: 2022

## Content

<table style="text-align:center;font-size:small">
  <tr>
    <td style="text-align:left"><strong>State \ Function</strong></td>
    <td><strong>CREATOR_SEED_SW_RW_EN</strong></td>
    <td><strong>OWNER_SEED_SW_RW_EN</strong></td>
    <td><strong>SEED_HW_RD_EN</strong></td>
    <td><strong>ISO_PART_SW_RD_EN</strong></td>
    <td><strong>ISO_PART_SW_WR_EN</strong></td>
    <td><strong>RMA_STATE</strong></td>
  </tr>
  <tr>
    <td style="text-align:left">RAW</td>
    <td colspan="6" style="background:#dadce0"></td>
  </tr>
  <tr>
   <td style="text-align:left">TEST_LOCKED</td>
   <td colspan="6" style="background:#dadce0"></td>
  </tr>
  <tr>
    <td style="text-align:left">TEST_UNLOCKED</td>
    <td colspan="4" style="background:#dadce0"></td><td>Y</td><td colspan="1" style="background:#dadce0"></td>
  </tr>
  <tr>
    <td style="text-align:left">DEV</td>
    <td>Y*</td><td>Y</td><td>Y*</td><td colspan="1" style="background:#dadce0"></td><td>Y</td><td colspan="1" style="background:#dadce0"></td>
  </tr>
  <tr>
    <td style="text-align:left">PROD</td>
    <td>Y*</td><td>Y</td><td>Y*</td><td>Y</td><td>Y</td><td colspan="1" style="background:#dadce0"></td>
  </tr>
  <tr>
    <td style="text-align:left">PROD_END</td>
    <td>Y*</td><td>Y</td><td>Y*</td><td>Y</td><td>Y</td><td colspan="1" style="background:#dadce0"></td>
  </tr>
  <tr>
    <td style="text-align:left">RMA</td>
    <td>Y</td><td>Y</td><td>Y</td><td>Y</td><td>Y</td><td>Y</td>
  </tr>
  <tr>
    <td style="text-align:left">SCRAP</td>
    <td colspan="6" style="background:#dadce0"></td>
  </tr>
  <tr>
    <td style="text-align:left;color:red">INVALID</td>
    <td colspan="6" style="background:#dadce0"></td>
  </tr>
  <tr>
    <td style="text-align:left;color:red">POST_TRANSITION</td>
    <td colspan="6" style="background:#dadce0"></td>
  </tr>
  <tr>
    <td style="text-align:left;color:red">ESCALATION</td>
    <td colspan="6" style="background:#dadce0"></td>
  </tr>
</table>
