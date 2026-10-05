# advance-reasoning-chain

An ARC side quest. Use it for the step after an answer is already finished.

Finish the current request. Then add exactly one last line:

- `NEXT_PROMPT:` one follow-up that could change the active goal
- `CHAIN_COMPLETE:` another step is unlikely to change that goal

This repository is not [ARC-CEB-1.0](https://github.com/donaldtuttle/ARC-CEB-1.0) and not [ARC40D-CORE](https://github.com/donaldtuttle/ARC40D-CORE). It does not enumerate a fixed defect list, hash a controller run, or call a model. Those jobs stay in their own repos.

## What is this?

An instruction pack for choosing one useful follow-up after answering the
current request, or stopping when another step is unlikely to help.

## Why care?

An AI can keep suggesting refinements long after they stop changing your
decision. ARC makes the next step answer a practical question: what could
still change the result you care about?

## Try this

Load the [instruction pack](skills/advance-reasoning-chain/SKILL.md), then ask:
"Review this experiment plan. Answer the review first, then identify the one
unresolved issue most likely to change whether I should run it."

Inspect the final line: does it name a concrete next step, or explain why the
chain can stop? This is a usage example, not evidence of improved reasoning.


## Load this

The pack is [`skills/advance-reasoning-chain/SKILL.md`](skills/advance-reasoning-chain/SKILL.md). The folder name matches the YAML `name` field, `advance-reasoning-chain`.

| | |
|---|---|
| SHA-256 | `06ea1687b9c5f77e6bb3257ed23f6dda8ba2b05573b127619e3edba0952e70d0` |
| Bytes | 6426 |
| Trailing newline | no |

That hash identifies this file. The file is the reference.

## Reference

Use [`skills/advance-reasoning-chain/SKILL.md`](skills/advance-reasoning-chain/SKILL.md).

The workflow, the P / M / G scoring, and the output contract are in that file. One terminal line follows a finished answer: `NEXT_PROMPT` or `CHAIN_COMPLETE`. The Quality Test lists seven conditions, and all seven are in the file.

This copy replaces the earlier 6171-byte file. The replacement includes the earlier-section revisions, not only the restored Quality Test.

## License

[MIT](LICENSE).
