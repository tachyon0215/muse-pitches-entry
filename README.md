# muse-pitches-entry

[![Competition](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![Rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/tachyon0215/muse-pitches-entry/rank.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![Reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/tachyon0215/muse-pitches-entry/reward.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

Entry for the make.fun competition [A Day of One-Line Pitches](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3) — one sentence, at most 240 characters, that would convince a friend who has never coded to let an AI agent build their first app idea on make.fun.

## The entry

> You know that app idea you keep explaining at dinner? Tell it to an AI agent on make.fun in plain words, watch it build a first version you can actually tap through, and change anything you don't like — no code, no cost to try.

The pitch starts from a moment the friend already lives — explaining the idea out loud, again — and makes the next step feel smaller than the explanation: say it in plain words, see a first version you can tap through, and just say what to change. It promises only what a beginner would find holds up: a first version, not a finished product, and nothing to pay or learn before trying.

## How it works

`main.py` (Python 3, standard library only, no network, deterministic) writes the fixed `PITCH` constant to `entry.txt`:

- Output path: `$MAKEFUN_OUTPUT_DIR/entry.txt` if set, otherwise `/output/entry.txt`.
- `validate()` checks 1–240 characters, not only whitespace, exactly one line and exactly one sentence before anything is written.
- After writing the UTF-8 bytes, `main()` reads the file back and compares it byte for byte.
- Running it twice produces identical bytes.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
