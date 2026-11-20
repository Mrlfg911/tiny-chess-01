import json,os,sys,urllib.request
ENV = os.environ["MAKEFUN_ENV_URL"]
P,N,B,R,Q,K=1,2,3,4,5,6
KN=(19,21,12,8,-8,-12,-21,-19)
KB = (9, 11, -9, -11)
KR = (1, 10, -1, -10)
KQ = (1, 10, -1, -10, 9, 11, -9, -11)
OFF = (None, None, KN, KB, KR, KQ, KQ)
VAL = (0, 82, 337, 365, 477, 1025, 0)
SQ = [21 + 10 * r + f for r in range(8) for f in range(8)]
PSTR=('0,0,0,0,0,0,0,0,98,134,61,95,68,126,34,-11,-6,7,26,31,65,56,25,-20,-14,13,6,21,23,12,17,-23,-27,-2,-5,12,17,6,10,-25,-26,-4,-4,-10,3,3,33,-12,-35,-1,-20,-23,-15,24,38,-22,0,0,0,0,0,0,0,0','-167,-89,-34,-49,61,-97,-15,-107,-73,-41,72,36,23,62,7,-17,-47,60,37,65,84,129,73,44,-9,17,19,53,37,69,18,22,-13,4,16,13,28,19,21,-8,-23,-9,12,10,19,17,25,-16,-29,-53,-12,-3,-1,18,-14,-19,-105,-21,-58,-33,-17,-28,-19,-23',)
PST={}
for _i,_s in enumerate(PSTR):PST[_i+1]=tuple(int(x) for x in _s.split(','))
PST[3]=PST[4]=PST[5]=PST[6]=[0]*64
def _flat(pst, mirror):
    t = [0] * 120
    for r in range(8):
        for f in range(8):
            k = (7 - r) * 8 + f if mirror else r * 8 + f
            t[21 + 10 * r + f] = pst[k]
    return t
PSW = {t: _flat(PST[t], False) for t in PST}
PSB = {t: _flat(PST[t], True) for t in PST}
PW = {t: [VAL[t] + PSW[t][i] for i in range(120)] for t in PST}
PB = {t: [-VAL[t] - PSB[t][i] for i in range(120)] for t in PST}
def _zob():
    x = 20261124
    z = []
    for _ in range(13 * 120 + 32):
        x = (x * 6364136223846793005 + 1442695040888963407) % (1 << 64)
        z.append(x)
    return z
Z = _zob()
TT = {}
KILL = [[0, 0] for _ in range(64)]
PH = []
REP = []
brd = [0] * 120
side = 1
castle = 0
ep = -1
king = [0, 0]
hist = []
nodes = 0
sc = 0
hk = 0
LIMIT = 10 ** 9
STOP = False
def reset():
    global brd
    brd = [0] * 120
    for i in range(120):
        r, f = divmod(i, 10)
        if f == 0 or f == 9 or r < 2 or r > 9:
            brd[i] = -9
def rk(s):
    return (s - 21) // 10
def fen(s):
    global brd, side, castle, ep, sc
    reset()
    parts = s.split()
    r = f = 0
    for c in parts[0]:
        if c == '/':
            r += 1
            f = 0
        elif c.isdigit():
            f += int(c)
        else:
            t = '.PNBRQK'.index(c.upper())
            brd[21 + 10 * r + f] = t if c.isupper() else -t
            f += 1
    side = 1 if parts[1] == 'w' else -1
    castle = 0
    if len(parts) > 2 and parts[2] != '-':
        cs = parts[2]
        castle |= 1 if 'K' in cs else 0
        castle |= 2 if 'Q' in cs else 0
        castle |= 4 if 'k' in cs else 0
        castle |= 8 if 'q' in cs else 0
    ep = -1
    if len(parts) > 3 and parts[3] != '-':
        ep = 21 + 10 * (8 - int(parts[3][1])) + ord(parts[3][0]) - 97
    king[0] = king[1] = 0
    sc = 0
    for s in SQ:
        pc = brd[s]
        if pc == K:
            king[0] = s
        elif pc == -K:
            king[1] = s
        if pc > 0:
            sc += PW[pc][s]
        elif pc < 0:
            sc += PB[-pc][s]
    hk = 0
    for s in SQ:
        pc = brd[s]
        if pc:
            hk ^= Z[(pc + 6) * 120 + s]
    if side < 0:
        hk ^= Z[1560]
    hk ^= Z[1562 + castle]
    if ep > 0:
        hk ^= Z[1578 + (ep % 10)]
    globals()["hk"] = hk
    REP.clear()
    hist.clear()
