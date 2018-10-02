import socket, sys, optparse

parser = optparse.OptionParser()

parser.add_option("-s", "--server", default="localhost", dest="server", 
help="server adress",metavar = "SERVER")

parser.add_option("-p", "--port", dest="port",
help="port number", type='int', metavar = "PORT")

parser.add_option("-m", "--message", dest="message",
help="message", metavar = "MESSAGE")

(options, args) = parser.parse_args()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
svr_addr = (options.server, options.port)
sock.connect(svr_addr)


try:
	sock.sendall(options.message.encode("utf-8"))
	data = sock.recv(32)
	print("Client Received message: "+str(data.decode("utf-8")))
	
finally:
	sock.close()
