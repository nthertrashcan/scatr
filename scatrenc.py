
import os
from cryptography.fernet import Fernet
import hashlib
from sys import exit

emb="xasdx"
start="adding200suc07@1999"
end="complete200suc07@1999"
gaps="guessit01071999"
gape="guessit07071999"
default=""
fno=1




def scattenc(name,path,kv,rflag,delflg):
	global fno
	if not os.path.isfile(name):
		print("\n[INFO] File not found!!!")
		exit(0)
	if kv!="":
		kv = hashlib.sha256(kv.encode()) 
		kv=kv.hexdigest() 
	key = Fernet.generate_key()
	cipher_suite = Fernet(key)
	sflag=0
	dest=""
	if path=="":
		dest=input("\n[INPUT] Enter Destination - :")
		if dest=="":
			dest=default
		else:
			if ":" not in dest:
				dest=os.path.join(os.getcwd(),dest)
				dest=dest.lower()
	else:
		dest=path
		if ":" not in dest:
			dest=os.path.join(os.getcwd(),dest)
			dest=dest.lower()
	name=name.strip()
	name=name.lower()
	pname=""

	try:
		indx=[n for n,x in enumerate(name) if x=="\\"][::-1][0]
	except:
		name=os.path.join(os.getcwd(),name)
		indx=[n for n,x in enumerate(name) if x=="\\"][::-1][0]
	pname=name[:indx]
	name=name[indx+1:]
	file=open(os.path.join(pname,name),"rb")
	siz=len(file.readlines())
	file=open(os.path.join(pname,name),"rb")
	dflag=1
	frag=[]
	for i in file.readlines():
		frag.append(i)
	n=0
	m=0
	if os.path.isdir(dest):
		f=[]
		for r,d,fi in os.walk(dest):
			for i in fi:
				f.append(os.path.join(r,i))
		if len(f)==0:
			if len(frag)>9:
				print("\n[INFO] Empty folder!!!, Creating dummy files")
				for i in range(0,10):
					fl=open(f"{dest}/{i}","wb")

				for r,d,fi in os.walk(dest):
					for i in fi:
						f.append(os.path.join(r,i))
			else:
				print("\n[INFO] File size too small")
				exit(0)
		if len(f)>0:
			flag=0
			if len(frag)<len(f):
				file=open(os.path.join(r,f[0]),"rb")
				flag=1
				
				for i in file.readlines():
					if bytes(emb,"utf-8") in i:
						if str(kv)!="":
							key=str(i).split(emb)[1].split(str(kv))[1].encode()
						else:
							key=str(i).split(emb)[1].encode()
						cipher_suite = Fernet(key)
						decoded_text = cipher_suite.decrypt(str(i).split(emb)[2][:len(str(i).split(emb)[2])-3].encode())
						if bytes(name+start,"utf-8") in decoded_text:
							flag=0
							print("\n[INFO] {} already exist!!!".format(name))
							break
				if flag==1:
					print("\n[INFO] Scattering...")
					file=open(f[0],"ab")
					encoded_text = cipher_suite.encrypt(bytes(name+start,"utf-8"))
					file.write(b"\n"+bytes(emb,"utf-8")+bytes(kv,"utf-8")+key+bytes(emb,"utf-8")+encoded_text+b"\n")
					for j in frag:
						encoded_text = cipher_suite.encrypt(j)
						file.write(b"\n"+encoded_text+b"\n")
					encoded_text=cipher_suite.encrypt(bytes(name+end,"utf-8"))
					file.write(b"\n"+bytes(emb,"utf-8")+bytes(kv,"utf-8")+key+bytes(emb,"utf-8")+encoded_text+b"\n")
				f=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"encfiles"),"ab")
				f.write(bytes(os.getcwd().lower()+"\\"+name+" -d "+dest+"\n","utf-8"))
				print("\n[INFO] Completed")
				if delflg:
					q=input("\n[INPUT] Do you want to delete - {} : ".format(name))
					q=q.lower()
					if q=="y" or q=="yes":
						os.remove("{}".format(os.path.join(pname,name)))
				flag=0	
			else:
				showf=0
				nl=len(frag)
				nl=int(nl/len(f))
				flag=1
				eflag=0
				for l,i in enumerate(f):
					file=open(i,"rb")
					for j in file.readlines():
						try:
							if bytes(emb,"utf-8") in j:
								if str(kv)!="":
									key=str(j).split(emb)[1].split(str(kv))[1].encode()
								else:
									key=str(j).split(emb)[1].encode()
								cipher_suite = Fernet(key)
								decoded_text = cipher_suite.decrypt(str(j).split(emb)[2][:len(str(j).split(emb)[2])-3].encode())
								if bytes(name+start,"utf-8") in decoded_text:
									flag=0
									break
						except:
							flag=0
					if flag==1:
						if showf==0:
							if rflag==1:
								print("\n[{}] - {}".format(fno,name))
								fno+=1
							else:
								print("\n[INFO] Scattering...")
							showf=1
						file=open(i,"ab")
						encoded_text = cipher_suite.encrypt(bytes(name+start,"utf-8"))
						e_nu = cipher_suite.encrypt(bytes(str(l+1)+"-"+str(len(f))+"|"+str(f),"utf-8"))
						file.write(b"\n"+bytes(emb,"utf-8")+bytes(kv,"utf-8")+key+bytes(emb,"utf-8")+encoded_text+b"\n"+e_nu+b"\n")	
						if int(n)<=len(frag):
							for j in frag[n:n+nl]:
								encoded_text = cipher_suite.encrypt(j)
								file.write(b"\n"+encoded_text+b"\n")
							n+=nl
						if l!=len(f)-1:
							encoded_text=cipher_suite.encrypt(bytes(name+end,"utf-8"))
							file.write(b"\n"+bytes(emb,"utf-8")+bytes(kv,"utf-8")+key+bytes(emb,"utf-8")+encoded_text+b"\n")
						
				if flag==1:
					file=open(f[len(f)-1],"ab")
					for l,j in enumerate(frag[n:]):
						encoded_text = cipher_suite.encrypt(j)
						file.write(b"\n"+encoded_text+b"\n")
					encoded_text=cipher_suite.encrypt(bytes(name+end,"utf-8"))
					file.write(b"\n"+bytes(emb,"utf-8")+bytes(kv,"utf-8")+key+bytes(emb,"utf-8")+encoded_text+b"\n")
					f=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"encfiles"),"ab")
					f.write(bytes(os.getcwd().lower()+"\\"+name+" -d "+dest+"\n","utf-8"))
					if rflag==0:
						print("\n[INFO] Completed")
					if delflg:
						if rflag==1:
							os.remove("{}".format(os.path.join(pname,name)))
						else:
							os.remove("{}".format(os.path.join(pname,name)))
					else:
						q=input("\n[INPUT] Do you want to delete - {} : ".format(name))
						q=q.lower()
						if q=="y" or q=="yes":
							os.remove("{}".format(os.path.join(pname,name)))
				elif flag==0:
					print("\n[INFO] {} already exist!!!".format(name))
	else:
		print("\n[INFO] Path doesn't exist!!!")
