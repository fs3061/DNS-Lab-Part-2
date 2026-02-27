from socket import *

def smtp_client(port=1025, mailserver="127.0.0.1"):
    msg = "Subject: SMTP Test\r\n\r\nMy message"
    endmsg = "\r\n.\r\n"

    # Create socket called clientSocket and establish a TCP connection
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    recv = clientSocket.recv(1024).decode()

    # Send HELO command and receive server response
    heloCommand = "HELO Alice\r\n"
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()

    # Send MAIL FROM command
    mailFromCommand = "MAIL FROM:<alice@nyu.edu>\r\n"
    clientSocket.send(mailFromCommand.encode())
    recv2 = clientSocket.recv(1024).decode()

    # Send RCPT TO command
    rcptToCommand = "RCPT TO:<bob@nyu.edu>\r\n"
    clientSocket.send(rcptToCommand.encode())
    recv3 = clientSocket.recv(1024).decode()

    # Send DATA command
    dataCommand = "DATA\r\n"
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024).decode()

    # Send message data (no recv here)
    clientSocket.send(msg.encode())

    # End message with single period
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()

    # Send QUIT command
    quitCommand = "QUIT\r\n"
    clientSocket.send(quitCommand.encode())
    recv6 = clientSocket.recv(1024).decode()

    clientSocket.close()


if __name__ == "__main__":
    smtp_client(1025, "127.0.0.1")