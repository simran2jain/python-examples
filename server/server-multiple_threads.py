import socket
import time

# import thread module
from _thread import *
import threading

def process_request(conn):
    with open("myfile.txt", "r") as file:
            for dataline in file:
                conn.send(dataline.encode())  # send data to the client
                print()
    data = "stop"
    conn.send(data.encode())

def server():
    # get the hostname
    host = socket.gethostbyname("localhost")
    port = 5001  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2000)
    
    req_no = 0
    starttime = time.time()
    while True:
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        send = conn.recv(1024).decode() 
        if send == 'send data':
            start_new_thread(process_request, (conn, ) )
        elif send == 'stop':
            endtime = time.time()
            break
    conn.close()  # close the connection


if __name__ == '__main__':
    server()