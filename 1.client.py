# client.py
from socket import*
host = "192.168.0.9"
port = 65535
while 1:
	s = socket(AF_INET,SOCK_STREAM)
	s.connect((host,port))
	msg_sent = "from client"
	s.send(msg_sent.encode('UTF-8'))
	msg_recive = s.recv(50)
	print(msg_recive.decode('UTF-8'))
	s.close()
