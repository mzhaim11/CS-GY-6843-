from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    server = mailserver
    mailPort = port
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect((server, mailPort))
    # Fill in start
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    # if recv1[:3] != '250':
      #  print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    mailFrom = "MAIL FROM: <example12 (at the rate) xyz(dot)com> \r\n"
    clientSocket.send(mailFrom.encode())
    # recv2 = clientSocket.recv(1024)
    # print("After MAIL FROM command: " + recv2)
    # if recv1[:3] != '250':
    # print('250 reply not received from server.')
    # Fill in start
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    # Fill in end
    rcptTo = "RCPT TO: <destination12(at the rate) xyz(dot)com> \r\n"
    clientSocket.send(rcptTo.encode())
    # recv3 = clientSocket.recv(1024)
    # print("After RCPT TO command: " + recv3)
    # if recv1[:3] != '250':
    # print('250 reply not received from server.')

    # Send DATA command and print server response.
    # Fill in start
    # Fill in end
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    # recv4 = clientSocket.recv(1024)
    # print("After DATA command: " + recv4)
    # if recv1[:3] != '250':
    # print('250 reply not received from server.')

    # Send message data.
    message = raw_input("Enter your message: \r\n")
    # Fill in start
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    # Fill in end
    mailMessageEnd = '\r\n.\r\n'
    clientSocket.send(message + mailMessageEnd)
    # print(recv1)
    # if recv1[:3] != '250':
    # print('250 reply not received from server.')
    # Send QUIT command and get server response.
    # Fill in start
    # Fill in end
    clientSocket.send("QUIT\r\n".encode())
    # message = clientSocket.recv(1024)
    # print(message)
    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')