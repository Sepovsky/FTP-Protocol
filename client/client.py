import socket
import os
import sys

host = '127.0.0.1'
port = 35355
ADDR = (host, port)
BUFFERSIZE = 1024


while True:
    cmd = input()

    if cmd.startswith == "dwld":
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect(ADDR)
            filename = cmd[5:]
            # filename = '.'+filename
            client.send(cmd.encode('utf-8'))
            with open(filename, 'wb') as file:
                data = client.recv(1200000)
                file.write(data)
                file.close()
                client.close()
            

    if cmd == "":
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect(ADDR)

    if cmd == "":
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect(ADDR)

    if cmd == "":
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect(ADDR)

    if cmd == "qq":
        break