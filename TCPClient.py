from socket import *

serverHost = "127.0.0.1"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverHost, serverPort))
print("Client is ready!")
while 1:
    message = input("Message: ")
    if message == "-1":
        clientSocket.close()
        break
    clientSocket.send(str.encode(message))
    print(clientSocket.recv(1024))