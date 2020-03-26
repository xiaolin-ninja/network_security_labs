from socket import *
import sys

clientSocket = socket(AF_INET, SOCK_STREAM)

if len(sys.argv) != 4:
    print("client: illegal command")
    print("usage: python client.py <server_host> <server_port> <file_name>")
    sys.exit()

host = str(sys.argv[1])
port = int(sys.argv[2])
request = str(sys.argv[3])
request = "GET /" + request + " HTTP/1.1"

try:
    clientSocket.connect((host,port))
    clientSocket.send(request)

    response = clientSocket.recv(1024)
    print(response)
except error, data:
    print error, data
    print("Something went wrong.")
    sys.exit()

clientSocket.close()
