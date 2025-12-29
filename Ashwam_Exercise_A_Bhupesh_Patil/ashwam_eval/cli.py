import json, argparse, os
from .scorer import score

def run(data_dir, out_dir):
    os.makedirs(out_dir, exist_ok=True)

    journals = {j["journal_id"]: j for j in map(json.loads, open(data_dir + "/journals.jsonl"))}
    golds = {g["journal_id"]: g for g in map(json.loads, open(data_dir + "/gold.jsonl"))}
    preds = {p["journal_id"]: p for p in map(json.loads, open(data_dir + "/sample_predictions.jsonl"))}

    results = []
    for jid, gold in golds.items():
        if jid not in preds:
            continue
        r = score(preds[jid], gold, journals[jid]["text"])
        results.append(r)

    with open(out_dir + "/per_journal_scores.jsonl", "w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")

    summary = {
        "object_f1": sum(r["f1"] for r in results) / len(results),
        "polarity_accuracy": sum(r["polarity_accuracy"] for r in results if r["polarity_accuracy"] is not None) / len(results)
    }

    json.dump(summary, open(out_dir + "/score_summary.json", "w"), indent=2)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run")
    ap.add_argument("--data", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    run(args.data, args.out)

if __name__ == "__main__":
    main()