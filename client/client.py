import socket
import os
import sys
import random

host = '127.0.0.1'
port = 2111
ADDR = (host, port)
BUFFERSIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def cd():
    # print('hello')
    ans = client.recv(1024).decode()
    print('salam')
    print(ans)


while True:
    cmd = input()
    client.send(cmd.encode('utf-8'))

    if cmd.startswith == "dwld":
        pass

    if 'cd' in cmd:
        cd()

    if cmd == "":
        pass

    if cmd == "":
        pass

    if cmd == "qq":
        break