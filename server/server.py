import sys
import socket
import os

host = '127.0.0.1'
port = 35355

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((host, port))
    server.listen()
    connection, address = server.accept()
    with connection:
        print('connected by', address)

        while True:
            data = connection.recv(1024)

            if not data:
                break
            connection.send(data)