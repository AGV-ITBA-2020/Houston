import sys
from PyQt5 import QtWidgets,QtCore,QtGui
import networkx as nx
import numpy as np
from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.colors as mc
from parse import *


class mapHandler():
    def __init__(self):
        self.G = nx.DiGraph()
        self.G.add_nodes_from([1, 4, 5, 6], description="Station")
        self.G.add_node(2, description="Slow down tag")
        self.G.add_node(3, description="Bifurcation", merge_node=2, fork_left_node=4)

        self.G.add_edge(1, 2, length=10)
        self.G.add_edge(2, 3, length=5)
        self.G.add_edge(3, 4, length=10)
        self.G.add_edge(3, 5, length=10)
        self.G.add_edge(4, 6, length=17)
        self.G.add_edge(5, 6, length=10)

        self.pos = {1: (0, 0), 2: (10, 0), 3: (20, 0), 4: (30, 10), 5: (30, -10), 6: (40, -10)}
        nx.draw_networkx(self.G, with_labels=True, pos=self.pos, node_color=self.gen_color())

    def get_path(self,orig,dest):
        node_path=nx.shortest_path(self.G, source=orig, target=dest,weight="length")
        descr=nx.get_node_attributes(self.G, 'description')
        merge2node = nx.get_node_attributes(self.G, 'merge_node')
        forkleftnode = nx.get_node_attributes(self.G, 'fork_left_node')
        strOut=""
        for i in range(len(node_path)): ###Falta revisar
            curr_node=node_path[i]
            if i!=0: #El primer punto es omitido en el mensaje
                if descr[curr_node] == "Station":
                    strOut += "St"
                elif descr[curr_node] == "Slow down tag":
                    strOut += "Sd"
                elif descr[curr_node] == "Speed up tag":
                    strOut += "Su"
                elif descr[curr_node] == "Bifurcation":
                    if node_path[i-1] == merge2node[curr_node]: #Viene del camino al que se va a dividir
                        if forkleftnode[curr_node] == node_path[i+1]:
                            strOut += "Fl"
                        else:
                            strOut += "Fr"
                    else:
                        strOut += "Me" #merge
        return strOut

    def gen_color(self):
        colors = []
        for n in self.G:
            d = nx.get_node_attributes(self.G, 'description')[n]
            if d == "Station":
                colors.append(mc.to_rgba('red'))
            elif d == "Slow down tag":
                colors.append(mc.to_rgba('green'))
            else:
                colors.append(mc.to_rgba('gray'))
        return colors


class ApplicationWindow(QtWidgets.QMainWindow):
    def enterPress(self):
        t=self.command.text()
        res = search("M {:d} {:d}",t)
        self.mission=self.map.get_path(res[0],res[1])
        self.log.append(self.mission)
        self.command.clear()
    def __init__(self):
        super().__init__()
        self._main = QtWidgets.QWidget()
        self.setWindowTitle('ITBAGV v0')
        self.setWindowIcon(QtGui.QIcon("AGV Icon.png"))
        self.setCentralWidget(self._main)
        layout = QtWidgets.QGridLayout(self._main)

        self.log = QtWidgets.QTextEdit()
        self.log.setReadOnly(True)
        layout.addWidget(self.log, 0, 0)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.map = mapHandler()
        self.canvas.draw_idle()

        layout.addWidget(self.canvas,0,1)
        self.addToolBar(NavigationToolbar(self.canvas, self))

        self.command = QtWidgets.QLineEdit()
        self.command.editingFinished.connect(self.enterPress)



        self.flo = QtWidgets.QFormLayout()
        self.flo.addRow("Comandos", self.command)
        layout.addWidget(self.command,1,0,1,2)




if __name__ == "__main__":
    # Check whether there is already a running QApplication (e.g., if running
    # from an IDE).
    qapp = QtWidgets.QApplication.instance()
    if not qapp:
        qapp = QtWidgets.QApplication(sys.argv)

    app = ApplicationWindow()
    app.show()
    app.activateWindow()
    app.raise_()
    qapp.exec_()

