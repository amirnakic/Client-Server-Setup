from socket import *

serverHost = "127.0.0.1"
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverHost, serverPort))
serverSocket.listen()
print("Server is ready!")
connectionSocket, clientAddress = serverSocket.accept()
while 1:
    print("Client address: " + str(clientAddress))
    message = connectionSocket.recv(1024)
    print(message)
    connectionSocket.send(str.encode("OK!"))
