all: p1 

# 192.168.207.1:6789/HelloWorld.html
p1: webServer.py
	python webServer.py

p2_server: UDPPingerServer.py
	python UDPPingerServer.py

p2_client: UDPPingerClient.py
	python UDPPingerClient.py

p3: mailClient.py
	python mailClient.py

d: deneme3.py
	python deneme3.py