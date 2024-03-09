from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QShortcut
import serial
from Movement import Movement
import keyboard



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 431)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        MainWindow.setStyleSheet("background-color: #8B4513;")  # Set the background color to brown

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 160, 75, 75))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("""
            QPushButton {
                font-size: 24px;
                background-color: #FFD700;
                border-style: outset;
                border-width: 2px;
                border-radius: 37px;
                border-color: beige;
                padding: 4px;
            }
            QPushButton:pressed {
                background-color: #FFA500;
                border-style: inset;
            }
        """)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 160, 75, 75))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("""
            QPushButton {
                font-size: 24px;
                background-color: #FFD700;
                border-style: outset;
                border-width: 2px;
                border-radius: 37px;
                border-color: beige;
                padding: 4px;
            }
            QPushButton:pressed {
                background-color: #FFA500;
                border-style: inset;
            }
        """)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 230, 75, 75))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet("""
            QPushButton {
                font-size: 24px;
                background-color: #FFD700;
                border-style: outset;
                border-width: 2px;
                border-radius: 37px;
                border-color: beige;
                padding: 4px;
            }
            QPushButton:pressed {
                background-color: #FFA500;
                border-style: inset;
            }
        """)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 90, 75, 75))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("""
            QPushButton {
                font-size: 24px;
                background-color: #FFD700;
                border-style: outset;
                border-width: 2px;
                border-radius: 37px;
                border-color: beige;
                padding: 4px;
            }
            QPushButton:pressed {
                background-color: #FFA500;
                border-style: inset;
            }
        """)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(160, 230, 75, 75))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet("""
            QPushButton {
                font-size: 24px;
                background-color: #FFD700;
                border-style: outset;
                border-width: 2px;
                border-radius: 37px;
                border-color: beige;
                padding: 4px;
            }
            QPushButton:pressed {
                background-color: #FFA500;
                border-style: inset;
            }
        """)

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(480, 230, 75, 75))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setStyleSheet("""
            QPushButton {
                font-size: 24px;
                background-color: #FFD700;
                border-style: outset;
                border-width: 2px;
                border-radius: 37px;
                border-color: beige;
                padding: 4px;
            }
            QPushButton:pressed {
                background-color: #FFA500;
                border-style: inset;
            }
        """)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton_5.pressed.connect(Movement.gauchearriere)
        self.pushButton_5.released.connect(Movement.stop)
        self.pushButton_6.pressed.connect(Movement.droitearriere)
        self.pushButton_6.released.connect(Movement.stop)
        self.pushButton.pressed.connect(Movement.avancer)
        self.pushButton.released.connect(Movement.stop)
        self.pushButton_4.pressed.connect(Movement.reculer)
        self.pushButton_4.released.connect(Movement.stop)
        self.pushButton_2.pressed.connect(Movement.gaucheavant)
        self.pushButton_2.released.connect(Movement.stop)
        self.pushButton_3.pressed.connect(Movement.droiteavant)
        self.pushButton_3.released.connect(Movement.stop)

        keyboard.on_press_key('up', lambda event: Movement.avancer())
        keyboard.on_release_key('up', lambda event: Movement.stop())

        keyboard.on_press_key('down', lambda event: Movement.reculer())
        keyboard.on_release_key('down', lambda event: Movement.stop())

        keyboard.on_press_key('up', lambda event: Movement.droiteavant() if keyboard.is_pressed('right') else Movement.gaucheavant() if keyboard.is_pressed('left') else Movement.avancerrapide() if keyboard.is_pressed('shift') else None)
        keyboard.on_press_key('right', lambda event: Movement.droiteavant() if keyboard.is_pressed('up') else Movement.droitearriere() if keyboard.is_pressed('down') else None)
        keyboard.on_release_key('right', lambda event: Movement.avancer() if keyboard.is_pressed('up') else Movement.reculer() if keyboard.is_pressed('down') else None)
        keyboard.on_press_key('left', lambda event: Movement.gaucheavant() if keyboard.is_pressed('up') else Movement.gauchearriere() if keyboard.is_pressed('down') else None)
        keyboard.on_release_key('left', lambda event: Movement.avancer() if keyboard.is_pressed('up') else Movement.reculer() if keyboard.is_pressed('down') else None)
        keyboard.on_release_key('up', lambda event: Movement.stop())
        keyboard.on_press_key('down', lambda event: Movement.droitearriere() if keyboard.is_pressed('right') else Movement.gauchearriere() if keyboard.is_pressed('left') else Movement.reculerrapide() if keyboard.is_pressed('shift') else None)
        keyboard.on_release_key('down', lambda event: Movement.stop())
        keyboard.on_press_key('shift', lambda event: Movement.avancerrapide() if keyboard.is_pressed('up') else Movement.reculerrapide() if keyboard.is_pressed('down') else None)
        keyboard.on_release_key('shift', lambda event: Movement.avancer() if keyboard.is_pressed('up') else Movement.reculer() if keyboard.is_pressed('down') else None)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Manual Mode"))
        self.pushButton_2.setText(_translate("MainWindow", " ⇦"))
        self.pushButton_3.setText(_translate("MainWindow", "⇨"))
        self.pushButton_4.setText(_translate("MainWindow", "⇩"))
        self.pushButton.setText(_translate("MainWindow", "⇧"))
        self.pushButton_5.setText(_translate("MainWindow", "⇦⇩"))
        self.pushButton_6.setText(_translate("MainWindow", "⇨⇩"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
