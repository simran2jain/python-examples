import socket
import time

# import thread module
from _thread import *
import threading
lock = threading.Lock()

processing_order = []

def process_request(conn, reqno):
    with open("../data/myfile.txt", "r") as file:
            for dataline in file:
                conn.send(dataline.encode())  # send data to the client
                sample_list = list(range(1, 100000000))
                sample_list.sort()
                order = "Execution in progess for request:" + str(reqno)
                processing_order.append(order)
    data = "stop"
    conn.send(data.encode())

def process_request_IO_only(conn, reqno):
    with open("../data/myfile.txt", "r") as file:
            for dataline in file:
                conn.send(dataline.encode())  # send data to the client
                time.sleep(0.5)
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

    reqno = 1
    while True:
        conn, address = server_socket.accept()  # accept new connection
        # print("Connection from: " + str(address))
        send = conn.recv(1024).decode() 
        if send == 'send data':
            start_new_thread(process_request, (conn, reqno ) )
            reqno = reqno + 1
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
        print("Results:")
        for line in processing_order:
            print(line)