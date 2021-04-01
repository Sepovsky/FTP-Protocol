import socket
import os
import sys
import random

host = '127.0.0.1'
port = 2121
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

def dwld(cmd):
    filename = cmd[5:]
    rand_port = random.randrange(3000, 50000)
    dwld_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dwld_socket.bind((host, rand_port))
    dwld_socket.listen()
    conn.send(str(rand_port).encode())
    dwld_conn, addres = dwld_socket.accept()
    with open(filename, 'rb') as file:
        dwld_conn.send(file.read())
        file.close()
        dwld_socket.close()


while True:
    cmd = conn.recv(1024).decode()

    if cmd.startswith('cd'):
        cd(cmd[3:])

    if cmd == 'pwd':
        pwd()

    if cmd == 'list':
        ls()

    if cmd.startswith('dwld'):
        dwld(cmd)

    if cmd == 'help':
        pass

