# first of all import the socket library
import socket


hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print("My IP Address: " + ip_address) #Esta IP no está bien
# next create a socket object
s = socket.socket()
print("Socket successfully created")
port = 12345

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('0.0.0.0', port))
print("socket binded to %s" % (port))

# put the socket into listening mode
s.listen(60)
print("socket is listening")

# Establish connection with client.
c, addr = s.accept()

print ('Got connection from', addr)
msg=c.recv(1024)
# send a thank you message to the client.
c.sendall(b'Thank you for connecting')

# Close the connection with the client
c.close()
print ('Client Msg:', msg)