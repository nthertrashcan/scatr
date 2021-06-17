
import os
from sys import exit

start="adding200suc07@1999"
end="complete200suc07@1999"
gaps="guessit01071999"
gape="guessit07071999"
default=""
fno=1


def one(name,path,rflag,delflg=False):
	global fno
	if not os.path.isfile(name):
		print("\n[INFO] File not found!!!")
		exit(0)
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
	pname=""
	
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
		flag=0
		try:
			file.readlines().index(bytes(name+start+"\n","utf-8"))
			flag=0
			print("\n[INFO] {} already exist!!!".format(name))
		except:
			flag=1
		if flag==1:
			if rflag==1:
				print("\n[{}] - {}".format(fno,name))
				fno+=1
			else:
				print("\n[INFO] Embedding...")
			file=open(dest,"ab")
			file.write(b"\n"+bytes(name+start+"\n","utf-8"))
			for l,j in enumerate(frag):
				if b'endstream\n' in j:
					m=l
			if m!=0:
				for j in frag[:m]:
					if b'endstream\n' in j:
						file.write(bytes("\n"+gaps,"utf-8")+bytes(j.decode().strip("\n"),"utf-8")+bytes(gaps+"\n","utf-8"))
					else:
						file.write(j)
				for j in frag[m:]:
					try:
						file.write(bytes("\n"+gaps,"utf-8")+bytes(j.decode().strip("\n"),"utf-8")+bytes(gaps+"\n","utf-8"))
					except:
						print("\n[ERROR] Encoding error, Use encryption [-oe]")
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
			else:
				for j in frag[m:]:
					file.write(j)

			file.write(bytes("\n"+name+end+"\n","utf-8"))
			f=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"cache/files"),"ab")
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
