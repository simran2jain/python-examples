import socket
import time
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
    
    while True:
        # print("Connection from: " + str(address))
        conn, address = server_socket.accept()  # accept new connection
        # print("Connection from: " + str(address))
        reqno = 1
        send = conn.recv(1024).decode() 
        if send == 'send data':
            process_request(conn, reqno)
            reqno = reqno + 1
        elif send == 'stop':
            break

    conn.close()  # close the connection


if __name__ == '__main__':
    try:
        server()
    except Exception as e:
        print("Exception occured:", e)
    finally:
        for item in processing_order:
            print(item)