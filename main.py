from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMainWindow
from PyQt5.QtGui import QPixmap
import gui
import sys

class MainWindow(gui.Ui_Dialog, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.LEDONBTN.clicked.connect(self.ledon)
        self.LEDOFFBTN.clicked.connect(self.ledoff)
        qpixmap = QPixmap('GREEN_LED.png')
        self.GREEN_LED.setPixmap(qpixmap)
        self.GREEN_LED.setEnabled(False)


    def ledon(self):
        self.GREEN_LED.setEnabled(True)

    def ledoff(self):
        self.GREEN_LED.setEnabled(False)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()