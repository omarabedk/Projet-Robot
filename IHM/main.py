import csv
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Robot Controller")  # Change the window title
        self.setGeometry(100, 100, 800, 600)  # Set the window geometry (left, top, width, height)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.button_mode_manuelle = QtWidgets.QPushButton(self.centralwidget)
        self.button_mode_manuelle.setGeometry(QtCore.QRect(400, 400, 120, 40))
        self.button_mode_manuelle.setObjectName("button_mode_manuelle")
        self.button_mode_manuelle.setText("Mode Manuelle")
        self.button_mode_manuelle.clicked.connect(self.execute_ihm_file)

        self.button_mode_automatique = QtWidgets.QPushButton(self.centralwidget)
        self.button_mode_automatique.setGeometry(QtCore.QRect(200, 400, 120, 40))
        self.button_mode_automatique.setObjectName("button_mode_automatique")
        self.button_mode_automatique.setText("Mode Automatique")
        self.button_mode_automatique.clicked.connect(self.execute_auto_file)

        self.textbox_write = QtWidgets.QLineEdit(self.centralwidget)
        self.textbox_write.setGeometry(QtCore.QRect(80, 30, 200, 30))
        self.textbox_write.setObjectName("textbox_write")

        self.button_write = QtWidgets.QPushButton(self.centralwidget)
        self.button_write.setGeometry(QtCore.QRect(150, 65, 80, 30))
        self.button_write.setObjectName("button_write")
        self.button_write.setText("Write")
        self.button_write.clicked.connect(self.write_to_file)

        self.textbox_read = QtWidgets.QLineEdit(self.centralwidget)
        self.textbox_read.setGeometry(QtCore.QRect(380, 30, 200, 30))
        self.textbox_read.setObjectName("textbox_read")
        self.textbox_read.setReadOnly(True)

        self.button_read = QtWidgets.QPushButton(self.centralwidget)
        self.button_read.setGeometry(QtCore.QRect(425, 65, 80, 30))
        self.button_read.setObjectName("button_read")
        self.button_read.setText("Read")
        self.button_read.clicked.connect(self.read_from_file)

        self.setCentralWidget(self.centralwidget)

    def execute_ihm_file(self):
        os.system("python manuelle.py")  # Replace "manuelle.py" with the correct file name if needed

    def execute_auto_file(self):
        os.system("python auto.py")  # Replace "auto.py" with the correct file name if needed

    def write_to_file(self):
        text = self.textbox_write.text()
        with open("TEXT.txt", "w") as file:
            file.write(text)

    def read_from_file(self):
        with open("TEXT.txt", "r") as file:
            text = file.read()
            self.textbox_read.setText(text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())