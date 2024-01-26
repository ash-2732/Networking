import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))

s.listen(5)

while True:
    clientsocket, address = s.accept()  # any body can connect to this server
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("Welcome to the server hahaha!", "utf-8")) #utf-8 is the encoding format/byte type
    clientsocket.close()