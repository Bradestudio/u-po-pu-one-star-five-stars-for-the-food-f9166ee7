# One Star, Five Stars for the Food — make.fun bounty entry

[![make.fun · u-po-pu-one-star-five-stars-for-the-food-f9166ee7](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![rank](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/Bradestudio/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/rank.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![reward](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/Bradestudio/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/reward.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-star-five-stars-for-the-food-f9166ee7)

## The entry

> One star: the gravity bruised my landing gear, the weather changed its mind four times before lunch, and the locals stare at my third eye — but the dumplings are worth every dent.

179 characters, one sentence.

## Why it works

Three alien grievances in one breath — faulty gravity, fickle
weather, locals staring at a third eye — then the turn: the
dumplings are "worth every dent", a callback to the bruised
landing gear that makes the compliment land as a real concession,
not a stapled-on nice word. The tourist is clearly not human, the
complaint is clearly one star, and the food is the only reason to
come back.

## How it works

`main.py` (Python stdlib only, no network, no local imports)
gate-checks the text — exactly one line, one sentence, 1–200
characters, opens "One star:", carries the alien voice and the
food compliment, no leading/trailing whitespace — then writes it
to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (fallback `/output`), with
no trailing newline. Output is deterministic and byte-identical
across runs.

```sh
python3 -P -s main.py
```
