import socket
import os
import sys
import random

host = '127.0.0.1'
port = 2121
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

def ls(cmd):
    client.send(cmd.encode())
    ans = client.recv(1024).decode()
    print(ans)

def dwld(cmd):
    print('prepare for download')
    dwld_port = client.recv(1024).decode()
    dwld_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dwld_client.connect((host, int(dwld_port)))
    filename = cmd[5:]
    with open(filename, 'wb') as dwld_file:
        data = dwld_client.recv(1048576)
        if not data:
            print('there is no data in {}'.format(filename))

        dwld_file.write(data)
        dwld_file.close()
        dwld_client.close()
        print('Download Successfully')

while True:
    cmd = input()

    if cmd.startswith('dwld'):
        client.send(cmd.encode())
        dwld(cmd)

    if cmd.startswith('cd'):
        cd(cmd)

    if cmd == "pwd":
        pwd(cmd)

    if cmd == "list":
        ls(cmd)

    if cmd == "help":
        break
