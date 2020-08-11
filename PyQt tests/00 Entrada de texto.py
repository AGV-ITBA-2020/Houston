import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QFormLayout


#https://matplotlib.org/3.1.1/gallery/user_interfaces/embedding_in_qt_sgskip.html
class myGUI:
    def enterPress(self):
        print(self.command.text())
        self.command.clear()
    def __init__(self):
        app = QApplication(sys.argv)

        self.win = QWidget()
        self.win.resize(1000, 800)

        self.command = QLineEdit()
        self.command.editingFinished.connect(self.enterPress)

        self.flo = QFormLayout()
        self.flo.addRow("Comandos", self.command)
        self.win.setLayout(self.flo)
        self.win.setWindowTitle('ITBAGV v0')
        self.win.show()
        sys.exit(app.exec_())


def main():
    gui=myGUI();



if __name__ == '__main__':
    main()