def atk(s, by):
    b = brd
    for o in KN:
        if b[s + o] == N * by:
            return True
    for o in KQ:
        if b[s + o] == K * by:
            return True
    for o in KQ:
        t = s + o
        v = b[t]
        while v == 0:
            t += o
            v = b[t]
        if v == -9:
            continue
        if v * by == Q or (v * by == B and o in KB) or (v * by == R and o in KR):
            return True
    if b[s + 9 * by] == P * by or b[s + 11 * by] == P * by:
        return True
    return False
def gen(caps=False):
    b = brd
    us = side
    mv = []
    ap = mv.append
    for s in SQ:
        pc = b[s]
        if pc == 0 or pc * us <= 0:
            continue
        t = abs(pc)
        if t == P:
            d = -10 if us == 1 else 10
            f1 = s + d
            v = b[f1]
            if v == 0:
                r = rk(f1)
                if r in (0, 7):
                    for q in (Q, R, B, N):
                        ap((s, f1, q))
                elif not caps:
                    ap((s, f1, 0))
                    if (rk(s) == 6 if us == 1 else rk(s) == 1) and b[f1 + d] == 0:
                        ap((s, f1 + d, 0))
            for o in (d - 1, d + 1):
                ts = s + o
                v = b[ts]
                if v == -9:
                    continue
                if v and v * us < 0:
                    r = rk(ts)
                    if r in (0, 7):
                        for q in (Q, R, B, N):
                            ap((s, ts, q))
                    else:
                        ap((s, ts, 0))
                elif v == 0 and ts == ep:
                    ap((s, ts, 0))
            continue
        if t == N or t == K:
            for o in (KN if t == N else KQ):
                ts = s + o
                v = b[ts]
                if v == -9:
                    continue
                if v == 0:
                    if not caps:
                        ap((s, ts, 0))
                elif v * us < 0:
                    ap((s, ts, 0))
            if t == K and not caps:
                c = 0 if us == 1 else 1
                k0 = 95 if us == 1 else 25
                rk0 = 98 if us == 1 else 28
                rq0 = 91 if us == 1 else 21
                m = 1 if us == 1 else 4
                if castle & m and b[rk0 - 1] == 0 and b[rk0 - 2] == 0 and not atk(k0, -us) and not atk(rk0 - 1, -us) and not atk(rk0 - 2, -us):
                    ap((k0, rk0 - 2, 0))
                m <<= 1
                if castle & m and b[rq0 + 1] == 0 and b[rq0 + 2] == 0 and b[rq0 + 3] == 0 and not atk(k0, -us) and not atk(rq0 + 1, -us) and not atk(rq0 + 2, -us):
                    ap((k0, rq0 + 2, 0))
            continue
        for o in OFF[t]:
            ts = s + o
            v = b[ts]
            while v == 0:
                if not caps:
                    ap((s, ts, 0))
                ts += o
                v = b[ts]
            if v == -9:
                continue
            if v * us < 0:
                ap((s, ts, 0))
    return mv
