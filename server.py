from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a server socket
#Fill in start
serverPort = 12345
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
#Fill in end

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Fill in start      #Fill in end
    try:
        message = connectionSocket.recv(1024)
        print(message)

        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        #Send one HTTP header line into socket
        print("Success!\n\n")
        connectionSocket.send("\nHTTP/1.x 200 OK\n")

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found (404)
        print("Failure: file not found!\n\n")
        connectionSocket.send("\n404 File Not Found\n")
        connectionSocket.send("\r\n".encode())

        #Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit()  #Terminate the program after sending the corresponding data