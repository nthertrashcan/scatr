import os
from sys import exit

start="adding200suc07@1999"
end="complete200suc07@1999"
gaps="guessit01071999"
gape="guessit07071999"
default=""
fno=1



def scatt(name,path,rflag,delflg):
	global fno

	if not os.path.isfile(name):
		print("\n[INFO] File not found!!!")
		exit(0)
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
				file=open(f[0],"rb")
				flag=0
				try:
					file.readlines().index(bytes(name+start+"\n","utf-8"))
					print("\n[INFO] {} already exist!!!".format(name))
					exit(0)
				except:
					flag=1
				if flag==1:
					print("\n[INFO] Scattering...")
					file=open(f[0],"ab")
					file.write(b"\n"+bytes(name+start+"\n","utf-8"))
					for i in frag:
						file.write(i)
					file.write(b"\n")
					file.write(b"\n"+bytes(name+end+"\n","utf-8"))
				f=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"files"),"ab")
				f.write(bytes(os.getcwd().lower()+"\\"+name+" -d "+dest+"\n","utf-8"))
				print("\n[INFO] Completed")
				q=input("\n[INPUT] Do you want to delete - {} : ".format(name))
				q=q.lower()
				if q=="y" or q=="yes":
					os.remove("{}".format(os.path.join(pname,name)))
				flag=0
			else:
				dflag=0
				for l,j in enumerate(frag):
					if b'endstream\n' in j:
						m=l
				if m!=0:
					dflag=1
					nl=len(frag[:m])
					nl=int(nl/len(f))
				else:
					m=len(frag)
					nl=len(frag[:m])
					nl=int(nl/len(f))
				flag=0
				eflag=0
				cou=0
				showf=0
				for l,i in enumerate(f):
					file=open(i,"rb")
					try:
						file.readlines().index(bytes(name+start+"\n","utf-8"))
						flag=0
						continue
					except:
						flag=1
						if showf==0:
							if rflag==1:
								print("\n[{}] - {}".format(fno,name))
								fno+=1
							else:
								print("\n[INFO] Scattering...")
							showf=1
					if flag==1:
						file=open(i,"ab")
						file.write(b"\n"+bytes(name+start+"\n"+str(l+1)+"-"+str(len(f))+"|"+str(f)+"\n","utf-8"))
						if int(n)<=m:
							for j in frag[n:n+nl]:
								if b'endstream\n' in j:
									file.write(bytes("\n"+gaps,"utf-8")+bytes(j.decode().strip("\n"),"utf-8")+bytes(gaps+"\n","utf-8"))
								else:
									file.write(j)
							n+=nl
						if l!=len(f)-1:
							file.write(b"\n"+bytes(name+end+"\n","utf-8"))
				if flag==1:
					file=open(f[len(f)-1],"ab")
					if dflag==1:
						for l,j in enumerate(frag[n:m]):
							file.write(j)
						for l,j in enumerate(frag[m:]):
							try:
								file.write(bytes("\n"+gape,"utf-8")+bytes(j.decode().strip("\n"),"utf-8")+bytes(gape+"\n","utf-8"))
							except:
								print("\n[ERROR] Encoding error, Use encryption [-se]")
								print("\n[INFO] Rolling back...")
								file.write(b"\n"+bytes(name+end+"\n","utf-8"))
								file.close()
								clean(name,des)
								if rflag==1:
									print("\n[INFO] Skipping {}".format(name))
									return
								else:
									print("\n[INFO] Exiting")
									exit(0)
					file.write(b"\n"+bytes(name+end+"\n","utf-8"))
					f=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"files"),"ab")
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
					print("\n[INFO] {} already exist!!!".format(name))
	else:
		print("\n[INFO] Path doesn't exist!!!")