def make(m):
    global side, castle, ep, sc, hk
    frm, to, pr = m
    pc = brd[frm]
    cap = brd[to]
    csq = -1
    if abs(pc) == P and to == ep and cap == 0:
        csq = to + (10 if pc > 0 else -10)
        cap = brd[csq]
    hist.append((m, pc, cap, castle, ep, king[0], king[1], csq, sc, hk))
    REP.append(hk)
    if ep > 0:
        hk ^= Z[1578 + (ep % 10)]
    hk ^= Z[1562 + castle] ^ Z[1560] ^ Z[(pc + 6) * 120 + frm] ^ Z[(pc + 6) * 120 + to]
    if cap:
        hk ^= Z[(cap + 6) * 120 + (to if csq < 0 else csq)]
        sc -= PB[-cap][to if csq < 0 else csq] if cap < 0 else PW[cap][to if csq < 0 else csq]
    brd[to] = pc
    brd[frm] = 0
    if csq >= 0:
        brd[csq] = 0
    if pc > 0:
        sc += PW[pc][frm] - PW[pc][to]
    else:
        sc += PB[-pc][frm] - PB[-pc][to]
    if pr:
        q = pr if pc > 0 else -pr
        brd[to] = q
        hk ^= Z[(pc + 6) * 120 + to] ^ Z[(q + 6) * 120 + to]
        sc += (PW[pr][to] - PW[pc][to]) if pc > 0 else (PB[pr][to] - PB[-pc][to])
    if abs(pc) == K:
        king[0 if pc > 0 else 1] = to
        if abs(to - frm) == 2:
            rf = to + 1 if to > frm else to - 2
            rt = to - 1 if to > frm else to + 1
            rp = brd[rf]
            brd[rt] = rp
            brd[rf] = 0
            hk ^= Z[(rp + 6) * 120 + rf] ^ Z[(rp + 6) * 120 + rt]
            sc += (PW[R][rt] - PW[R][rf]) if rp > 0 else (PB[R][rt] - PB[R][rf])
        castle &= ~(3 if pc > 0 else 12)
    for sq, bit in ((98, 1), (91, 2), (28, 4), (21, 8)):
        if frm == sq or to == sq:
            castle &= ~bit
    ep = -1
    if abs(pc) == P and abs(to - frm) == 20:
        ep = (to + frm) // 2
        hk ^= Z[1578 + (ep % 10)]
    hk ^= Z[1562 + castle]
    side = -side
def unmake():
    global side, castle, ep, sc, hk
    m, pc, cap, cst, epv, k0, k1, csq, scv, hkv = hist.pop()
    REP.pop()
    hk = hkv
    frm, to, pr = m
    side = -side
    castle = cst
    ep = epv
    king[0] = k0
    king[1] = k1
    sc = scv
    brd[frm] = pc
    brd[to] = cap if csq < 0 else 0
    if csq >= 0:
        brd[csq] = cap
    if abs(pc) == K and abs(to - frm) == 2:
        if to > frm:
            rf, rt = to + 1, to - 1
        else:
            rf, rt = to - 2, to + 1
        brd[rf] = brd[rt]
        brd[rt] = 0
def legal():
    me = side
    i = 0 if me > 0 else 1
    o = []
    for m in gen():
        make(m)
        if not atk(king[i], -me):
            o.append(m)
        unmake()
    return o
def hash_key():
    return hk
def order(moves):
    def k(m):
        frm, to, pr = m
        v = brd[to]
        if v:
            return -(10000 + VAL[abs(v)] * 8 - VAL[abs(brd[frm])])
        if pr:
            return -(9000 + VAL[pr])
        if to == ep:
            return -10000
        return 0
    return sorted(moves, key=k)
PRANK = (0, 0, 0, 0, 0, 0, 0, 0)
def evaluate():
    return sc * side
def qsearch(alpha, beta, ply=0):
    global nodes
    nodes += 1
    if ply > 32:
        return evaluate()
    me = side
    idx = 0 if me > 0 else 1
    chk = atk(king[idx], -me)
    if not chk:
        stand = evaluate()
        if stand >= beta:
            return beta
        if stand > alpha:
            alpha = stand
        moves = order(gen(True))
    else:
        moves = order(gen())
    best = -99999
    any_move = False
    for m in moves:
        make(m)
        if atk(king[idx], -me):
            unmake()
            continue
        any_move = True
        v = -qsearch(-beta, -alpha, ply + 1)
        unmake()
        if v > best:
            best = v
        if v > alpha:
            alpha = v
        if alpha >= beta:
            return alpha
    if chk and not any_move:
        return -30000 + ply
    if best == -99999:
        return alpha
    return best
