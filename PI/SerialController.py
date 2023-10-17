import serial

class Arduino:
    def __init__(self, port, baud = 9600):
        self.port = port
        self.ser = serial.Serial(port,baud)

    def send_message(self, message: str):
        self.ser.write(message.encode())

    def read_message(self) -> list:
        return self.ser.readline()
        