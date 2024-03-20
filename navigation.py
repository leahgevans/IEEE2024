
import time
import arduino.py
from arduino.py import send_command

#Navigation template
#Does interactions between vision.py and arduino.py

tolerance = .02
#When a box is detected in the vision system loop, Call this function repeatedly
def centerTargetStep(xCoord, yCoord, xMax, yMax):
    #Rotate robot until target is centered, within a tolerance
    if( xCoord < xMax/2 * (1+tolerance) ):
        turnLeft()
    if( xCoord > xMax/2 * (1-tolerance) ):
        turnLeft()
    
def turnLeft():
    send_command("L")
    send_command("Start")
    time.sleep(0.1)
    send_command("Brake")

def turnRight():
    send_command("R")
    send_command("Start")
    time.sleep(0.1)
    send_command("Brake")
