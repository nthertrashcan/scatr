
import os
import subprocess as sp
from prettytable import PrettyTable
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




def table(t):
	print("\n[INFO]\n")
	print("--------------------------------------")
	print("| Missing Fragment\t|\tFile |")
	print("--------------------------------------")

	for key,value in t.items():
		print(f"| {key}\t\t\t|\t{value} |")




def retrenc(name,path,kv):
	if kv!="":
		kv = hashlib.sha256(kv.encode()) 
		kv=kv.hexdigest() 
	des=""
	if path=="":
		flag=0
		fflag=0
		fil=[]
		f=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"encfiles"),"rb")
		for i in f.readlines():
			if name.lower() in i.decode().strip("\n").split("-d")[0].strip().lower():
				fil.append(i.decode().strip("\n"))
		fil=set(fil)
		if len(fil)>1:
			fdic={}
			for l,i in enumerate(fil):
				if name in i.split("-d")[0].strip():
					if "-d" in i:
						print(l+1,"-",i.split("-d")[1].strip())
						fdic[l+1]=i.split("-d")[1].strip()
			qq=input("\n[INPUT] Choose destination -: ")
			if qq!="":
				nname=fdic[int(qq)].lower().strip()
				for i in fil:
					if nname in i.split("-d")[1].strip():
						des=i.split("-d")[1].strip()
						path=des
						break
			else:
				des=default		
		elif len(fil)==1:
			for i in fil:
				des=i.split("-d")[1].strip()
		if path=="":
			path=input("\n[INPUT] Enter destination -: ")
		if ":" not in path:
			des=os.path.join(os.getcwd(),path)
		else:
			des=path
	else:
		des=""
		if ":" not in path:
			des=os.path.join(os.getcwd(),path)
		else:
			des=path

	name=name.lower()

	
	exflag=0
	ext=""
	for i in extt:
		if str(des.split("\\")[len(des.split("\\"))-1]).endswith(i):
			exflag=1
			ext=i
			break
	key=b""
	flag=0
	msflag=0
	if exflag==1:
		s=0
		e=0
		if not os.path.isfile(des):
			print("\n[INFO] File doesn't exist!!!")
			exit(0)
		file=open(des,"rb")
		for l,i in enumerate(file.readlines()):
			if bytes(emb,"utf-8") in i:
				try:
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
			print("\n[INFO] Retrieving...",name)
			file1=open(name,"wb")
			file=open(des,"rb")
			for j in file.readlines()[s+1:e]:
				if j==b"\n":
					pass
				else:
					cipher_suite = Fernet(key)
					decoded_text = cipher_suite.decrypt(j)
					file1.write(decoded_text)
			flag=1
			file1.close()
		else:
			flag=0

	else:
		if not os.path.isdir(des):
			print("\n[INFO] Path doesn't exist!!!")
			exit(0)

		fragn={}
		f=[]
		for r,d,fi in os.walk(des):
			for i in fi:
				f.append(os.path.join(r,i))
		if len(f)==0:
			print("\n[INFO] Empty folder!!!")
			exit(0)
		elif len(f)>0:
			s=0
			e=0
			for k in f:
				file=open(k,"rb")
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
					data=[]
					try:
						file=open(k,"rb")
						v=file.readlines()[s+1]
						cipher_suite = Fernet(key)
						decoded_text = cipher_suite.decrypt(v)
						v=decoded_text.decode()
						fn=int(v.split("-")[0])
						fnt=int(v.split("-")[1].strip("\n").split("|")[0].strip("\n"))
						fl=[]
						fl=eval(v.split("|")[1])
						data.append(k)
						data.append(s)
						data.append(e)
						data.append(fnt)
						data.append(fl)
						fragn[fn]=data
					except:
						pass
				else:
					print("\n[INFO] File doesn't exist!!!")
					exit(0)
			flag=1
			if len(fragn)>0:
				tmp=0
				for i in fragn:
					tmp=i
					break
				print(f"\n[INFO] Total nummber of Fragments: {fragn[tmp][3]}")
				t={}

				for i in range(1,fragn[tmp][3]+1):
					if i in fragn:
						pass
					else:
						t[i]=fragn[tmp][4][i-1]
						msflag=1
						flag=0
				if len(t)>0:
					# table(t)
					tp = PrettyTable(['Missing Fragment', 'Filename'])
					for key, val in t.items():
						tp.add_row([key+1, val])
					print("\n[INFO]")
					print(tp)
			else:
				print("\n[INFO] Empty folder!!!")
				exit(0)
			if msflag==1:
				pass
			else:
				print("\n[INFO] Retrieving...",name)
				file1=open(name,"wb")
				tm=set(fragn)
				for i in tm:
					file=open(fragn[i][0],"rb")
					for j in file.readlines()[int(fragn[i][1])+2:int(fragn[i][2])]:
						if j==b"\n":
							pass
						else:
							cipher_suite = Fernet(key)
							decoded_text = cipher_suite.decrypt(j)
							file1.write(decoded_text)
				file1.close()
	if flag==1:
		print("\n[INFO] Completed")
		q=input("\n[INPUT] Do you want to open - {} : ".format(name))
		q=q.lower()
		if q=="y" or q=="yes":
			try:
				sp.Popen('{}'.format(name),shell=True)
			except:
				print("\n[ERROR] Unable to open")
	elif flag==0 and msflag==0:
		print("\n[INFO] File doesn't exist!!!")
