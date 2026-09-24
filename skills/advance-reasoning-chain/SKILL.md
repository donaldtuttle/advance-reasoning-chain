---
name: advance-reasoning-chain
description: Answer the user's current substantive request completely, then append exactly one terminal line — NEXT_PROMPT when another step has material expected value for the user's active goal, or CHAIN_COMPLETE when further recursion is unlikely to change the relevant decision, conclusion, artifact, or action. Use for recursive research, analysis, critique, formalization, experimental design, protocol refinement, specification work, or any conversation that needs rigorous next-step generation without endless refinement. This is a multi-turn process-control protocol that governs what happens between completed answers. Optimize for falsifiability, contract precision, evidence discipline, and goal relevance while allowing the current claim, plan, or proposal to fail.
---

# Advance Reasoning Chain

Answer the current request completely. Then either generate one goal-relevant follow-up prompt or stop the reasoning chain explicitly.

This is a process-control protocol, not an internal chain-of-thought technique. It decides whether a completed answer should terminate or advance through one additional, goal-preserving, materially valuable, and preferably falsifying inquiry.

## Workflow

1. Draft the answer without weakening or shortening it merely to make room for the follow-up.
2. State the user's active goal and the answer's headline conclusion internally in one sentence each. Treat the main claim, recommendation, decision, artifact outcome, or proposed validity judgment as the headline conclusion.
3. Build an unranked candidate set by checking for:
   - an untested assumption or viable alternative explanation;
   - a claim that cannot yet be disproved;
   - an underspecified term, operator, measurement, threshold, or failure condition;
   - a confound, leakage path, circular validation, or evidence-quality gap;
   - a missing boundary case, negative control, replication condition, or decision rule.

   Treat these categories only as discovery aids. Do not infer priority from category, list order, or when a candidate was noticed. Presence of an unresolved issue does not by itself justify continuation.
4. Score every candidate internally on two dimensions:

   | Dimension | 0 | 1 | 2 | 3 |
   | --- | --- | --- | --- | --- |
   | **Change probability (P):** likelihood that resolving the issue would change the headline conclusion | No credible path | Possible but weakly supported | Credible | Likely or directly indicated |
   | **Change magnitude (M):** size of that change | No change | Clarifies wording or a local detail | Materially narrows or reorders the conclusion | Reverses, invalidates, or makes the conclusion unsupported |

   Calculate `expected-effect score = P × M`. This is an ordinal decision score, not a calibrated empirical probability.
5. Score each candidate's expected net value for the user's active goal:

   | Goal value (G) | Meaning |
   | --- | --- |
   | 0 | No plausible effect on the active goal, or expected effort exceeds likely benefit |
   | 1 | Optional clarification, polish, or methodological refinement that would not materially change the result |
   | 2 | Could materially change the user's decision, conclusion, artifact, or planned action and is worth the required effort |
   | 3 | Likely to determine the outcome or prevent a major error |

   Do not assign material value merely because a real unresolved issue exists. Interesting residual questions, additional replications after adequate ones, or further precision that would not alter the decision all score G ≤ 1.
6. If no candidate has `G ≥ 2`, stop and append:

   `CHAIN_COMPLETE: <concise reason further recursion is unlikely to change the active goal>`

7. Otherwise, retain only candidates with `G ≥ 2` and select exactly one. Prefer higher `G`, then higher expected-effect score. Resolve remaining ties in this order:
   1. higher change magnitude;
   2. higher change probability;
   3. a test that more decisively distinguishes whether the conclusion survives or fails;
   4. less new information or scope required;
   5. attachment to the earliest premise in the answer's causal or derivational chain.

   If candidates remain indistinguishable, choose the one expressible in the fewest clauses. Never use issue category as a tie-breaker.
8. Write the smallest prompt that would materially resolve or expose the selected issue. Do not bundle unrelated improvements. Keep the scoring internal unless the user asks to inspect it.
9. Ensure the prompt preserves the user's active goal and current reasoning trajectory, can be pasted verbatim as the next user message, and permits the current position to be rejected, narrowed, or revised.
10. Append it as the final line of the response in exactly this form:

    `NEXT_PROMPT: <prompt>`

## Output Contract

- Emit exactly one terminal line: either `NEXT_PROMPT:` or `CHAIN_COMPLETE:`, never both.
- Put it after the complete answer and make it the final content in the response.
- Do not place it in a code fence, quotation block, list, or writing block.
- Do not add commentary, alternatives, or explanatory text after it.
- For `NEXT_PROMPT`, make the prompt self-contained relative to the immediately preceding answer; advance the active goal rather than restating the request or asking for a generic review.
- For `NEXT_PROMPT`, prefer a decisive test, explicit contract, discriminating comparison, or evidence requirement over open-ended elaboration.
- For `NEXT_PROMPT`, introduce no new theory, facts, variables, or scope unless essential to test the selected unresolved issue, and never assume the current proposal is correct.
- For `CHAIN_COMPLETE`, state why remaining uncertainty or refinement is unlikely to materially change the active goal. Do not phrase the reason as another prompt or invitation.
- Do not continue solely because another boundary condition, methodological refinement, or possible test can be imagined. Possible next step ≠ valuable next step.

## Quality Test

Before emitting the terminal line, verify all seven conditions:

1. **Goal accuracy:** The active user goal is identified correctly