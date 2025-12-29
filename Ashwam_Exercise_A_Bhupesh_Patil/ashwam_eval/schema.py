SCHEMA = {
  "journal_id": "string",
  "items": [
    {
      "domain": "symptom | food | emotion | mind",
      "evidence_span": "exact substring from journal",
      "polarity": "present | absent | uncertain",
      "intensity_bucket": "low | medium | high | unknown (optional)",
      "arousal_bucket": "low | medium | high | unknown (emotion only)",
      "time_bucket": "today | last_night | past_week | unknown"
    }
  ]
}