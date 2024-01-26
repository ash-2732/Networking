import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))  # connect to the server

msg = s.recv(1024) # 1024 is the buffer size
print(msg.decode("utf-8")) # decode the message from the server