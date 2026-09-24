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

That hash is the received file, not a claim that the skill is finished.

## The paste is cut off

The Quality Test says to check seven conditions. The file ends during condition 1:

> Goal accuracy: The active user goal is identified correctly

Conditions 2 through 7 were not in the source. They are not written here. Do not treat this copy as a complete quality test.

## License

[MIT](LICENSE).
