import socket
import os
import sys

host = '127.0.0.1'
port = 35355
ADDR = (host, port)
BUFFERSIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(ADDR)
    server.listen()
    connection, address = server.accept()

    def dwld(filename):
        with open(filename, 'rb') as file:
            connection.sendall(file.read())
            print('salam')
            file.close()
            server.close()

    cmd = connection.recv(1024).decode('utf-8')
    if 'dwld' in cmd:
        dwld(cmd[5:])