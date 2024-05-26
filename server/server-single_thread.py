import socket


def server():
    # get the hostname
    host = socket.gethostbyname("localhost")
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)

    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    
    starttime = time.time()
    while True:
        send = conn.recv(1024).decode() 
        if send == 'send data':
            print('start sending data now')
            break

    with open("myfile.txt", "r") as file:
        for dataline in file:
            conn.send(dataline.encode())  # send data to the client
    
    data = "stop"
    conn.send(data.encode())
    conn.close()  # close the connection


if __name__ == '__main__':
    server()