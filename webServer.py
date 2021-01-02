from socket import *

#Prepare a server socket (for UTP)
serverSocket = socket(AF_INET, SOCK_STREAM)

#Fill in start
bufferSize = 1024
serverSocket.bind(('', 6789))

# listen one client each time
serverSocket.listen(1)

#Fill in end

while True:
	#Establish the connection
	print("Ready to serve...")

	#Accept the -one and only- client
	connectionSocket, addr = serverSocket.accept() #Fill in start #Fill in end

	try:

		message = connectionSocket.recv(bufferSize)

		#Fill in start

		# Print the message from client
		print(message)
		
		#Fill in end

		filename = message.split()[1]
		f = open(filename[1:])

		# Prepare the message to send
		outputdata = f.read() #Fill in start	#Fill in end

		#Send one HTTP header line into socket

		#Fill in start

		# Send to client that found
		connectionSocket.send("\nHTTP/1.x 200 OK\r\n\r\n")

		#Fill in end

		#Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i])
		connectionSocket.close()
	except IOError:
		#Send response message for file not found

		#Fill in start

		print("404 NOT FOUND")
		# Typical ups 404 not found error

		connectionSocket.send("\nHTTP/1.x 404 Not Found\r\n\r\n")
		connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")

		#Fill in end

		#Close client socket

		#Fill in start
		connectionSocket.close()
		#Fill in end
	except:

		print("Ups another issue happened")
		connectionSocket.close()


# 127.0.0.1:6789/HelloWorld.html
