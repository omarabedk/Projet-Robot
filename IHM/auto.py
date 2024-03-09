from PyQt5 import QtCore, QtGui, QtWidgets
import serial
from Movement import Movement

class AutoWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(AutoWindow, self).__init__()

        self.setWindowTitle("Automatic")
        self.setGeometry(100, 100, 700, 200)  # Set window size

        self.setStyleSheet("background-color: #8B4513;")

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 50, 700, 100))  # Adjust label position
        self.label.setObjectName("label")
        self.label.setText("On est en mode automatique...")

        font = QtGui.QFont()
        font.setPointSize(20)  # Set font size
        font.setBold(True)
        self.label.setFont(font)

        # Apply color to the text
        self.label.setStyleSheet("color: #FFD700;")

        self.setCentralWidget(self.centralwidget)

        # Call the auto function from the movement module
        Movement.auto(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = AutoWindow()
    window.show()
    sys.exit(app.exec_())