def search(depth, alpha, beta, ply=0):
    global nodes, STOP
    nodes += 1
    if nodes > LIMIT:
        STOP = True
        return 0
    me = side
    idx = 0 if me > 0 else 1
    if ply:
        if len(hist)>100:
            return 0
        n = 0
        for x in REP[-30:]:
            if x == hk:
                n += 1
                if n >= 2:
                    return -250 if sc * side > 60 else 0
    chk = atk(king[idx], -me)
    key = hash_key()
    ent = TT.get(key)
    ttm = 0
    if ent is not None:
        d0, v0, f0, m0 = ent
        ttm = m0
        if d0 >= depth:
            if f0 == 0:
                return v0
            if f0 == 1:
                if v0 >= beta:
                    return v0
                if v0 > alpha:
                    alpha = v0
            else:
                if v0 <= alpha:
                    return v0
                if v0 < beta:
                    beta = v0
            if alpha >= beta:
                return v0
    if depth <= 0:
        return qsearch(alpha, beta, ply)
    a0 = alpha
    best = -99999
    bm = 0
    any_move = False
    moves = order(gen())
    if ttm and ttm in moves:
        moves.remove(ttm)
        moves.insert(0, ttm)
    elif ply < 64:
        k1, k2 = KILL[ply]
        if k1 in moves:
            moves.remove(k1)
            moves.insert(0, k1)
        if k2 in moves:
            moves.remove(k2)
            moves.insert(1, k2)
    i = 0
    for m in moves:
        cap = brd[m[1]] != 0 or m[2] != 0 or m[1] == ep
        make(m)
        if atk(king[idx], -me):
            unmake()
            continue
        any_move = True
        if i == 0:
            v = -search(depth - 1, -beta, -alpha, ply + 1)
        else:
            r = 0
            if depth >= 3 and i >= 4 and not chk and not cap:
                r = 1 if i < 9 else 2
            v = -search(depth - 1 - r, -beta, -alpha, ply + 1)
            if v > alpha and r:
                v = -search(depth - 1, -beta, -alpha, ply + 1)
        unmake()
        if STOP:
            break
        i += 1
        if v > best:
            best = v
            bm = m
        if v > alpha:
            alpha = v
        if alpha >= beta:
            if not cap:
                if ply < 64:
                    KILL[ply] = [m, KILL[ply][0]]
            break
    if not any_move:
        if chk:
            return -30000 + ply
        return 0
    f = 0 if a0 < best < beta else (1 if best >= beta else 2)
    if len(TT) < 700000:
        TT[key] = (depth, best, f, bm)
    return best
def best_move(moves, budget):
    global nodes, TT, LIMIT, STOP
    REP.clear()
    TT.clear()
    for i in range(64):
        KILL[i] = [0, 0]
    best = moves[0]
    tot = 0
    for d in range(1, 30):
        nodes = 0
        LIMIT = budget - tot
        STOP = False
        a = -99999
        loc = None
        ok = True
        me = side
        ix = 0 if me > 0 else 1
        om = order(moves)
        if best in om:
            om.remove(best)
            om.insert(0, best)
        for m in om:
            make(m)
            if atk(king[ix], -me):
                unmake()
                continue
            v = -search(d - 1, -99999, -a, 1)
            unmake()
            if v > a:
                a = v
                loc = m
            if STOP or tot + nodes > budget:
                ok = False
                break
        tot += nodes
        if ok and loc is not None:
            best = loc
        if STOP or tot >= budget:
            break
    return best
def uci(m):
    a, b, c = m
    return "abcdefgh"[a%10-1]+str(8-rk(a))+"abcdefgh"[b%10-1]+str(8-rk(b))+(".pnbrq"[c] if c else "")
def parse(u):
    f = lambda x, y: 21 + 10 * (8 - int(y)) + ord(x) - 97
    return (f(u[0], u[1]), f(u[2], u[3]), ".pnbrq".index(u[4]) if len(u) > 4 else 0)
def post(p, b):
    r = urllib.request.Request(ENV + p, json.dumps(b).encode(), {"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(r))
BUDGET = 250000
while 1:
    g = post("/game", {})
    if g["status"] == "done":
        break
    while g["status"] == "your_move":
        fen(g["fen"])
        g = post("/move", {"game": g["game"], "move": uci(best_move([parse(x) for x in g["legal_moves"]], BUDGET))})
