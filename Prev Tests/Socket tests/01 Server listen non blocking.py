import select
import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print("My IP Address: " + ip_address)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('', 12345))
req_queue_max=10 #La máxima cantidad de AGVs
server_socket.listen(req_queue_max)
print("Listening on port 12345")

def do_other_activities():
    return 0

read_list = [server_socket]
while True:
    readable, writable, errored = select.select(read_list, [], [],0.001)
    for s in readable:
        if s is server_socket:
            client_socket, address = server_socket.accept()
            read_list.append(client_socket)
            print("Connection from", address)
        else:
            data = s.recv(1024)
            if data:
                s.send(data)
            else:
                s.close()
                read_list.remove(s)
    do_other_activities()

