import zipfile as B,os as A,shutil as F,string as C,random as D,base64 as E
def G(folder_path,output_path):
	C=folder_path
	with B.ZipFile(output_path,'w',B.ZIP_DEFLATED)as F:
		for(D,H,G)in A.walk(C):
			for E in G:F.write(A.path.join(D,E),A.path.relpath(A.path.join(D,E),C))
def H(source_folder,destination_folder):
	C=source_folder;B=destination_folder
	if not A.path.exists(B):A.makedirs(B)
	G=A.listdir(C)
	for D in G:
		E=A.path.join(C,D);H=A.path.join(B,D)
		if A.path.isfile(E):
			try:F.copy2(E,H)
			except:continue
def I(length):A=C.ascii_letters+C.digits;B=''.join(D.choice(A)for B in range(length));return B
def J(array_2d):
	A=[]
	for B in array_2d:
		for C in B:A.append(C)
	return A
def K(str):
	if str==None:return
	return E.b64decode(str[::-1]).decode('utf-8')