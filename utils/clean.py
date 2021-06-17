
import os
from sys import exit

extt=[".pdf",".mp3",".wav",".mp4",".mkv",".png",".jpg",".jpeg",".zip",".rar",".docx"]
start="adding200suc07@1999"
end="complete200suc07@1999"
gaps="guessit01071999"
gape="guessit07071999"
default=""





def clean(name,path):
	des=""
	nname=""
	fil=[]
	f=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"cache/files"),"rb")
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
			qq=input("\n[INPUT] Choose destination -: ")
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
					if name.lower() in i.split("-d")[0].strip().lower():
						if des.lower() in i.split("-d")[1].strip().lower():
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
	flag=1
	exflag=0
	name=name.lower()

	if des!="":
		for i in extt:
			if str(des.split("\\")[len(des.split("\\"))-1]).endswith(i):
				exflag=1
				ext=i
				break



		if exflag==1:
			if not os.path.isfile(des):

				print("\n[INFO] File doesn't exits!!!")
				exit(0)
			try:

				file=open(des,"rb")
				s=file.readlines().index(bytes(name+start+"\n","utf-8"))
				file=open(des,"rb")
				e=file.readlines().index(bytes(name+end+"\n","utf-8"))
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
			except:
				flag=1
		else:
			flag=0
			showf=0
			if not os.path.isdir(des):

				print("\n[INFO] Path doesn't exist!!!")
				exit(0)
			f=[]
			for r,d,fi in os.walk(des):
				for i in fi:
					f.append(os.path.join(r,i))
			if len(f)==0:
				print("\n[INFO] Empty folder!!!")
				exit(0)
			elif len(f)>0:
				for i in f:
					try:
						file=open(i,"rb")
						s=file.readlines().index(bytes(name+start+"\n","utf-8"))
						file=open(i,"rb")
						if showf==0:
							print("\n[INFO] Cleaning...",name," from ",des)
							showf=1

						
						e=file.readlines().index(bytes(name+end+"\n","utf-8"))

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
					except:
						flag=1
		if flag==0:
			print("\n[INFO] Completed")
			if nname!="":
				fil=[]
				file=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"cache/files"),"rb")
				for i in file.readlines():
					fil.append(i.decode().strip("\n"))
				fil=set(fil)
				fil.remove(nname)
				file=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"cache/files"),"wb")
				for i in fil:
					file.write(bytes(i,"utf-8")+b"\n")
		elif flag==1:
			print("\n[INFO] File doesn't exist!!!")

