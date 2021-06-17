
import os
from cryptography.fernet import Fernet
import hashlib
from sys import exit

extt=[".pdf",".mp3",".wav",".mp4",".mkv",".png",".jpg",".jpeg",".zip",".rar",".docx"]
emb="xasdx"
start="adding200suc07@1999"
end="complete200suc07@1999"
gaps="guessit01071999"
gape="guessit07071999"
default=""



def cleanenc(name,path,kv):
	if kv!="":
		kv = hashlib.sha256(kv.encode()) 
		kv=kv.hexdigest() 
	des=""
	nname=""
	fil=[]
	f=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"encfiles"),"rb")
	for i in f.readlines():
		if name.lower() in i.decode().strip("\n").split("-d")[0].strip().lower():
			fil.append(i.decode().strip("\n"))
	fil=set(fil)
	if path=="":
		flag=0
		
		if len(fil)>1:
			fdic={}
			for l,i in enumerate(fil):
				if name in i.split("-d")[0].strip():
					if "-d" in i:
						print(l+1,"-",i.split("-d")[1].strip())
						fdic[l+1]=i.split("-d")[1].strip()	
			qq=input("\n[INFO] Choose destination -: ")
			if qq!="":
				ename=fdic[int(qq)].lower().strip()
				for i in fil:
					if ename in i.split("-d")[1].strip():
						nname=i
						des=i.split("-d")[1].strip()
						break
			else:
				des=default
				for i in fil:
					if name in i.split("-d")[0].strip():
						if des in i.split("-d")[1].strip():
							nname=i
							break			
		else:
			for i in fil:
				nname=i
				des=i.split("-d")[1].strip()
		if path=="":
			path=input("\n[INPUT] Enter destination -: ")
		if ":" not in path:
			des=os.getcwd()+"\\"+path
		else:
			des=path
	else:
		des=""
		if ":" not in path:
			des=os.getcwd()+"\\"+path
		else:
			des=path

		for i in fil:
			if name.lower() in i.split("-d")[0].strip().lower():
				if des.lower() in i.split("-d")[1].strip().lower():
					nname=i
					break
	exflag=0
	name=name.lower()
	if des!="":
		for i in extt:
			if str(des.split("\\")[len(des.split("\\"))-1]).endswith(i):
				exflag=1
				ext=i
				break
		flag=1
		if exflag==1:
			if not os.path.isfile(des):
				print("\n[INFO] File doesn't exist!!!")
				exit(0)
			s=0
			e=0
			file=open(des,"rb")
			for l,i in enumerate(file.readlines()):
				try:
					if bytes(emb,"utf-8") in i:
						if str(kv)!="":
							key=str(i).split(emb)[1].split(str(kv))[1].encode()
						else:
							key=str(i).split(emb)[1].encode()
						cipher_suite = Fernet(key)
						decoded_text = cipher_suite.decrypt(str(i).split(emb)[2][:len(str(i).split(emb)[2])-3].encode())
						if bytes(name+start,"utf-8") in decoded_text:
							s=l
						elif bytes(name+end,"utf-8") in decoded_text:
							e=l 
				except:
					pass
			if s!=0:
				print("\n[INFO] Cleaning...",name," from ",des)
				file1=open(os.path.join(os.getcwd(),"temp"),"wb")
				file=open(des,"rb")
				for j in file.readlines()[:s]:
					file1.write(j)
				file1=open(os.path.join(os.getcwd(),"temp"),"ab")
				file=open(des,"rb")
				for j in file.readlines()[e+1:]:
					file1.write(j)
				file1=open(os.path.join(os.getcwd(),"temp"),"rb")
				file=open(des,"wb")
				for j in file1.readlines():
					file.write(j)
				file1.close()
				os.remove("{}".format(os.path.join(os.getcwd(),"temp")))
				flag=0
			else:
				flag=1
		else:
			if not os.path.isdir(des):
				print("\n[INFO] Path doesn't exist!!!")
				exit(0)
			showf=0
			f=[]
			for r,d,fi in os.walk(des):
				for i in fi:
					f.append(os.path.join(r,i))
			if len(f)==0:
				print("\n[INFO] Empty folder!!!")
				exit(0)
			elif len(f)>0:
				for i in f:
					s=0
					e=0
					file=open(i,"rb")
					for l,j in enumerate(file.readlines()):
						try:
							if bytes(emb,"utf-8") in j:
								if str(kv)!="":
									key=str(j).split(emb)[1].split(str(kv))[1].encode()
								else:
									key=str(j).split(emb)[1].encode()
								cipher_suite = Fernet(key)
								decoded_text = cipher_suite.decrypt(str(j).split(emb)[2][:len(str(j).split(emb)[2])-3].encode())
								if bytes(name+start,"utf-8") in decoded_text:
									s=l
								elif bytes(name+end,"utf-8") in decoded_text:
									e=l
						except:
							pass
					if s!=0:
						if showf==0:
							print("\n[INFO] Cleaning...",name," from ",des)
							showf=1
						file1=open(os.path.join(r,"temp"),"wb")
						file=open(i,"rb")
						for j in file.readlines()[:s]:
							file1.write(j)
						file1=open(os.path.join(r,"temp"),"ab")
						file=open(i,"rb")
						for j in file.readlines()[e+1:]:
							file1.write(j)
						file1=open(os.path.join(r,"temp"),"rb")
						file=open(i,"wb")
						for j in file1.readlines():
							file.write(j)
						file1.close()
						os.remove("{}".format(os.path.join(r,"temp")))
						flag=0
					else:
						flag=1
				
		if flag==0:
			print("\n[INFO] Completed")
			if nname!="":
				fil=[]
				file=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"encfiles"),"rb")
				for i in file.readlines():
					fil.append(i.decode().strip("\n"))
				fil=set(fil)
				fil.remove(nname)
				file=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"encfiles"),"wb")
				for i in fil:
					file.write(bytes(i,"utf-8")+b"\n")
		elif flag==1:
			print("\n[INFO] File doesn't exist!!!")
