import socket
import select
import parse
import copy
import msvcrt

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
                #print("Connection from", address)
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

class inputManager():
    def __init__(self,):
        self.msg = "";
    def new_msg(self):
        if msvcrt.kbhit():
            ch = msvcrt.getch()
            chStr = str(ch.decode('ASCII'))
            if chStr.isprintable() or chStr == "\r":
                msvcrt.putch(ch)
                self.msg = self.msg + chStr;
                if chStr == "\r":
                    return True;
        return False;
    def clear_msg(self):
        self.msg = ""
    def get_msg(self):
        retVal=copy.deepcopy(self.msg);
        msvcrt_print("SERVER WILL SEND:"+ retVal)
        self.msg = ""
        return retVal;

def is_com_valid(msg):
    return True; #TBD

class comProtocol():
    def __init__(self,):
        self.nm = networkManager(12345, 2)
        self.cmd_to_send = "";
    def new_msg(self):
        return self.nm.check_new_msgs()
    def get_msg(self):
        agv_num,msg_rec=self.nm.get_msgs()
        if self.cmd_to_send: # Al recibir un mensaje y tenía algo para enviar lo manda.
            self.nm.send_msg(agv_num,self.cmd_to_send)
        self.nm.delete_socket(agv_num)
        return msg_rec;

def msvcrt_print(str):
    l=list(str)
    msvcrt.putch(b'\n')
    for i in range(len(l)):
        msvcrt.putch(bytes([ord(l[i])]))
    msvcrt.putch(b'\n')
if __name__ == "__main__":
    input = inputManager()
    com = comProtocol()
    while 1:
        if input.new_msg():
            msg = input.get_msg();
            if is_com_valid(msg):
                com.cmd_to_send=msg;
        if com.new_msg():
             input.clear_msg()
             msvcrt_print(com.get_msg())


