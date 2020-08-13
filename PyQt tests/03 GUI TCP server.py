#https://stackoverflow.com/questions/9355511/pyqt-qtcpserver-how-to-return-data-to-multiple-clients

import sys,time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QFormLayout, QPushButton
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *

class EmulatedClient:
    def __init__(self):
        self.socket = QTcpSocket()

        self.makeRequest()
        self.socket.waitForConnected(1000)

        self.socket.writeData(b'Hello') #Esto parecería no llegar ...
        self.socket.flush()



    def makeRequest(self):
        HOST = '127.0.0.1'
        PORT = 12345
        self.socket.connectToHost(HOST, PORT, QIODevice.ReadWrite)



class NetworkManager:
    def __init__(self):
        self.server = QTcpServer()
        self.port=12345
        self.server.listen(QHostAddress("0.0.0.0"), self.port)
        self.server.newConnection.connect(self.on_new_connection)


    def on_new_connection(self):
        print("Connected")
        self.clientConnection = self.server.nextPendingConnection()
        self.clientConnection.readyRead.connect(self.read)

    def read(self):
        instr = self.clientConnection.readAll()
        print(str(instr, encoding='ascii'))
        self.clientConnection.writeData(b'Hola')
        self.clientConnection.flush()
        self.clientConnection.disconnectFromHost()


class myGUI:
    def sendClientReq(self):
        client = EmulatedClient()
    def __init__(self):
        app = QApplication(sys.argv)
        self.nm=NetworkManager()
        self.win = QWidget()
        self.win.resize(1000, 800)

        self.command = QLineEdit()
        self.flo = QFormLayout()
        self.flo.addRow("Comandos", self.command)

        self.but = QPushButton()
        self.but.clicked.connect(self.sendClientReq)

        self.flo.addRow("Presione para enviar", self.but)
        self.win.setLayout(self.flo)
        self.win.setWindowTitle('ITBAGV v0')
        self.win.show()
        sys.exit(app.exec_())


def main():
    gui=myGUI();



if __name__ == '__main__':
    main()