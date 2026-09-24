# advance-reasoning-chain

An ARC side quest. Use it for the step after an answer is already finished.

Finish the current request. Then add exactly one last line:

- `NEXT_PROMPT:` one follow-up that could change the active goal
- `CHAIN_COMPLETE:` another step is unlikely to change that goal

This repository is not [ARC-CEB-1.0](https://github.com/donaldtuttle/ARC-CEB-1.0) and not [ARC40D-CORE](https://github.com/donaldtuttle/ARC40D-CORE). It does not enumerate a fixed defect list, hash a controller run, or call a model. Those jobs stay in their own repos.

## Load this

The pack is [`skills/advance-reasoning-chain/SKILL.md`](skills/advance-reasoning-chain/SKILL.md). The folder name matches the YAML `name` field, `advance-reasoning-chain`.

| | |
|---|---|
| SHA-256 | `1394da52392cc9e8e60ac15dd4ee87bca5b81bc9f4b250f25159b2aa8e56666e` |
| Bytes | 6171 |
| Trailing newline | no |

That hash identifies this file. The file is the reference. Do not swap in a summary or a reconstructed quality test.

## Reference

Use [`skills/advance-reasoning-chain/SKILL.md`](skills/advance-reasoning-chain/SKILL.md).

The workflow, the P / M / G scoring, and the output contract are in that file. One terminal line follows a finished answer: `NEXT_PROMPT` or `CHAIN_COMPLETE`.

The Quality Test section in that same file stops during condition 1. The heading mentions seven conditions. Only the first is present. That is a limit of this reference, not a second document waiting somewhere else. The missing lines are not supplied here.

## License

[MIT](LICENSE).
