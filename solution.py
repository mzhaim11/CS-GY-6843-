# import socket module

from socket import *

import sys

serverPort = 13331

serverSocket = socket(AF_INET, SOCK_STREAM)

print("Socket Created!!")

try:

    # Prepare a sever socket

    # Fill in start

    serverSocket.bind(('', serverPort))

    serverSocket.listen(1)

    print('The server is ready to server:', serverPort)

    # Fill in end

except error as msg:

    print("Bind failed. Error Code: " + str(msg[0]) + "Message: " + msg[1])

    sys.exit()

print("Socket bind complete")

# start listening on the socket

# fill in start

# fill in end

print('Socket now listening')

while True:

    # Establish the connection

    connectionSocket, addr = serverSocket.accept()

    print('source address:' + str(addr))

    try:

        # Receive message from the socket

        message = connectionSocket.recv(1024)

        print(message, '::', message.split()[0], ':', message.split()[1])

        # obtian the file name carried by the HTTP request message

        filename = message.split()[1]

        print(filename, '||', filename[1:])

        f = open(filename[1:])

        outputdata = f.read()

        print(outputdata)

        # Send one HTTP header line into socket

        # Fill in start

        connectionSocket.send('\nHTTP/1.1 200 OK\n\n')

        # Send the content of the requested file to the client

        connectionSocket.send(outputdata)

        # Fill in end

        connectionSocket.close()

    except IOError:

        # Send response message for file not found

        # Fill in start

        connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')

        connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')

serverSocket.close()