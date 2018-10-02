import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

web_server = ("www.google.com", 80)

print(sock.connect(web_server))

sock.close()

