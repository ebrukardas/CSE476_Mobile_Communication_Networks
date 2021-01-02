import sys, time
from socket import *

timeoutVal = 1
bufferSize = 1024
 
# Create UDP client socket. SOCK_DGRAM for UDP msgToSend packet
clientsocket = socket(AF_INET, SOCK_DGRAM)
# Set socket timeout
clientsocket.settimeout(timeoutVal)


# Ping for 10 times
for pingNum in range(10):

	# Meesage to sent to server
	msgToSend = b'ebru kardas'

	try:
		# Start time 
		RTT_start = time.time()

		# Send the UDP packet with the ping message (as in the server)
		clientsocket.sendto(msgToSend, ('', 12000))
		# Receive the server response
		msgToBeRcv, address = clientsocket.recvfrom(bufferSize)
		# End (Received) time
		RTT_end = time.time()

		# Response time
		totalTime = RTT_end - RTT_start
		# Server response
		print(str(pingNum+1) + '. ping: Response: ' + msgToBeRcv + '. RTT: ' + str(totalTime))

		time.sleep(1)

	except timeout:
		# Server does not response
		# cause of the packet is lost
		print(str(pingNum+1) + '. ping: Request timed out.')
	except:
		# Ups, unexpected issue happened!
		print(str(pingNum+1) + '. ping:  Unknown error!')

# After 10 pings, close socket gently
clientsocket.close()