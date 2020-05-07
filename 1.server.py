from socket import*
# import socket from socket 
# alternative method 
# import socket 1.0
host="192.168.0.9"
# our local host also loop back address
port=65535
s = socket(AF_INET,SOCK_STREAM)
# s = var name
# AF_INET = ip4 interface 
# SOCK_STREAM = choose tcp protocol
s.bind((host,port))
s.listen(10)
while 1:
	c,addr = s.accept()
	print("got  connecton from  =  ",addr)
	recive_messge = c.recv(50)
	# 50 data packet can be sent
	print(recive_messge.decode('UTF-8'))
	sent_messge = raw_input("send data to client:")
	c.send(sent_messge.encode('UTF-8'))
	c.close()
