from PyQt5.QtNetwork import *
from parse import *

class NetworkManager:
    def __init__(self):
        self.server = QTcpServer() ##Crea server TCP
        self.port=12345
        self.server.listen(QHostAddress("0.0.0.0"), self.port) #Escucha al que quiera conectarse por el puerto 12345
        self.server.newConnection.connect(self.on_new_connection) ##En caso de conexión, se llamará a este callback
        self.nxt_AGV_num=1 #El numero que le da al nuevo agv que se quiera unir
        self.msgs_to_send = {}
    def set_read_callback(self,callback):
        self.callback=callback
    def set_new_agv_callback(self, callback):
            self.new_agv_callback = callback
    def on_new_connection(self):
        print("Connected")
        self.clientConnection = self.server.nextPendingConnection()
        self.clientConnection.readyRead.connect(self.read)
    def has_msgs_pending(self,agvN): ##Dice si tiene mensajes pendientes para enviar a este agv
        return agvN in self.msgs_to_send
    def send(self,agvNumber,msg):
        self.msgs_to_send[agvNumber]=msg;
    def read(self):
        instr = self.clientConnection.readAll()
        msg=str(instr, encoding='ascii')
        if msg.find("AGV ?") != -1: ##En el caso de que sea un agv nuevo conectandose y pidiendo su número, respuesta automática.
            string = str(self.nxt_AGV_num)
            self.clientConnection.writeData(str.encode(string))
            self.clientConnection.flush()
            self.new_agv_callback(self.nxt_AGV_num)
            self.nxt_AGV_num=self.nxt_AGV_num+1
        else:
            data_recieved = msg.split('\n', 1)  # Me quedo con el header del agv
            header = data_recieved[0]
            msg = data_recieved[1]
            AGV_number = int(parse("AGV {}", header)[0])
            self.callback(AGV_number,msg)
            if AGV_number in self.msgs_to_send: #Si tiene mensajes para ese agv
                msg = self.msgs_to_send[AGV_number]
                self.clientConnection.writeData(str.encode(msg))
                self.clientConnection.flush()
                del self.msgs_to_send[AGV_number] #Borro ese mensaje porque ya lo envié
        self.clientConnection.disconnectFromHost()