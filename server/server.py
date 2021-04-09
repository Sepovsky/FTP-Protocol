import socket
import os
import sys
import random

host = '127.0.0.1'
port = 2121
ADDR = (host, port)
BUFFERSIZE = 1024
root = os.chdir('files')
ROOT_PATH = os.getcwd()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
conn, address = server.accept()
print('Connected by {}'.format(address[0]))
print('Server listenning........')


def cd(pathcd):

    if not os.path.exists(pathcd):
        msg = "No directory"
        conn.send(msg.encode())

    elif pathcd == '/':
        os.chdir(ROOT_PATH)
        ans = os.getcwd()
        ans = '/'
        res = 'We are now in '+ str(ans)
        conn.send(res.encode())
        print('Successfuly changed directory')

    else:
        if os.path.isdir(pathcd):
            check_path = os.getcwd()
            os.chdir(pathcd)
            ans = os.getcwd()

            if ROOT_PATH in ans:
                ans = ans.replace(ROOT_PATH, '')
                if not ans:
                    ans = '/'
                res = 'We are now in '+ str(ans)
                conn.send(res.encode())
                print('Successfuly changed directory')

            else:
                os.chdir(check_path)
                msg = 'Access Denied!'
                print('Bad Request')
                conn.send(str(msg).encode())
        else:
            msg = f'{pathcd} is not a directory'
            conn.send(str(msg).encode())


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
            ans += '>\t' + l + '\t->\t' + str(os.path.getsize(l)) + ' bytes\n'
        elif os.path.isfile(l):
            ans += '\t' + l + '\t->\t' + str(os.path.getsize(l)) + ' bytes\n' 
    
    ans += 'Total size : ' + str(total_size) + ' bytes'
    conn.send(str(ans).encode())
    print('Successfuly sent list of files')


def dwld(cmd):
    list_files = os.listdir()
    filename = cmd[5:]
    if filename in list_files:
        rand_port = random.randint(3000, 50000)
        dwld_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dwld_socket.bind((host, rand_port))
        dwld_socket.listen()
        conn.send(str(rand_port).encode())
        dwld_conn, addres = dwld_socket.accept()
        with open(filename, 'rb') as file:
            dwld_conn.send(file.read())
            file.close()
            dwld_socket.close()
    else:
        msg = 'Access Denied!'
        print('Bad Request')
        conn.send(str(msg).encode())


while True:
    print('Waiting for command')
    cmd = conn.recv(BUFFERSIZE).decode()

    if cmd.startswith('cd'):
        print('Received command is CD')
        cd(cmd[3:])

    elif cmd == 'pwd':
        print('Received command is PWD')
        pwd()

    elif cmd == 'list':
        print('Received command is LIST')
        ls()

    elif cmd.startswith('dwld'):
        print('Received command is DWLD')
        dwld(cmd)

    elif cmd == 'help':
        print('Received command is HELP')
        pass

    elif cmd == 'quit':
        print('Received command is QUIT')
        conn.close()
        print('server closed')
        break


