import socket
import os
import sys
import random

host = '127.0.0.1'
port = 2141
ADDR = (host, port)
BUFFERSIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def cd(cmd):
    # print('hello')
    client.send(cmd.encode())
    ans = client.recv(1024).decode()
    # print('salam')
    print(ans)

def pwd(cmd):
    client.send(cmd.encode())
    ans = client.recv(1024).decode()
    print(ans)


while True:
    cmd = input()

    if cmd.startswith('dwld'):
        pass

    if cmd.startswith('cd'):
        cd(cmd)

    if cmd == "pwd":
        pwd(cmd)

    if cmd == "":
        pass

    if cmd == "qq":
        break