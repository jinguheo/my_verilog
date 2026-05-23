# Hardware Description Retrieval Evaluation

- Questions: 150
- Hardware descriptions: `D:\MyWork\verilog\dbs\graphify-out\hardware-descriptions\hardware_descriptions.json`

## Overall

| Method | spec hit@5 | code hit@5 | joint hit@5 | joint hit@10 | joint MRR |
|---|---:|---:|---:|---:|---:|
| code-only current | 0.0 | 0.1267 | 0.0 | 0.0 | 0.0 |
| code-only base | 0.0 | 0.5533 | 0.0 | 0.0 | 0.0 |
| spec-code current | 0.8933 | 0.3 | 0.2533 | 0.3867 | 0.1132 |
| hardware-description | 0.2133 | 0.4933 | 0.0467 | 0.06 | 0.0282 |
| spec-code + hardware-description | 0.8733 | 0.5533 | 0.4667 | 0.5533 | 0.1655 |

## Interpretation

- `hardware-description` evaluates only the generated middle-layer documents.
- `spec-code + hardware-description` fuses existing spec-code graph retrieval with the generated middle layer.
- A useful improvement should mainly appear in code hit and joint hit, because the middle layer is intended to connect code evidence back to spec anchors.

## By Type

### code-only current

| Type | spec hit@5 | code hit@5 | joint hit@5 | joint hit@10 |
|---|---:|---:|---:|---:|
| bridge_disambiguation | 0.0 | 0.2 | 0.0 | 0.0 |
| code_to_spec_trace | 0.0 | 0.1667 | 0.0 | 0.0 |
| requirement_to_rtl | 0.0 | 0.0333 | 0.0 | 0.0 |
| spec_to_code_trace | 0.0 | 0.2 | 0.0 | 0.0 |
| verification_trace | 0.0 | 0.0333 | 0.0 | 0.0 |

### code-only base

| Type | spec hit@5 | code hit@5 | joint hit@5 | joint hit@10 |
|---|---:|---:|---:|---:|
| bridge_disambiguation | 0.0 | 0.9333 | 0.0 | 0.0 |
| code_to_spec_trace | 0.0 | 0.9 | 0.0 | 0.0 |
| requirement_to_rtl | 0.0 | 0.1 | 0.0 | 0.0 |
| spec_to_code_trace | 0.0 | 0.4667 | 0.0 | 0.0 |
| verification_trace | 0.0 | 0.3667 | 0.0 | 0.0 |

### spec-code current

| Type | spec hit@5 | code hit@5 | joint hit@5 | joint hit@10 |
|---|---:|---:|---:|---:|
| bridge_disambiguation | 0.8333 | 0.3333 | 0.2667 | 0.4 |
| code_to_spec_trace | 0.8333 | 0.4667 | 0.3667 | 0.4667 |
| requirement_to_rtl | 1.0 | 0.1667 | 0.1667 | 0.3333 |
| spec_to_code_trace | 0.8 | 0.3333 | 0.2667 | 0.4 |
| verification_trace | 1.0 | 0.2 | 0.2 | 0.3333 |

### hardware-description

| Type | spec hit@5 | code hit@5 | joint hit@5 | joint hit@10 |
|---|---:|---:|---:|---:|
| bridge_disambiguation | 0.1667 | 0.9333 | 0.1667 | 0.1667 |
| code_to_spec_trace | 0.0 | 0.9333 | 0.0 | 0.0 |
| requirement_to_rtl | 0.4 | 0.0333 | 0.0333 | 0.0333 |
| spec_to_code_trace | 0.1 | 0.3667 | 0.0 | 0.0 |
| verification_trace | 0.4 | 0.2 | 0.0333 | 0.1 |

### spec-code + hardware-description

| Type | spec hit@5 | code hit@5 | joint hit@5 | joint hit@10 |
|---|---:|---:|---:|---:|
| bridge_disambiguation | 0.8667 | 0.9333 | 0.8333 | 0.8667 |
| code_to_spec_trace | 0.8333 | 0.8333 | 0.7333 | 0.8333 |
| requirement_to_rtl | 0.9333 | 0.2667 | 0.2333 | 0.3333 |
| spec_to_code_trace | 0.8 | 0.4667 | 0.3333 | 0.4 |
| verification_trace | 0.9333 | 0.2667 | 0.2 | 0.3333 |
