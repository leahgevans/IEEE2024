# Raspberry Pi Motor Control Script with Two Motors and GPIO Pins

import RPi.GPIO as GPIO
import time

# Set GPIO pins for motor control
motor1_pin = 4  # GPIO pin for motor 1
motor2_pin = 5  # GPIO pin for motor 2
startup_pin = 6

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(motor1_pin, GPIO.OUT)
GPIO.setup(motor2_pin, GPIO.OUT)

def send_command(direction):
    
    direction = input("Here ya go ed: ")
    
    if direction == 'F':
        GPIO.output(motor1_pin, GPIO.HIGH)  # Forward
        GPIO.output(motor2_pin, GPIO.HIGH)  # Forward
    elif direction == 'B':
        GPIO.output(motor1_pin, GPIO.LOW)   # Backwards
        GPIO.output(motor2_pin, GPIO.LOW)
    elif direction == 'L':
        GPIO.output(motor1_pin, GPIO.HIGH)  # Left
        GPIO.output(motor2_pin, GPIO.LOW)
    elif direction == 'R':
        GPIO.output(motor1_pin, GPIO.LOW)  # Right
        GPIO.output(motor2_pin, GPIO.HIGH)
    elif direction == "Start":              
        GPIO.ouput(startup_pin, GPIO.HIGH)  # Start
    elif direction == "Brake":
        GPIO.ouput(startup_pin, GPIO.LOW)   # Brake
        
        
        
        
        
