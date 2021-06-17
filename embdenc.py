

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





def onenc(name,path,kv,rflag,delflg):
	global fno
	if not os.path.isfile(name):
		print("\n[INFO] File not found!!!")
		exit(0)
	if kv!="":
		kv = hashlib.sha256(kv.encode()) 
		kv=kv.hexdigest() 
	key = Fernet.generate_key()
	cipher_suite = Fernet(key)
	dest=""
	if path=="":
		dest=input("\n[INPUT] Enter Destination - :")

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
	try:
		indx=[n for n,x in enumerate(name) if x=="\\"][::-1][0]
	except:
		name=os.path.join(os.getcwd(),name)
		indx=[n for n,x in enumerate(name) if x=="\\"][::-1][0]
	pname=name[:indx]
	name=name[indx+1:]
	file=open(os.path.join(pname,name),"rb")
	frag=[]
	for i in file.readlines():
		frag.append(i)
	n=0
	m=0
	if os.path.isfile(dest):
		file=open(dest,"rb")
		flag=1
		for i in file.readlines():
			if bytes(emb,"utf-8") in i:
				key=str(i).split(emb)[1][:len(str(i).split(emb)[2])-3]
				key=key[len(key)-44:len(key)].encode()
				cipher_suite = Fernet(key)
				decoded_text = cipher_suite.decrypt(str(i).split(emb)[2][:len(str(i).split(emb)[2])-3].encode())
				if bytes(name+start,"utf-8") in decoded_text:
					flag=0
					print("\n[INFO] {} already exist!!!".format(name))
					break
		if flag==1:
			if rflag==1:
				print("\n[{}] - {}".format(fno,name))
				fno+=1
			else:
				print("\n[INFO] Embedding...")
			file=open(dest,"ab")
			encoded_text = cipher_suite.encrypt(bytes(name+start,"utf-8"))
			file.write(b"\n"+bytes(emb,"utf-8")+bytes(kv,"utf-8")+key+bytes(emb,"utf-8")+encoded_text+b"\n")
			for j in frag:
				encoded_text = cipher_suite.encrypt(j)
				file.write(b"\n"+encoded_text+b"\n")
			encoded_text=cipher_suite.encrypt(bytes(name+end,"utf-8"))
			file.write(b"\n"+bytes(emb,"utf-8")+bytes(kv,"utf-8")+key+bytes(emb,"utf-8")+encoded_text+b"\n")
			f=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"encfiles"),"ab")
			f.write(bytes(os.getcwd().lower()+"\\"+name+" -d "+dest+"\n","utf-8"))
			if rflag==0:
				print("\n[INFO] Completed")
			if delflg==1:
				if rflag==1:
					os.remove("{}".format(os.path.join(pname,name)))
				else:
					os.remove("{}".format(os.path.join(pname,name)))
			else:
				q=input("\n[INPUT] Do you want to delete - {} : ".format(name))
				q=q.lower()
				if q=="y" or q=="yes":
					os.remove("{}".format(os.path.join(pname,name)))
	else:
		print("\n[INFO] File not found!!!")
