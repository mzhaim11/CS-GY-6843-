from socket import *
import socket
import sys
def webServer(port=13331):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(("127.0.0.1", port))
    serverSocket.listen(1)
    while True:
        print ('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        try:
            try:
                message = connectionSocket.recv(1024)
                print ('Message is: ', message)
                filename = message.split()[1]
                print ('File name is: ', filename)
                f = open(helloworld.html[1:])
                outputdata = f.read()
                connectionSocket.send("HTTP/1.1 200 OK ")
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())
                connectionSocket.send("\r\n".encode())
                connectionSocket.close()
            except IOError:
                connectionSocket.send("HTTP/1.1 404 Not Found ")
                connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html> ")
                connectionSocket.close()
        except (ConnectionResetError, BrokenPipeError):
            pass
    serverSocket.close()
    sys.exit()
if __name__ == "__main__":
    webServer(13331)