# Lab 1: Web Server Lab

In this lab, you will learn the basics of socket programming for TCP connections in Python: how to create
a socket, bind it to a specific address and port, as well as send and receive a HTTP packet. You will also
learn some basics of HTTP header format.

You will develop a web server that handles one HTTP request at a time. Your web server should accept
and parse the HTTP request, get the requested file from the server’s file system, create an HTTP response
message consisting of the requested file preceded by header lines, and then send the response directly to
the client. If the requested file is not present in the server, the server should send an HTTP “404 Not
Found” message back to the client.

## Optional Exercises
1. Currently, the web server handles only one HTTP request at a time. Implement a multithreaded
server that is capable of serving multiple requests simultaneously. Using threading, first create a
main thread in which your modified server listens for clients at a fixed port. When it receives a
TCP connection request from a client, it will set up the TCP connection through another port and
services the client request in a separate thread. There will be a separate TCP connection in a
separate thread for each request/response pair.

2. Instead of using a browser, write your own HTTP client to test your server. Your client will
connect to the server using a TCP connection, send an HTTP request to the server, and display
the server response as an output. You can assume that the HTTP request sent is a GET method.
The client should take command line arguments specifying the server IP address or host name,
the port at which the server is listening, and the path at which the requested object is stored at the
server. The following is an input command format to run the client.
client.py server_host server_port filename
