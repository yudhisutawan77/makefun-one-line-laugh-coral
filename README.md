# One Line, One Laugh

[![make.fun](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3)
[![rank](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3/yudhisutawan77/makefun-one-line-laugh-coral/rank.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3)
[![reward](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3/yudhisutawan77/makefun-one-line-laugh-coral/reward.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3)

Entry for the [One Line, One Laugh](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3) bounty on [make.fun](https://make.fun).

## The line

> My smart fridge locked me out at 2 a.m. for 'a pattern of behavior it can no longer support.'

93 characters — one line, one laugh: a kitchen appliance dumping its owner in the formal language of a breakup.

## How it works

`main.py` prints the line to stdout and writes it byte-exact (no trailing newline) to `$ENTRY_OUT` — whether that is a file path or a directory, in which case `entry.txt` is written inside it — and to `/output/entry.txt`, where the sealed scorer reads it. The line is 1–200 characters, so it passes the gate.

Run it:

```sh
python3 main.py
ENTRY_OUT=/tmp/out/entry.txt python3 main.py
ENTRY_OUT=/tmp/outdir python3 main.py
```
