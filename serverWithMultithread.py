# import socket module
from socket import *
import sys # In order to terminate the program
import threading

server_port = 10024

def handle_client(connectionSocket, address):
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.close()

def main(port):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("", port))
    serverSocket.listen(5)
    print('Ready to serve...')

    while True:
        connectionSocket, addr = serverSocket.accept()
        print(f'New connection from {addr}')
        print("Connection from %s port %s" % addr)
        # 스래드 생성
        client_thread = threading.Thread(target=handle_client, args=(connectionSocket, addr))
        client_thread.start()
    
    serverSocket.close()
    sys.exit() #Terminate the program after sending the corresponding data                                    

main(server_port)