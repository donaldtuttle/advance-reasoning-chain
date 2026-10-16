# Minimal ARC Control Record

Produced internally at answer completion. Sole input to candidate generation.

```json
{
  "active_goal": "<the sentence written at the top of the answer>",
  "headline_claim_id": "C1",
  "headline_claim_text": "<exact span from the answer that states the headline conclusion>",
  "decision_claim_id": null,
  "claims": [
    {
      "id": "C1",
      "text": "<exact answer span>",
      "depends_on": []
    }
  ],
  "terms": [],
  "evidence": []
}
```

## Rules

- `headline_claim_id` is always present and is the sole required root.
- `decision_claim_id` is present only when the answer states an explicit accept/reject/run/ship decision; otherwise null.
- Every load-bearing claim, operative term, and evidence item that the headline or decision depends on must appear with an exact text span.
- `depends_on` and `supports` are the only edges. The enumerator’s boundary is the backward closure of the roots over these edges.
- Anything not linked by those edges is outside the record and cannot generate a candidate.
- No paraphrasing; claim and evidence text must match the answer bytes.
