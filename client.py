from socket import *
from sys import *

def client(server_host, server_port, path):
    print("im client :)")
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((server_host, server_port))
    
    request = f'GET /{path} HTTP/1.1\r\nHost: {server_host}\r\n\r\n'
    clientSocket.send(request.encode())
    
    response = b''
    while True:
        data = clientSocket.recv(1024)
        if not data:
            break
        response += data
    
    print(response.decode())
    clientSocket.close()


# server_host = "localhost"
# server_port = 10024
# path = "HelloWorld.html"
server_host = argv[1]
server_port = int(argv[2])
path = argv[3]

client(server_host, server_port, path)