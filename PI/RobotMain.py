import ImgRec as Image
import SerialController as Arduino
import RPi.GPIO as GPIO
import time

port = 0 # change this to be the serial port for arduino
arduino = Arduino(port)

def moveRobot(direction, cm):
    if direction == "left":
        letter = "l"
    if direction == "right":
        letter = "r"
    if direction == "forward":
        letter = "f"
    if direction == "backward":
        letter = "b"
    else:
        return "Direction " + direction + " not valid"
    
    string = letter + cm
    arduino.send_message(string)
        
# while True:
#     if(Image.isDetectingBox()):
#         print("Detected box!")
#     else:
#         print("NO BOX")

 

