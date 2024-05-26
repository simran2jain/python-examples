import socket
import time

# import thread module
from _thread import *
import threading

def process_request(conn):
    with open("../data/myfile.txt", "r") as file:
            for dataline in file:
                time.sleep(0.5)
                conn.send(dataline.encode())  # send data to the client
    data = "stop"
    conn.send(data.encode())

def server():
    # get the hostname
    host = socket.gethostbyname("localhost")
    port = 3001  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2000)

    while True:
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        send = conn.recv(1024).decode() 
        if send == 'send data':
            start_new_thread(process_request, (conn, ) )
        elif send == 'stop':
            break
    conn.close()  # close the connection


if __name__ == '__main__':
    try:
        server()
    except Exception as e:
        print("exception occured:",e)
    finally:
        for thread in threading.enumerate():
            if thread != threading.current_thread():
                thread.join()