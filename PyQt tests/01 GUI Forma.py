import sys
from PyQt5 import QtWidgets,QtCore,QtGui
import numpy as np
from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

#https://matplotlib.org/3.1.1/gallery/user_interfaces/embedding_in_qt_sgskip.html
class ApplicationWindow(QtWidgets.QMainWindow):
    def enterPress(self):
        self.log.append(self.command.text())
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

        static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(static_canvas,0,1)
        self.addToolBar(NavigationToolbar(static_canvas, self))

        self.command = QtWidgets.QLineEdit()
        self.command.editingFinished.connect(self.enterPress)



        self.flo = QtWidgets.QFormLayout()
        self.flo.addRow("Comandos", self.command)
        layout.addWidget(self.command,1,0,1,2)

        im = plt.imread("../Graph tests/map.png")
        self._static_ax = static_canvas.figure.subplots()
        # t = np.linspace(0, 10, 501)
        # self._static_ax.plot(t, np.tan(t), ".")
        self._static_ax.imshow(im)



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

