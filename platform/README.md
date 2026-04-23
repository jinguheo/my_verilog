# Verilog Final Monorepo v2

This is the integrated ontology-first platform workspace with **multi-project bootstrap** support.

## Recommended location

Extract to:

`D:\MyWork\verilog\platform`

Your public DBs should exist at:

- `D:\MyWork\verilog\dbs\opentitan`
- `D:\MyWork\verilog\dbs\ibex`
- `D:\MyWork\verilog\dbs\sv-tests`
- `D:\MyWork\verilog\dbs\RTLLM`

## New in v2

- OpenTitan + Ibex multi-project seed generation
- Ibex label extraction
- merged ontology seed / label files
- review-queue preparation helpers
- multi-project embedding row preparation

## Design priority

1. ontology correctness
2. evidence-backed labels
3. relational + graph consistency
4. QA retrieval quality
5. semantic search
6. generation

## Fast start

### 1. Copy `.env.example` to `.env`
```powershell
Copy-Item .env.example .env
```

### 2. Install Python dependency
```powershell
pip install -r requirements.txt
```

### 3. Bootstrap runtime + merged ontology seed + graph
```powershell
cd D:\MyWork\verilog\platform\scripts
.\full_bootstrap.ps1
```

### 4. Run Module QA API
```powershell
.\run_module_qa_api.ps1
```

### 5. Run Vector Search API
```powershell
.\run_vector_search_api.ps1
```

## Output files under D:\MyWork\verilog\out

- `opentitan_ontology_seed.jsonl`
- `ibex_ontology_seed.jsonl`
- `merged_ontology_seed.jsonl`
- `opentitan_labels.jsonl`
- `ibex_labels.jsonl`
- `merged_labels.jsonl`
- `embedding_rows.json`
- `review_candidates.jsonl`

## Ontology recommendation

Start review in this order:
1. OpenTitan protocol labels
2. OpenTitan controller / crypto / memory roles
3. Ibex core / pipeline / controller / register-file style labels
4. shared cross-project canonical labels
