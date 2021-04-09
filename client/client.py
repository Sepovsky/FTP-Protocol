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

def help():
    commands = ['HELP', 'LIST', 'PWD', 'CD directory_name', 'DWLD file_path', 'QUIT']
    description = ['Show this help', 'List files', 'Show current directory', 'Change directory', 'Download file', 'Exit']
    for cmd, desc in zip(commands, description):
        ans = cmd.ljust(20, ' ')
        ans += ':'
        ans += desc
        print(ans)


def cd(cmd):
    client.send(cmd.encode())
    ans = client.recv(BUFFERSIZE).decode()
    print(ans)


def pwd(cmd):
    client.send(cmd.encode())
    ans = client.recv(BUFFERSIZE).decode()
    print(ans)


def ls(cmd):
    client.send(cmd.encode())
    ans = client.recv(BUFFERSIZE).decode()
    print(ans)


def dwld(cmd):
    print('Prepare for download')
    dwld_port = client.recv(BUFFERSIZE).decode()

    if dwld_port == 'Access Denied!':
        print('Access Denied!')

    else:
        dwld_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dwld_client.connect((host, int(dwld_port)))
        filename = cmd[5:]
        with open(filename, 'wb') as dwld_file:
            data = b""
            while True:
                binary_dwld = dwld_client.recv(BUFFERSIZE)
                data += binary_dwld

                if not binary_dwld:
                    break

            dwld_file.write(data)
            dwld_file.close()
            dwld_client.close()
            print('Downloaded Successfully')



print('Welcome to FTP-client made by Sepehr Shirani')
print()
help()

while True:
    cmd = input('Enter a command:')

    if cmd.startswith('dwld'):
        client.send(cmd.encode())
        dwld(cmd)

    elif cmd.startswith('cd'):
        cd(cmd)

    elif cmd == "pwd":
        pwd(cmd)

    elif cmd == "list":
        ls(cmd)

    elif cmd == "help":
        help()

    elif cmd == "quit":
        client.send(cmd.encode())
        client.close()
        print('client closed')
        break

    else:
        test = cmd.split(' ')
        print(f'Command "{test[0]}" is not found')
