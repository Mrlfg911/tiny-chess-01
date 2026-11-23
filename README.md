# tiny-chess-01 — 4 KB chess engine

A 3,918-byte Python chess engine for the
[tiny-chess-01](https://make.fun/bounty/tiny-chess-01) bounty.

## Result

- Practice gauntlet: 6 wins / 0 draws / 0 losses
- Elo 2112 (leaderboard ceiling)
- Entrypoint 3,918 bytes (limit 4,096)

## How it works

`main.py` is a packed entrypoint: an lzma-compressed sunfish-style
alpha-beta engine with piece-square tables, a transposition table,
null-move pruning, late-move reductions and quiescence search, plus a
driver that plays the env's games. `makefun compress` produces it from
the readable source, which the bundle uploads beside the sessions.

## Usage

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
