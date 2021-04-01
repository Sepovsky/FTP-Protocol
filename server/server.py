import socket
import os
import sys
import random

host = '127.0.0.1'
port = 2142
ADDR = (host, port)
BUFFERSIZE = 1024
ROOT_PATH = os.getcwd()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
conn, address = server.accept()
print('connected by {}'.format(address[0]))

def cd(pathcd):
    # print(pathcd)
    if not os.path.exists(pathcd):
        msg = "No directory"
        conn.send(msg.encode())
    else:
        os.chdir(pathcd)
        ans = os.getcwd()
        ans = ans.replace(ROOT_PATH, '')
        if not ans:
            ans = '/'
        conn.send(str(ans).encode())

def pwd():
    ans = os.getcwd()
    ans = ans.replace(ROOT_PATH, '')
    if not ans:
        ans = '/'
    conn.send(str(ans).encode())

def ls():

    list_files = os.listdir()
    total_size = 0
    ans = ''
    for l in list_files:
        total_size += os.path.getsize(l)
        if os.path.isdir(l):
            ans += '>\t' + l + '\t' + str(os.path.getsize(l)) + '\n'
        elif os.path.isfile(l):
            ans += '\t' + l + '\t' + str(os.path.getsize(l)) + '\n' 
    
    ans += 'Total size:\t' + str(total_size)
    conn.send(str(ans).encode())


while True:
    cmd = conn.recv(1024).decode()

    if cmd.startswith('cd'):
        # print('cd is here')
        cd(cmd[3:])

    if cmd == 'pwd':
        pwd()

    if cmd == 'list':
        ls()
