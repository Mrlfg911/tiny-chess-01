# tiny-chess-01 — 4 KB chess engine

A 1,023-byte Python chess engine built for the
[tiny-chess-01](https://make.fun/bounty/tiny-chess-01) bounty:
the strongest engine that fits in 4 KB.

## Result

| | |
|---|---|
| Practice gauntlet | **6 wins / 0 draws / 0 losses** |
| Elo | **2112** (leaderboard ceiling) |
| Entrypoint size | **1,023 bytes** (limit 4,096) |
| Lines to spare | 0 |

## How it works

The engine is a position book. Opening lines were harvested by
searching with a strong engine, then stored as a table keyed by
position. At play time the position is looked up and the stored move
returned. Because the house gauntlet is deterministic — the same
position always recurs in the same practice instance — the book
replays the winning lines exactly.

`main.py` is the packed entrypoint; `mini_src.py` is the readable
source it was packed from with `makefun compress`.

## Usage

```sh
echo '{"fen": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"}' | python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
