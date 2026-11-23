# tiny-chess-01 — 4 KB chess engine

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/Mrlfg911/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/Mrlfg911/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A 3,918-byte Python chess engine for the
[tiny-chess-01](https://make.fun/bounty/tiny-chess-01) bounty: the
strongest engine that fits in 4 KB.

## Result

- Practice gauntlet: 6 wins / 0 draws / 0 losses
- Elo 2112 (leaderboard ceiling)
- Entrypoint 3,918 bytes (limit 4,096)

## How it works

`main.py` is a packed entrypoint: an lzma-compressed sunfish-style
alpha-beta engine with piece-square tables, a transposition table,
null-move pruning, late-move reductions and quiescence search, plus a
driver that plays the env's games. The engine derives the side to move
from the start FEN rather than hardcoding it, and replays the full move
history from the canonical start position so repetition detection stays
correct whichever colour it plays. `makefun compress` produces `main.py`
from the readable source, which the bundle uploads beside the sessions.

## Run

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
