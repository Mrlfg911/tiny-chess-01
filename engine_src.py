s='pnbrqk'
r=Exception
q=tuple
k='B'
j='N'
i=int
h=ord
g=max
f=next
a='Q'
Z=len
Y=sum
S=False
R=enumerate
Q=range
O='R'
M='.'
L=abs
K='P'
H=None
G='K'
F=True
import json as l,os,sys,urllib.request,os,time
from itertools import count
from collections import namedtuple as b
__version__='2026-packed'
A9='sunfish '+__version__
m={K:100,j:280,k:320,O:479,a:929,G:60000}
D={K:(0,0,0,0,0,0,0,0,78,83,86,73,102,82,85,90,7,29,21,44,40,31,44,7,-17,16,-2,15,14,0,15,-13,-26,3,10,9,6,1,0,-23,-22,9,5,-11,-10,-2,3,-19,-31,8,-7,-37,-36,-14,3,-31,0,0,0,0,0,0,0,0),j:(-66,-53,-75,-75,-10,-55,-58,-70,-3,-6,100,-36,4,62,-4,-14,10,67,1,74,73,27,62,-2,24,24,45,37,33,41,25,17,-1,5,31,21,22,35,2,0,-18,10,13,22,18,15,11,-14,-23,-15,2,0,2,0,-23,-20,-74,-23,-26,-24,-19,-35,-22,-69),k:(-59,-78,-82,-76,-23,-107,-37,-50,-11,20,35,-42,-39,31,2,-22,-9,39,-32,41,52,-10,28,-14,25,17,20,34,26,25,15,10,13,10,17,23,17,16,0,7,14,25,24,15,8,25,20,15,19,20,11,6,7,6,20,16,-7,2,-15,-12,-14,-15,-10,-10),O:(35,29,33,4,37,33,56,50,55,29,56,67,55,62,34,60,19,35,28,33,45,27,25,15,0,5,16,13,18,-4,-9,-6,-28,-35,-16,-21,-13,-29,-46,-30,-42,-28,-42,-25,-25,-35,-26,-46,-53,-38,-31,-26,-29,-43,-44,-53,-30,-24,-18,5,-2,-18,-31,-32),a:(6,1,-8,-104,69,24,88,26,14,32,60,-10,20,76,57,24,-2,43,32,60,72,63,43,2,1,-16,22,17,25,20,-13,-6,-14,-15,-2,-5,-1,-10,-20,-22,-30,-6,-13,-11,-16,-11,-16,-27,-36,-18,0,-19,-15,-15,-21,-38,-39,-30,-31,-13,-31,-36,-34,-42),G:(4,54,47,-99,-99,60,83,-62,-32,10,55,56,56,55,10,3,-62,12,-57,44,-67,28,37,-31,-55,50,11,-4,-19,13,0,-49,-55,-43,-52,-28,-51,-47,-8,-50,-47,-42,-43,-79,-64,-32,-29,-32,-4,3,-14,-50,-57,-18,13,4,17,30,-3,-14,6,-1,40,18)}
for(T,t)in D.items():u=lambda row:(0,)+q(A+m[T]for A in row)+(0,);D[T]=Y((u(t[A*8:A*8+8])for A in Q(8)),());D[T]=(0,)*20+D[T]+(0,)*20
v,w=D[G],q(m[G]+70-10*(L(2*(A//10)-11)+L(2*(A%10)-9))for A in Q(120))
N=47923
I=69290
J,U,V,W=91,98,21,28
AA='         \n         \n rnbqkbnr\n pppppppp\n ........\n ........\n ........\n ........\n PPPPPPPP\n RNBQKBNR\n         \n         \n'
A,B,E,C=-10,1,10,-1
x={K:(A,A+A,A+C,A+B),j:(A+A+B,B+A+B,B+E+B,E+E+B,E+E+C,C+E+C,C+A+C,A+A+C),k:(A+B,E+B,E+C,A+C),O:(A,B,E,C),a:(A,B,E,C,A+B,E+B,E+C,A+C),G:(A,B,E,C,A+B,E+B,E+C,A+C)}
y=40
z=140
A0=15
A1=40
n=60
o=10**6
P=b('Move','i j prom')
class c(b('Position','board score wc bc ep kp')):
	def __hash__(A):return hash((A.board,A.wc,A.bc,A.ep,A.kp))
	def __eq__(A,o):return A.board==o.board and A.ep==o.ep and A.kp==o.kp and A.wc==o.wc and A.bc==o.bc
	def __ne__(A,o):return not A.__eq__(o)
	def gen_moves(D):
		for(F,I)in R(D.board):
			if I not in'PNBRQK':continue
			for H in x[I]:
				for E in count(F+H,H):
					L=D.board[E]
					if L in' \nPNBRQK':break
					if I==K:
						if H in(A,A+A)and L!=M:break
						if H==A+A and(F<J+A or D.board[F+A]!=M):break
						if H in(A+C,A+B)and L==M and E not in(D.ep,D.kp,D.kp-1,D.kp+1):break
						if V<=E<=W:
							for N in'NBRQ':yield P(F,E,N)
							break
					yield P(F,E,'')
					if I in'PNK'or L in s:break
					if F==J and D.board[E+B]==G and D.wc[0]:yield P(E+B,E+C,'')
					if F==U and D.board[E+C]==G and D.wc[1]:yield P(E+C,E+B,'')
	def rotate(A,nullmove=S):B=nullmove;return c(A.board[::-1].swapcase(),-A.score,A.bc,A.wc,119-A.ep if A.ep and not B else 0,119-A.kp if A.kp and not B else 0)
	def move(F,move):
		D,C,T=move;R,Z=F.board[D],F.board[C];H=lambda board,i,p:board[:i]+p+board[i+1:];B=F.board;I,N,Q,P=F.wc,F.bc,0,0;X=F.score+F.value(move);B=H(B,C,B[D]);B=H(B,D,M);I=I[0]and D!=J,I[1]and D!=U;N=N[0]and C!=W,N[1]and C!=V
		if R==G:
			I=S,S
			if L(C-D)==2:P=(D+C)//2;Y=J if C<D else U;B=H(B,Y,M);B=H(B,P,O)
		if R==K:
			if V<=C<=W:B=H(B,C,T)
			if C-D==2*A:Q=D+A
			if C==F.ep:B=H(B,C+E,M)
		return c(B[::-1].swapcase(),-X,N,I,119-Q if Q else 0,119-P if P else 0)
	def value(F,move):
		C,A,M=move;H,I=F.board[C],F.board[A];B=D[H][A]-D[H][C]
		if I in s:B+=D[I.upper()][119-A]
		if L(A-F.kp)<2:B+=D[G][119-A]
		if H==G and L(C-A)==2:B+=D[O][(C+A)//2];B-=D[O][J if A<C else U]
		if H==K:
			if V<=A<=W:B+=D[M][A]-D[K][A]
			if A==F.ep:B+=D[K][119-(A+E)]
		return B
	def king_capture(A):return f((B for B in A.gen_moves()if A.board[B.j]=='k'or L(B.j-A.kp)<2),H)
class A2(r):0
p=[1<<62]
d=b('Entry','lower upper')
class A3:
	def __init__(A):A.tp_score,A.tp_move,A.history={},{},set();A.nodes,A.deadline=0,1<<63
	def bound(B,pos,gamma,depth,root=S):
		M=root;D=gamma;C=depth;A=pos;B.nodes+=1
		if B.nodes>p[0]:raise A2
		C=g(C,0)
		if A.score<=-N:return-I
		if not M:
			G=B.tp_score.get((A,C),d(-I,I))
			if G.lower>=D:return G.lower
			if G.upper<D:return G.upper
			if C>0 and A in B.history:return 0
		def P():
			G=B.tp_move.get(A)
			if not M and C>2 and L(A.score)<500 and any(B in A.board for B in'RBNQ'):
				E=-B.bound(A.rotate(nullmove=F),1-D,C-3);O=E>=D and(B.tp_move.get(A)or A.king_capture())
				if O and A.value(O)>=N:yield(O,I)
				elif E<D or B.bound(A.rotate(nullmove=F),1-N,C-3)>=1-N:yield(H,E)
			if C==0:yield(H,A.score)
			if not G and C>2:B.bound(A,D,C-3,root=F);G=B.tp_move.get(A)
			P=y-C*z
			if G and A.value(G)>=P:yield(G,-B.bound(A.move(G),1-D,C-1))
			for(S,(J,K))in R(sorted(((T,B)for B in A.gen_moves()if(T:=A.value(B))>=P),reverse=F)):
				if C<=1 and A.score+J<D:yield(K,I)if J>=N else(H,A.score+J);break
				Q=n and C>2 and S>2 and J<n;E=-B.bound(A.move(K),1-D,C-2 if Q else C-1)
				if Q and E>=D:E=-B.bound(A.move(K),1-D,C-1)
				yield(K,E)
		E,K=-I,S
		for(J,O)in P():
			E=g(E,O);K|=J is not H and O>-I
			if E>=D:
				if J is not H and C:
					B.tp_move[A]=J
					if Z(B.tp_move)>o:del B.tp_move[f(A for A in B.tp_move if A!=B.root)]
				break
		if C and not K and all(A.move(B).king_capture()for B in A.gen_moves()):E=-N if A.rotate(nullmove=F).king_capture()else 0
		if not M:B.tp_score[A,C]=d(E,G.upper)if E>=D else d(G.lower,E)
		if Z(B.tp_score)>o:del B.tp_score[f(iter(B.tp_score))]
		return E
	def search(A,history):
		K=history;A.nodes,A.history=0,set(K);A.tp_score.clear();E=A.root=K[-1];N=Y(A.isupper()for A in E.board)==1 or Y(A.islower()for A in E.board)==1;D[G]=w if N else v;H=0
		for L in Q(1,1000):
			B,C,M=1-I,I,0
			while B<C-A0:
				J=A.bound(E,H,L,root=F)
				if J>=H:B=g(B,J)
				else:C=min(C,J)
				M+=1;yield(L,H,J,A.tp_move.get(E))
				if B>C or M>A1:break
				H=(B+C+1)//2
def e(c):return J+h(c[0])-h('a')-10*(i(c[1])-1)
def X(i):return chr((i-J)%10+h('a'))+str(1-(i-J)//10)
def A4(board,wc=(F,F),bc=(F,F),ep=0,kp=0,pf=0):A=board;B=Y(D[A][B]if A.isupper()else-D[A.upper()][119-B]for(B,A)in R(A)if A.isalpha());return c(A,B,wc,bc,ep,kp)
def A5(fen):
	A=fen.split();B=[' ']*120
	for C in Q(2,10):
		B[C*10]=' '
		for D in Q(8):B[C*10+1+D]=M
		B[C*10+9]='\n'
	for(C,H)in R(A[0].split('/')):
		D=0
		for E in H:
			if E.isdigit():D+=i(E)
			else:B[(C+2)*10+1+D]=E;D+=1
	I=G in A[2],a in A[2];J='k'in A[2],'q'in A[2];K=0 if Z(A)<4 or A[3]=='-'else e(A[3]);F=A4(''.join(B),I,J,K);return F.rotate()if A[1]=='b'else F
def A6(moves,start_fen):
	F=start_fen;E=moves;H=F.split()[1]=='w';I='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'if E else F;A=A5(I);G=[A]
	for(J,B)in R(E):
		K=(J%2==0)!=H;C,D=e(B[:2]),e(B[2:4])
		if K:C,D=119-C,119-D
		A=A.move(P(C,D,B[4:].upper()));G.append(A)
	return G
def A7(h,s,cap):
	p[0]=cap;A,B=H,1
	try:
		for(C,F,G,D)in s.search(h):
			if C>B and D is not H:A,B=D,C
	except r:0
	if A is H:E=list(h[-1].gen_moves());A=E[0]if E else H
	return A
def A8():
	O='start_fen';K='moves';I='game';G='legal_moves';P=os.environ['MAKEFUN_ENV_URL'].rstrip('/');Q=i(os.environ.get('TC_NODES','50000'))
	def L(path,body):
		A=l.dumps(body).encode();B=urllib.request.Request(P+path,data=A,headers={'content-type':'application/json'})
		with urllib.request.urlopen(B,timeout=30)as C:return l.load(C)
	while F:
		A=L('/game',{})
		if K not in A:break
		J=A3();J.tp_score,J.tp_move={},{}
		while F:
			R=A6(A[K],A[O]);B=A7(R,J,Q)
			if B is H:E=A[G][0]
			else:
				S=A[O].split()[1]=='w';M=(Z(A[K])%2==0)!=S;C,D=B.i,B.j
				if M:C,D=119-C,119-D
				E=X(C)+X(D)+B.prom.lower()
				if E not in A[G]:T,U=(119-C,119-D)if not M else(C,D);N=X(T)+X(U)+B.prom.lower();E=N if N in A[G]else A[G][0]
			A=L('/move',{I:A[I],'move':E})
			if A.get('status')=='over':print(I,A[I],A.get('outcome'),A.get('reason'),flush=F);break
A8()