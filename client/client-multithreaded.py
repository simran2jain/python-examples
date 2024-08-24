# simulation of multiple clients using threading
import socket
import time

from _thread import *
import threading
import time

lock = threading.Lock()

def client(i):
    host = socket.gethostbyname("localhost")  # as both code is running on same pc
    port = 3001  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    send = "send data"  #request to send data
    client_socket.send(send.encode())

    starttime = time.time()
    while True:
        data = client_socket.recv(1024).decode()  # receive response
        if data == "stop":
            break
        elif data:
           lock.acquire()
           print("processing client:", i)  # show in terminal
           lock.release()

    send = "stop"  #request to send data
    client_socket.send(send.encode())
    client_socket.close()  # close the connection


if __name__ == '__main__':
    start = time.time()
    for i in range(1,4):
        t = threading.Thread(target=client, args=(i,))
        t.start()
    for thread in threading.enumerate():
        if thread != threading.current_thread():
            thread.join()
    end = time.time()
    print("response time:", (end-start)*1000)
    