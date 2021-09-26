<<<<<<< HEAD
### welcome_assignment_answers
### Input - All eight questions given in the assignment.
### Output - The right answer for the specific question

def welcome_assignment_answers(question):
    #The student doesn't have to follow the skeleton for this assignment.
    #Another way to implement is using a "case" statements similar to C.
    if question == "In Slack, what is the secret passphrase posted in the #cyberfellows-computernetworking-fall2021 channel posted by a TA?":
        answer = "mTLS"
    elif question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif question == "What is the MD5 hashing value to the following message: 'NYU Computer Networking' - Use MD5 hash generator and use the answer in your code":
        answer = "42b76fe51778764973077a5a94056724"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    elif question == "What layer from the TCP/IP model the protocol DHCP belongs to? - The answer should be a numeric numbe":
        answer = 5
    elif question == "What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number":
        answer = 4
    else:
        answer = 5
    return (answer)
# Complete all the questions.


=======
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
>>>>>>> 6be1f650578d33442fafc76837bf0630a6044106
if __name__ == "__main__":
    webServer(13331)