import socket
import time


def client():
    host = socket.gethostbyname("localhost")  # as both code is running on same pc
    port = 5000  # socket server port number

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
           print(data)  # show in terminal

    stop = "stop"  #request to stop sending data
    client_socket.send(stop.encode())

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client()
    