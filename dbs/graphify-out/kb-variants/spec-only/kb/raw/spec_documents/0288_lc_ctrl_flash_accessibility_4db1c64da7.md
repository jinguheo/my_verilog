# Spec Document: opentitan/hw/ip/lc_ctrl/doc/lc_ctrl_flash_accessibility.md

- Project: `opentitan`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\ip\lc_ctrl\doc\lc_ctrl_flash_accessibility.md`
- Exported path: `D:\MyWork\verilog\out\spec_documents_20260514_204108\opentitan\hw\ip\lc_ctrl\doc\lc_ctrl_flash_accessibility.md`
- Original extension: `.md`
- Original bytes: 697

## Content

<table>
<thead>
<tr>
<th>Collateral</th>
<th>SW Program</th>
<th>SW Erase</th>
<th>SW Read</th>
<th>HW Read</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>CREATOR_DATA</td>
<td colspan="3" style="text-align:center;vertical-align:middle">CREATOR_SEED_SW_RW_EN == ON</td>
<td style="text-align:center;vertical-align:middle">SEED_HW_RD_EN == ON</td>
<td>Similar control to creator collateral in OTP.</td>
</tr>
<tr>
<td>OWNER_DATA</td>
<td colspan="3" style="text-align:center;vertical-align:middle">OWNER_SEED_SW_RW_EN == ON</td>
<td style="text-align:center;vertical-align:middle">yes</td>
<td>Follows normal software isolation rules.</td>
</tr>
</tbody>
</table>
