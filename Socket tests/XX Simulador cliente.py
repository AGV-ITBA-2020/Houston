import socket

s = socket.socket();

s.connect(('loopback',12345))
print('Conecté')

s.sendall(b'AGV 1\nHB\n')


data = s.recv(1024)
print('Recibí: ', repr(data))

s.sendall(b'AGV 1\nACK\n')

s.close()