import socket
import select
import parse
import copy

class networkManager():
    def __init__(self,port,n_AGVs):
        self.n_AGVs = n_AGVs
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(('', port))
        self.server_socket.listen(self.n_AGVs)
        self.read_list = [self.server_socket]
        self.timeout_select=0.001
        self.agvs_sockets={}
        self.msgs_recieved=[]
    def check_new_msgs(self):

        retVal=0;
        readable, writable, _ = select.select(self.read_list, [], [], self.timeout_select)
        for s in readable:
            if s is self.server_socket:
                client_socket, address = self.server_socket.accept()
                self.read_list.append(client_socket)
                print("Connection from", address)
            else:
                retVal=1
                data_recieved = repr(s.recv(1024))
                data_recieved = data_recieved.split('\n', 1) #Me quedo con el header del agv
                header = data_recieved[0]
                data_recieved = data_recieved[1]
                AGV_number = int(parse.parse("AGV {}\n", header))
                return_msg = (AGV_number, data_recieved)
                self.msgs_recieved.append(return_msg)
                self.agvs_sockets[AGV_number] = s
        return retVal
    def get_msgs(self):
        retVal=copy.deepcopy(self.msgs_recieved)
        self.msgs_recieved=[]
        return retVal;

    def send_msg(self,AGV_number,msg):
        agv_socket = self.agvs_sockets[AGV_number]
        agv_socket.sendall(msg)
    def delete_socket(self,AGV_number):
        agv_socket = self.agvs_sockets[AGV_number]
        agv_socket.close()
        self.read_list.remove(agv_socket)
        del self.agvs_sockets['key']

if __name__ == "__main__":
    nm=networkManager(12345, 2)
    while 1:
        if nm.check_new_msgs():
            msgs=nm.get_msgs()
            msg_2_send=input()
            nm.send_msg(msgs[0], msg_2_send)

