from socket import *

serverHost = "127.0.0.1"
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverHost, serverPort))
print("Listening...")
while 1:
    message, clientAddress = serverSocket.recvfrom(1024)
    message = str(message).upper()
    serverSocket.sendto(str.encode(message), clientAddress)