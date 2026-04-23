# Verilog Skills Workspace

This workspace contains 6 independent skills for a Verilog/SystemVerilog knowledge and design system.

## Included skills
- rtl-source-ingestor
- rtl-structure-parser
- rtl-knowledge-indexer
- rtl-module-qa
- rtl-semantic-labeler
- rtl-design-generator

## Install on Windows
1. Create the target folder if needed:
   - `D:\MyWork\verilog`
2. Extract this zip into `D:\MyWork\verilog`
3. Open PowerShell in `D:\MyWork\verilog`
4. Run one of these:
   - `./setup_git.ps1`
   - or `setup_git.bat`

## Recommended repo layout
This archive already contains the recommended layout.
Each skill folder includes:
- `SKILL.md`
- `agents/openai.yaml`
- `references/*`
- `assets/*`

## Suggested next steps
- Review each `SKILL.md`
- Add orchestration docs if you want a top-level coordinator
- Add Go service code beside each skill, or in a sibling `services/` folder

- rtl-orchestrator: dispatch and sequence the six rtl skills for end-to-end workflows
