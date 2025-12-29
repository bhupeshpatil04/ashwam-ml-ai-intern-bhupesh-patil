Ashwam Exercise A — Evidence-Grounded Extraction & Evaluation

This repository contains a strict implementation of Exercise A, focused on evidence-grounded, deterministic evaluation without canonical labels.

Implemented:
- Extraction schema (JSON)
- Scorer (object-level P/R/F1, polarity accuracy, bucket accuracy, evidence coverage)
- CLI entrypoint
- Mock evaluation using provided sample_predictions.jsonl

CLI:
python -m ashwam_eval.cli run --data ./data --out ./out

Outputs:
out/
├── score_summary.json
└── per_journal_scores.jsonl

Notes:
Matching is based on domain + evidence span overlap
No canonical vocabularies
Deterministic and reproducible
No extra features beyond assignment requirements