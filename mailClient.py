from socket import *
import ssl
import base64
from email.mime.text import MIMEText

msg = '\r\n I love computer networks!'
endmsg = '\r\n.\r\n'
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.gmail.com'#Fill in start 
mailPort = 587					# port integer 587 25 465  
endmsg2 = '\r\n'

#Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
# Create socket called clientSocket and establish 
# a TCP connection with gmailserver
clientSocket = socket(AF_INET, SOCK_STREAM) # IPv4 internet protocols
clientSocket.connect((mailserver,mailPort))
#Fill in end
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
	print '220 reply not received from server.'
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv = clientSocket.recv(1024).decode()
print recv
if recv[:3] != '250':
	print '250 reply not received from server.'
# Send MAIL FROM command and print server response.
# Fill in start

tlsCommand = 'STARTTLS\r\n'
clientSocket.send(tlsCommand.encode())
recv = clientSocket.recv(1024).decode()
print recv
if recv[:3] != '220':
	print '220 reply not received from server.'
# Add SSL after the STARTTLS command
clientSocket = ssl.wrap_socket(clientSocket)

authCommand = 'AUTH LOGIN\r\n'
clientSocket.write(authCommand.encode())
recv = clientSocket.recv(1024).decode()
print recv
if recv[:3] != '334':
	print '334 reply not received from server.'

mail = "deneme1530@gmail.com"
psw = "EK123456"

clientSocket.write((str(base64.b64encode(mail.encode())).encode("utf-8") 
				+ endmsg2).encode())
recv = clientSocket.recv(1024).decode()
print recv
if recv[:3] != '334':
	print '334 reply not received from server.'

clientSocket.write((str(base64.b64encode(psw.encode())).encode("utf-8") 
				+ endmsg2).encode())
recv = clientSocket.recv(1024).decode()
print recv
if recv[:3] != '235':
	print '235 reply not received from server.'

mailFromCmd = 'MAIL FROM: <' + mail + '>' + endmsg2
clientSocket.send(mailFromCmd.encode())
recv = clientSocket.recv(1024).decode()
print recv
if recv[:3] != '250':	# if first 3 chars is not '250'
	print 'ERROR: 7 250 reply not received from server.\n'
# Fill in end
# Send RCPT TO command and print server response.
# Fill in start
cmd = ('RCPT TO: <' + mail + '>\r\n').encode()
clientSocket.send(cmd)
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '250':	# if first 3 chars is not '250'
	print '250 reply not received from server.\n'
# Fill in end
# Send DATA command and print server response.
# Fill in start
dataCommand = 'Data\r\n'
clientSocket.send(dataCommand.encode())
recv = clientSocket.recv(1024).decode()
print recv
if recv[:3] != '354':	# if first 3 chars is not '250'
	print '354 reply not received from server.\n'
# Fill in end
# Send message data.
# Fill in start

# for message
clientSocket.send(msg.encode() + endmsg.encode())
#for image
#imgFName = 'https://www.network.com.tr/assets/v2/img/Network.jpg'
#imageMsg = MIMEText('<html><body><h1>Hello</h1>' +
#					'<p><img src="'+ imgFName + '"></p>' +
#					'</body></html>', 'html', 'utf-8')
#clientSocket.send(imageMsg.as_string().encode() + endmsg.encode())
#print imageMsg.as_string().encode()


# Fill in end
# Message ends with a single period.
# Fill in start
recv = clientSocket.recv(1024).decode()
print recv
if recv[:3] != '250':	# if first 3 chars is not '250'
	print '250 reply not received from server.\n'

# Fill in end
# Send QUIT command and get server response.
# Fill in start
quitCommand = 'Quit\r\n'
clientSocket.send(quitCommand.encode())
recv = clientSocket.recv(1024).decode()
print recv
if recv[:3] != '221':	# if first 3 chars is not '250'
	print '221 reply not received from server.\n'
# Fill in end

exit()

# text and image