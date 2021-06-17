
import os
import sys
from sys import exit



def initialize():
	if os.path.isfile(os.path.join(os.path.dirname(os.path.realpath(__file__)),"defaultf.txt")):
		f=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"defaultf.txt"),"r")
		default=f.read()
	else:
		f=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"defaultf.txt"),"w")
		f.write(os.path.dirname(os.path.realpath(__file__)))
	if not os.path.isfile(os.path.join(os.path.dirname(os.path.realpath(__file__)),"files")):
		f=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"files"),"wb")
		f.close()
	if not os.path.isfile(os.path.join(os.path.dirname(os.path.realpath(__file__)),"encfiles")):
		f=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"encfiles"),"wb")
		f.close()
	

initialize()



if len(sys.argv)>1:
	if str(sys.argv[1]).lower()=="-s":
		delflg=0
		if len(sys.argv)>2:
			cmd=""
			for i in sys.argv[2:]:
				cmd+=" "+i
			cmd=cmd.strip()
			des=""
			name=""
			if "-d" in cmd:
				name=cmd.split("-d")[0].strip()
				des=cmd.split("-d")[1].strip()
				if "-flag" in des:
					delflg=int(des.split("-flag")[1].strip())
					des=des.split("-flag")[0].strip()

				if des=="":
					des=input("\n[INPUT] Enter destination -:")
					if not os.path.isdir(des):
						if not os.path.isdir(os.path.join(os.getcwd(),des)):
							print("\n[INFO] Invalid address!!!")
							exit()
						else:
							des=os.path.join(os.getcwd(),des)
				if os.path.isdir(des):
					scatt(name.lower(),des,0,delflg)
				else:
					print("\n[INFO] Path doesn't exist!!!")
					exit()
			elif "-r" in cmd:
				name=cmd.split("-r")[0].strip()
				des=cmd.split("-r")[1].strip()
				
				if "-flag" in des:
					delflg=int(des.split("-flag")[1].strip())
					des=des.split("-flag")[0].strip()

				if des=="":
					des=input("\n[INPUT] Enter destination -:")
					if not os.path.isdir(des):
						if not os.path.isdir(os.path.join(os.getcwd(),des)):
							print("\n[INFO] Invalid address!!!")
							exit()
						else:
							des=os.path.join(os.getcwd(),des)

				if os.path.isdir(name):
					print("\n[INFO] Scattering...")
					for r,d,f in os.walk(name):
						for i in f:
							scatt(os.path.join(name,i.lower()),des,1,delflg)
					fno=1
					print("\n[INFO] Completed")
			else:
				name=cmd
				if "-flag" in cmd:
					delflg=int(cmd.split("-flag")[1].strip())
					name=cmd.split("-flag")[1].strip()
				if not os.path.isfile(name):
					if not os.path.isfile(os.path.join(os.getcwd(),name)):
						print("\n[INFO] File not found!!!")
						exit()
					else:
						name=os.path.join(os.getcwd(),name)
				scatt(name.lower(),"",0,delflg)

		else:
			name=input("\n[INPUT] Enter filename -: ")
			if name!="":
				if os.path.isfile(name):
					scatt(name.lower(),"",0,0)
				else:
					print("\n[INFO] File not found!!!")
			else:
				print("\n[INFO] Path doesn't exist!!!")

	elif str(sys.argv[1]).lower()=="-r":
	    if len(sys.argv)>2:
	    	cmd=""
	    	for i in sys.argv[2:len(sys.argv)]:
	    		cmd+=" "+i
	    	cmd=cmd.strip()
	    	des=""
	    	if "-d" in cmd:
	    		if cmd.split("-d")[1]!="":
		    		des=cmd.split("-d")[1].strip()
		    		cmd=cmd.split("-d")[0].strip()
		    	else:
		    		des=input("\n[INPUT] Enter destination -: ")
		    		cmd=cmd.split("-d")[0].strip()
		    		des=des.lower().strip()
	    	retr(cmd,des)
	    else:
	    	fil=[]
	    	cdic={}
	    	f=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"files"),"rb")
	    	if len(f.readlines())==0:
	    		print("\n[INFO] Empty file!!!")
	    	f=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"files"),"rb")
	    	if len(f.readlines())>0:
		    	f=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"files"),"rb")
		    	for i in f.readlines():
		    		fil.append(i.decode().strip("\n").split("-d")[0].split("\\")[len(i.decode().strip("\n").split("-d")[0].split("\\"))-1])
		    	fil=set(fil)
		    	for l,i in enumerate(fil):
		    		print(l+1,"-",i)
		    		cdic[l+1]=i
		    	qq=input("\n[INPUT] Enter -: ")
		    	if qq!="":
	    			val=cdic[int(qq)].lower().strip()
	    			retr(val,"")
	    		

	elif str(sys.argv[1]).lower()=="-c":
		if len(sys.argv)>2:
			cmd=""
			for i in sys.argv[2:len(sys.argv)]:
				cmd+=" "+i
			cmd=cmd.strip()
			des=""
			if "-d" in cmd:
				if cmd.split("-d")[1]!="":
					des=cmd.split("-d")[1].strip()
					cmd=cmd.split("-d")[0].strip()
				else:
					des=input("\n[INPUT] Enter destination -: ")
					cmd=cmd.split("-d")[0].strip()
					des=des.lower().strip()
			clean(cmd,des)
		else:
			fil=[]
			cdic={}
			f=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"files"),"rb")
			if len(f.readlines())==0:
				print("\n[INFO] Empty file!!!")
			f=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"files"),"rb")
			if len(f.readlines())>0:
				f=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"files"),"rb")
				for i in f.readlines():
					fil.append(i.decode().strip("\n").split("-d")[0].split("\\")[len(i.decode().strip("\n").split("-d")[0].split("\\"))-1])
			
				fil=set(fil)
				for l,i in enumerate(fil):
					print(l+1,"-",i)
					cdic[l+1]=i
				qq=input("\n[INPUT] Enter -: ")
				if qq!="":
					val=cdic[int(qq)].lower().strip()
					clean(val,"")
			

	elif str(sys.argv[1]).lower()=="-f":
		flag=0
		cmd=""
		if len(sys.argv)>2:
			for i in sys.argv[2:len(sys.argv)]:
				cmd+=" "+i
			cmd=cmd.strip()
			flag=1

		fil=[]
		f=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"files"),"rb")
		for i in f.readlines():
			fil.append(i.decode().strip("\n"))

		fil=set(fil)
		if flag==1:
			dflag=0
			for i in fil:
				if cmd in i:
					print(i.split("-d")[0],"| -d ",i.split("-d")[1].strip())
					dflag=1
			if dflag==0:
				print("\n[INFO] File doesn't exist!!!")
		else:
			if len(fil)>0:
				for i in fil:
					print(i.split("-d")[0],"| -d ",i.split("-d")[1].strip())
			else:
				print("\n[INFO] Empty file!!!")

	elif str(sys.argv[1]).lower()=="clear" or str(sys.argv[1]).lower()=="clean":
		f1=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"files"),"wb")
		f1.write(b"")
		f1=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"encfiles"),"wb")
		f1.write(b"")
		f1=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"defaultf.txt"),"w")
		f1.write("")
		print("\n[INFO] Cleared!!!")

	elif str(sys.argv[1]).lower()=="-o":

		delflg=0
		if len(sys.argv)>2:
			cmd=""
			for i in sys.argv[2:]:
				cmd+=" "+i
			cmd=cmd.strip()
			des=""
			name=""
			if "-d" in cmd:
				name=cmd.split("-d")[0].strip()
				des=cmd.split("-d")[1].strip()
				if "-flag" in des:
					delflg=int(des.split("-flag")[1].strip())
					des=des.split("-flag")[0].strip()

				if des!="":
					if os.path.isfile(des):
						one(name.lower(),des,0,delflg)
					else:
						print("\n[INFO] File not found!!!")
				else:
					one(name.lower(),"",0,delflg)
			elif "-r" in cmd:
				name=cmd.split("-r")[0].strip()
				des=cmd.split("-r")[1].strip()
				
				if "-flag" in des:
					delflg=int(des.split("-flag")[1].strip())
					des=des.split("-flag")[0].strip()

				if des=="":
					des=input("\n[INPUT] Enter destination -:")
					if not os.path.isfile(des):
						if not os.path.isfile(os.path.join(os.getcwd(),des)):
							print("\n[INFO] Invalid filename!!!")
							exit()
						else:
							des=os.path.join(os.getcwd(),des)
				if os.path.isdir(name):
					print("\n[INFO] Embedding...")
					for r,d,f in os.walk(name):
						for i in f:
							one(os.path.join(name,i.lower()),des,1,delflg)
					fno=1
					print("\n[INFO] Completed")
			else:
				name=cmd
				if "-flag" in cmd:
					delflg=int(cmd.split("-flag")[1].strip())
					name=cmd.split("-flag")[0].strip()
				if not os.path.isfile(name):
					if not os.path.isfile(os.path.join(os.getcwd(),name)):
						print("\n[INFO] File not found!!!")
						exit()
					else:
						name=os.path.join(os.getcwd(),name)
		
				one(name.lower(),"",0,delflg)
				
		else:
			name=input("\n[INPUT] Enter filename -: ")
			if name!="":
				if os.path.isfile(name):
					one(name.lower(),"",0)
				else:
					print("\n[INFO] File not found!!!")
			else:
				print("\n[INFO] Path doesn't exist!!!")

	elif str(sys.argv[1]).lower()=="-se":
		key=""
		des=""
		name=""
		delflg=0
		if len(sys.argv)>2:
			cmd=""
			for i in sys.argv[2:]:
				cmd+=" "+i
			cmd=cmd.strip()
			
			if "-d" in cmd:
				name=cmd.split("-d")[0].strip()
				des=cmd.split("-d")[1].strip()
				if "-k" in des:
					key=des.split("-k")[1].strip()
					des=des.split("-k")[0].strip()
				if "-flag" in key:
					delflg=int(key.split("-flag")[1].strip())
					key=key.split("-flag")[0].strip()

				if des=="":
					des=input("\n[INPUT] Enter destination -:")
					if not os.path.isdir(des):
						if not os.path.isdir(os.path.join(os.getcwd(),des)):
							print("\n[INFO] Invalid address!!!")
							exit()
						else:
							des=os.path.join(os.getcwd(),des)

				if os.path.isdir(des):
					scattenc(name.lower(),des,key,0,delflg)
				else:
					print("\n[INFO] Path doesn't exist!!!")
					exit(0)
			
			elif "-r" in cmd:
				name=cmd.split("-r")[0].strip()
				des=cmd.split("-r")[1].strip()
				if "-k" in des:
					key=des.split("-k")[1].strip()
					des=des.split("-k")[0].strip()
				if "-flag" in key:
					delflg=int(key.split("-flag")[1].strip())
					key=key.split("-flag")[0].strip()
				if des=="":
					des=input("\n[INPUT] Enter destination -:")
					if not os.path.isdir(des):
						if not os.path.isdir(os.path.join(os.getcwd(),des)):
							print("\n[INFO] Invalid address!!!")
							exit()
						else:
							des=os.path.join(os.getcwd(),des)
				if os.path.isdir(name):
					print("\n[INFO] Scattering...")
					for r,d,f in os.walk(name):
						for i in f:
							scattenc(os.path.join(name.lower(),i.lower()),des,key,1,delflg)
					fno=1
					print("\n[INFO] Completed")
			elif "-k" in cmd:
				key=cmd.split("-k")[1].strip()
				name=cmd.split("-k")[0].strip()
				if "-flag" in key:
					delflg=key.split("-flag")[1].strip()
					key=key.split("-flag")[0].strip()
				scattenc(name.lower(),des,key,0,delflg)
			else:
				name=cmd
				if "-flag" in cmd:
					delflg=cmd.split("-flag")[1].strip()
					name=cmd.split("-flag")[0].strip()
				scattenc(name.lower(),des,key,0,delflg)
		else:
			name=input("\n[INPUT] Enter filename -: ")
			if name!="":
				if os.path.isfile(name):
					scattenc(name.lower(),"",key,0,0)
				else:
					print("\n[INFO] File not found!!!")
			else:
				print("\n[INFO] Invalid path!!!")

	elif str(sys.argv[1]).lower()=="-re":
			key=""
			name=""
			if len(sys.argv)>2:
				cmd=""
				for i in sys.argv[2:len(sys.argv)]:
					cmd+=" "+i
				cmd=cmd.strip()
				des=""
				if "-d" in cmd:
					if cmd.split("-d")[1]!="":
						des=cmd.split("-d")[1].strip()
						if "-k" in des:
							key=des.split("-k")[1].strip()
							des=des.split("-k")[0].strip()
						name=cmd.split("-d")[0].strip()
					else:
						des=input("\n[INPUT] Enter destination -: ")
						name=cmd.split("-d")[0].strip()
						des=des.lower().strip()

					retrenc(name.lower(),des.lower(),key)
				elif "-k" in cmd:
					key=cmd.split("-k")[1].strip()
					name=cmd.split("-k")[0].strip()
					retrenc(name.lower(),des.lower(),key)
				else:
					name=cmd
					retrenc(name.lower(),des.lower(),key)	
			else:
				fil=[]
				cdic={}
				f=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"encfiles"),"rb")
				if len(f.readlines())==0:
					print("\n[INFO] Empty file!!!")
				f=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"encfiles"),"rb")
				if len(f.readlines())>0:
					f=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"encfiles"),"rb")
					for i in f.readlines():
						fil.append(i.decode().strip("\n").split("-d")[0].split("\\")[len(i.decode().strip("\n").split("-d")[0].split("\\"))-1])
					fil=set(fil)
					for l,i in enumerate(fil):
						print(l+1,"-",i)
						cdic[l+1]=i
					qq=input("\n[INPUT] Enter -: ")
					if qq!="":
						val=cdic[int(qq)].lower().strip()
						retrenc(val,"",key)

	elif str(sys.argv[1]).lower()=="-ce":
		key=""
		name=""
		des=""
		if len(sys.argv)>2:
			cmd=""
			for i in sys.argv[2:len(sys.argv)]:
				cmd+=" "+i
			cmd=cmd.strip()
			if "-d" in cmd:
				if cmd.split("-d")[1]!="":
					des=cmd.split("-d")[1].strip()
					if "-k" in des:
						key=des.split("-k")[1].strip()
						des=des.split("-k")[0].strip()
					name=cmd.split("-d")[0].strip()
				else:
					des=input("\n[INPUT] Enter destination -: ")
					name=cmd.split("-d")[0].strip()
					des=des.lower().strip()
				cleanenc(name.lower(),des,key)
			elif "-k" in cmd:
				key=cmd.split("-k")[1].strip()
				name=cmd.split("-k")[0].strip()
				cleanenc(name.lower(),des,key)
			else:
				name=cmd
				cleanenc(name.lower(),des,key)
		else:
			fil=[]
			cdic={}
			f=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"encfiles"),"rb")
			if len(f.readlines())==0:
				print("\n[INFO] Empty file!!!")
			f=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"encfiles"),"rb")
			if len(f.readlines())>0:
				f=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"encfiles"),"rb")
				for i in f.readlines():
					fil.append(i.decode().strip("\n").split("-d")[0].split("\\")[len(i.decode().strip("\n").split("-d")[0].split("\\"))-1])
				fil=set(fil)
				for l,i in enumerate(fil):
					print(l+1,"-",i)
					cdic[l+1]=i
				qq=input("\n[INPUT] Enter -: ")
				if qq!="":
					val=cdic[int(qq)].lower().strip()
					cleanenc(val,"",key)
				
	elif str(sys.argv[1]).lower()=="-oe":
		key=""
		name=""
		des=""
		delflg=0
		if len(sys.argv)>2:
			cmd=""
			for i in sys.argv[2:]:
				cmd+=" "+i
			cmd=cmd.strip()
			if "-d" in cmd:
				name=cmd.split("-d")[0].strip()
				des=cmd.split("-d")[1].strip()
				if "-k" in des:
					key=des.split("-k")[1].strip()
					des=des.split("-k")[0].strip()
				if "-flag" in des:
					delflg=int(des.split("-flag")[1].strip())
					des=des.split("-flag")[0].strip()
				if des!="":
					if os.path.isfile(des):
						onenc(name.lower(),des,key,0,delflg)
					else:
						print("\n[INFO] File not found!!!")
				else:
					print("\n[INFO] Invalid filename!!!")
					exit(0)
			elif "-r" in cmd:
				name=cmd.split("-r")[0].strip()
				des=cmd.split("-r")[1].strip()
				
				if "-k" in des:
					key=des.split("-k")[1].strip()
					des=des.split("-k")[0].strip()

				if "-flag" in key:
					delflg=int(key.split("-flag")[1].strip())
					key=key.split("-flag")[0].strip()
				if des=="":
					des=input("\n[INPUT] Enter destination -:")
					if not os.path.isfile(des):
						if not os.path.isfile(os.path.join(os.getcwd(),des)):
							print("\n[INFO] Invalid filename!!!")
							exit()
						else:
							des=os.path.join(os.getcwd(),des)
				if os.path.isdir(name):
					print("\n[INFO] Embedding...")
					for r,d,f in os.walk(name):
						for i in f:
							onenc(os.path.join(name,i.lower()),des,key,1,delflg)
					fno=1
					print("\n[INFO] Completed")
			elif "-k" in cmd:
				key=cmd.split("-k")[1].strip()
				name=cmd.split("-k")[0].strip()
				if "-flag" in key:
					delflg=key.split("-flag")[1].strip()
					key=key.split("-flag")[0].strip()
				onenc(name.lower(),des,key,0,delflg)
			else:
				name=cmd
				if "-flag" in cmd:
					delflg=cmd.split("-flag")[1].strip()
					name=cmd.split("-flag")[0].strip()
				onenc(name.lower(),des,key,0,delflg)
		else:
			name=input("\n[INPUT] Enter filename -: ")
			if name!="":
				if os.path.isfile(name):
					onenc(name.lower(),"",key,0,0)
				else:
					print("\n[INFO] File not found!!!")
			else:
				print("\n[INFO] Path doesn't exist!!!")

	elif str(sys.argv[1]).lower()=="-fe":
		flag=0
		cmd=""
		if len(sys.argv)>2:
			for i in sys.argv[2:len(sys.argv)]:
				cmd+=" "+i
			cmd=cmd.strip()
			flag=1

		fil=[]
		f=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"encfiles"),"rb")
		for i in f.readlines():
			fil.append(i.decode().strip("\n"))
		fil=set(fil)
		if flag==1:
			dflag=0
			for i in fil:
				if cmd in i:
					print(i.split("-d")[0],"| -d ",i.split("-d")[1].strip())
					dflag=1
			if dflag==0:
				print("\n[INFO] File doesn't exist!!!")
		else:
			if len(fil)>0:
				for i in fil:
					print(i.split("-d")[0],"| -d ",i.split("-d")[1].strip())
			else:
				print("\n[INFO] Empty file!!!")

	elif str(sys.argv[1]).lower()=="-chd":

		file=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"defaultf.txt"),"w")
		if len(sys.argv)>2:
			cmd=""
			for i in sys.argv[2:]:
				cmd+=" "+i
			cmd=cmd.strip()
			file.write(cmd)
		else:
			cmd=input("\n[INPUT] Enter default destination -: ")
			if ":" not in cmd:
				cmd=os.path.join(os.getcwd(),cmd)
			file.write(cmd)

	elif str(sys.argv[1]).lower()=="-cd":
		file=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"defaultf.txt"),"r")
		print(file.read())

	elif str(sys.argv[1]).lower()=="-h" or str(sys.argv[1]).lower()=="-help":
		print(" Usage[ %sctr% OPTIONS NAME ARG1 ARG2 ]\n OPTIONS:\n -s\tScattering\n -se\tEncrypted scattering\n -o\tEmbedding\n -oe\tEncrypted embedding\n -r\tRetrieving\n -re\tRetrieving encrypted files\n -c\tCleaning\n -ce\tCleaning encrypted files\n -f\tList of files\n -fe\tList of encrypted files\n -chd\tChange default diretory\n -cd\tCurrent default diretory \n\n ARG1:\n -d\tDestination\n -r\tRecursively\n\n ARG2\n -k\tKey\n -flag\tDeletion flag")

else:
	print(" Usage[ %sctr% OPTIONS NAME ARG1 ARG2 ]\n OPTIONS:\n -s\tScattering\n -se\tEncrypted scattering\n -o\tEmbedding\n -oe\tEncrypted embedding\n -r\tRetrieving\n -re\tRetrieving encrypted files\n -c\tCleaning\n -ce\tCleaning encrypted files\n -f\tList of files\n -fe\tList of encrypted files\n -chd\tChange default diretory\n -cd\tCurrent default diretory \n\n ARG1:\n -d\tDestination\n -r\tRecursively\n\n ARG2\n -k\tKey\n -flag\tDeletion flag")