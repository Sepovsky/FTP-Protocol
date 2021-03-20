import socket
import os
import sys

host = '127.0.0.1'
port = 35355

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((host, port))
    client.send(b'salam sepehr hastam')
    data = client.recv(1024)

print("Recived", repr(data) )