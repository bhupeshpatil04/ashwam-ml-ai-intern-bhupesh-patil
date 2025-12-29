def span_overlap(a, b):
    return a in b or b in a

def score(pred, gold, journal_text):
    matched_gold = set()
    tp = fp = fn = 0
    polarity_correct = 0
    bucket_correct = 0
    bucket_total = 0
    evidence_valid = 0

    for p in pred["items"]:
        if p["evidence_span"] in journal_text:
            evidence_valid += 1

        match = None
        for i, g in enumerate(gold["items"]):
            if i in matched_gold:
                continue
            if p["domain"] == g["domain"] and span_overlap(p["evidence_span"], g["evidence_span"]):
                match = (i, g)
                break

        if match:
            i, g = match
            matched_gold.add(i)
            tp += 1
            if p["polarity"] == g["polarity"]:
                polarity_correct += 1

            for k in ["intensity_bucket", "arousal_bucket", "time_bucket"]:
                if k in g:
                    bucket_total += 1
                    if p.get(k) == g.get(k):
                        bucket_correct += 1
        else:
            fp += 1

    fn = len(gold["items"]) - len(matched_gold)

    precision = tp / (tp + fp) if tp + fp else 0
    recall = tp / (tp + fn) if tp + fn else 0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0

    return {
        "journal_id": gold["journal_id"],
        "tp": tp,
        "fp": fp,
        "fn": fn,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "polarity_accuracy": polarity_correct / tp if tp else None,
        "bucket_accuracy": bucket_correct / bucket_total if bucket_total else None,
        "evidence_coverage": evidence_valid / len(pred["items"]) if pred["items"] else None
    }