from PyQt5.QtNetwork import *
from PyQt5.QtCore import *
import time

def communicate(msg_to_send):
    socket = QTcpSocket()
    socket.connectToHost('127.0.0.1', 12345, QIODevice.ReadWrite)
    socket.waitForConnected(100)
    socket.writeData(str.encode(msg_to_send))
    socket.flush()
    socket.waitForReadyRead(1000)
    msg_rec=str(socket.readAll())
    return msg_rec
if __name__ == '__main__':
    print(communicate("AGV ?"))
    time.sleep(10) #En este espacio se tiene que enviar una misión
    print(communicate("AGV 1\nHB"))
    time.sleep(3)
    print(communicate("AGV 1\nQuest\nYes")) # El AGV "acepta" la misión
    time.sleep(5)
    print(communicate("AGV 1\nQuest step reached"))  # El AGV avanza en la mision
    time.sleep(5)
    print(communicate("AGV 1\nQuest step reached"))  # El AGV avanza en la mision
    time.sleep(5)
    print(communicate("AGV 1\nQuest step reached"))  # El AGV avanza en la mision
