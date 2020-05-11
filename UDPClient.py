from socket import *

serverHost = "127.0.0.1"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
print("Client is ready!")
while 1:
    message = input("Message: ")
    if message == "-1":
        clientSocket.close()
        break
    clientSocket.sendto(str.encode(message), (serverHost, serverPort))
    message, serverAddress = clientSocket.recvfrom(1024)
    print(str(message))