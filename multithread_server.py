from socket import *
import threading
import sys

class ThreadedServer(object):
    def __init__(self):
        self.host = ''
        self.port = 1111
        self.serverSocket = socket(AF_INET, SOCK_STREAM)

    def run(self):
        print("Ready to serve...")

        self.serverSocket.bind((self.host, self.port))
        self.serverSocket.listen(10)

        while True:
            clientSocket, address = self.serverSocket.accept()
            clientSocket.settimeout(60)

            threading.Thread(
                target = self.new_thread,
                args = (clientSocket, address)
            ).start()

        serverSocket.close()

    def new_thread(self, clientSocket, address):
        while True:
            try:
                request = clientSocket.recv(1024)
                print(request)

                filename = request.split()[1]
                f = open(filename[1:])
                outputdata = f.read()
                clientSocket.send("\nHTTP/1.x 200 OK\n")

                for i in range(0, len(outputdata)):
                    clientSocket.send(outputdata[i].encode())

                clientSocket.send("\r\n".encode())
                clientSocket.close()
            except error, data:
                print error, data
                clientSocket.send("\n400 Bad Request\n")
                clientSocket.close()
                sys.exit()

ThreadedServer().run()