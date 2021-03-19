from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
import sys
import os




class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('app.ui', self)
        self.show()
        self.pushButton.clicked.connect(self.logs)
        self.pushButton_2.clicked.connect(self.sair)
        self.progressBar.setRange(0, 100)
        self.show()

    def logs(self):
        self.progressBar.setValue(40)
        self.label_loading.setText("loading...")
        os.system(r"del /q C:\Windows\Temp\*")
        self.progressBar.setValue(60)
        os.system(r"del /q C:\Users\%username%\AppData\Local\Temp\*")
        self.progressBar.setValue(80)
        os.system(r"del /q C:\Windows\Prefetch\*")
        self.progressBar.setValue(90)
        os.system(r"del /q C:\Users\kauan\AppData\Local\Google\Chrome\User Data\Default\Cache\*")
        self.progressBar.setValue(100)
        os.system(r"rd /S /Q c:\$Recycle.bin")
        self.progressBar.setValue(100)
        self.label_descriao.setText("<strong>JA</strong> ACABOU!")

    def sair(self):
        exit()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())
