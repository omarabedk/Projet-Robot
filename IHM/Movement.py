import serial

class Movement:
    @staticmethod
    def avancer():
        ser = serial.Serial('COM15', 115200)
        data = b'\x62'
        ser.write(data)
        ser.close()
    
    def auto(self):
        ser = serial.Serial('COM15', 115200)
        data = b'\x77'
        ser.write(data)
        ser.close()

    @staticmethod
    def avancerrapide():
        ser = serial.Serial('COM15', 115200)
        data = b'\x6C'
        ser.write(data)
        ser.close()

    @staticmethod
    def reculer():
        ser = serial.Serial('COM15', 115200)
        data = b'\x72'
        ser.write(data)
        ser.close()

    @staticmethod
    def reculerrapide():
        ser = serial.Serial('COM15', 115200)
        data = b'\x63'
        ser.write(data)
        ser.close()

    @staticmethod
    def stop():
        ser = serial.Serial('COM15', 115200)
        data = b'\x73'
        ser.write(data)
        ser.close()

    @staticmethod
    def gaucheavant():
        ser = serial.Serial('COM15', 115200)
        data = b'\x74'
        ser.write(data)
        ser.close()

    @staticmethod
    def droiteavant():
        ser = serial.Serial('COM15', 115200)
        data = b'\x64'
        ser.write(data)
        ser.close()

    @staticmethod
    def gauchearriere():
        ser = serial.Serial('COM15', 115200)
        data = b'\x61'
        ser.write(data)
        ser.close()

    @staticmethod
    def droitearriere():
        ser = serial.Serial('COM15', 115200)
        data = b'\x79'
        ser.write(data)
        ser.close()
