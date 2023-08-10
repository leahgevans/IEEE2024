'''
Pi Motor Controlling code here

use pins
'''
import time
import RPi.GPIO as GPIO
import math

#north is 0, east is 90, south is 180, west is 270

#coordinates might not be exact  

#current_y = 30.48
current_y = 8.6
current_x = 121.92
current_direction = 0

#recycle center 1 is one by starting point
recycle_center1_x = 200.66
recycle_center1_y = 11.43
recycle_center2_x = 200.66
recycle_center2_y = 105.41

redzone_x = 11.43
redzone_y = 15.24
greenzone_x = 11.43
greenzone_y = 104.14

#coordinates of duck pond is the center of inner circle
duckpond_x = 119.38
duckpond_y = 60.96

class Motor:
    def __init__(self, dirPin, stepPin):
        self.dirPin = dirPin
        self.stepPin = stepPin

        
    def forward(self, steps):
        GPIO.output(self.dirPin, GPIO.LOW)
        for i in range (int(steps)):
            #self.stepPin = True
            print("forward motor")
            GPIO.output(self.stepPin, GPIO.LOW)
            start = time.time()
            while(time.time() - start <0.005):
                pass
            GPIO.output(self.stepPin, GPIO.HIGH)
            #time.sleep(1000)
            start = time.time()
            while(time.time() - start <0.005):
                pass

    def backward(self,steps):
        GPIO.output(self.dirPin, GPIO.HIGH)
        for i in range (steps):
            #self.stepPin = True
            print("forward motor")
            GPIO.output(self.stepPin, GPIO.HIGH)
            start = time.time()
            while(time.time() - start <0.005):
                pass
            GPIO.output(self.stepPin, GPIO.LOW)
            #time.sleep(1000)
            start = time.time()
            while(time.time() - start <0.005):
                pass

class Servo:
    
    def __init__(self, pin, minimum=2, maximum=12):
        #self.position =position
        self.servopin = pin
        self.minimum = minimum
        self.maximum = maximum
        
        GPIO.setup(pin, GPIO.OUT)
       # GPIO.setup(servo1, GPIO.OUT)
        self.servo = GPIO.PWM(pin, 50)
        self.servo.start(0);
        
    def setpos(self, pos):
        #middle is 7.5
        if pos < self.minimum:
            self.servo.ChangeDutyCycle(self.minimum)
        elif pos > self.maximum:
            self.servo.ChangeDutyCycle(self.maximum)
        else:
            self.servo.ChangeDutyCycle(pos)
      #  pi_pwm = GPIO.PWM(pin, position)
      #  pi_pwm.start(0)
      #  sleep(.05)
      #  pi_pwm.stop()
        
 #   def setpos(self, position):
 #       self.position = position
        
class RobotControl:
    leftMotors = []
    rightMotors = []
    otherMotors = []
    servos = []
    

    def __init__(self, lefts, rights):
        self.leftMotors = lefts
        self.rightMotors = rights

    def left(self, steps):
        for motor in self.leftMotors:
            GPIO.output(motor.dirPin, GPIO.HIGH)
            
        for motor in self.rightMotors:
            GPIO.output(motor.dirPin, GPIO.LOW)
            
        for i in range (int(steps)):
            #self.stepPin = True
            print("right motor")
            for motor in self.leftMotors:
                GPIO.output(motor.stepPin, GPIO.LOW)
                
            for motor in self.rightMotors:
                GPIO.output(motor.stepPin, GPIO.LOW)
                
            start = time.time()
            while(time.time() - start <0.005):
                pass
            for motor in self.leftMotors:
                GPIO.output(motor.stepPin, GPIO.HIGH)
                
            for motor in self.rightMotors:
                GPIO.output(motor.stepPin, GPIO.HIGH)
            #time.sleep(1000)
            start = time.time()
            while(time.time() - start <0.005):
                pass

            #this code is assuming that we only turn 90 degrees
            current_direction = current_direction - 90
            if current_direction < 0:
                current_direction = current_direction + 360
            
    def right(self, steps):
        for motor in self.leftMotors:
            GPIO.output(motor.dirPin, GPIO.LOW)
            
        for motor in self.rightMotors:
            GPIO.output(motor.dirPin, GPIO.HIGH)
            
        for i in range (int(steps)):
            #self.stepPin = True
            print("left im motor")
            for motor in self.leftMotors:
                GPIO.output(motor.stepPin, GPIO.LOW)
                
            for motor in self.rightMotors:
                GPIO.output(motor.stepPin, GPIO.LOW)
                
            start = time.time()
            while(time.time() - start <0.005):
                pass
            for motor in self.leftMotors:
                GPIO.output(motor.stepPin, GPIO.HIGH)
                
            for motor in self.rightMotors:
                GPIO.output(motor.stepPin, GPIO.HIGH)
            #time.sleep(1000)
            start = time.time()
            while(time.time() - start <0.005):
                pass
    
            #this code is assuming that we only turn 90 degrees
            current_direction = current_direction + 90
            if current_direction >= 360:
                current_direction = 0
                
    def backwards(self, steps):
        for motor in self.leftMotors:
            GPIO.output(motor.dirPin, GPIO.HIGH)
            
        for motor in self.rightMotors:
            GPIO.output(motor.dirPin, GPIO.HIGH)
            
        for i in range (int(steps)):
            #self.stepPin = True
            print("backward motor")
            for motor in self.leftMotors:
                GPIO.output(motor.stepPin, GPIO.LOW)
                
            for motor in self.rightMotors:
                GPIO.output(motor.stepPin, GPIO.LOW)
                
            start = time.time()
            while(time.time() - start <0.005):
                pass
            for motor in self.leftMotors:
                GPIO.output(motor.stepPin, GPIO.HIGH)
                
            for motor in self.rightMotors:
                GPIO.output(motor.stepPin, GPIO.HIGH)
            #time.sleep(1000)
            start = time.time()
            while(time.time() - start <0.005):
                pass
            
            #update coordinates
            cm = steps / (20/math.pi)
            if current_direction == 0:
                current_y = current_y - cm
            if current_direction == 90:
                current_x = current_x - cm
            if current_direction == 180:
                current_y = current_y + cm
            if current_direction == 270:
                current_x = current_x + cm
                
            
    def forward (self, steps):
        for motor in self.leftMotors:
            GPIO.output(motor.dirPin, GPIO.LOW)
            
        for motor in self.rightMotors:
            GPIO.output(motor.dirPin, GPIO.LOW)
            
        for i in range (int(steps)):
            #self.stepPin = True
            print("forward motor")
            for motor in self.leftMotors:
                GPIO.output(motor.stepPin, GPIO.LOW)
                
            for motor in self.rightMotors:
                GPIO.output(motor.stepPin, GPIO.LOW)
                
            start = time.time()
            while(time.time() - start <0.005):
                pass
            for motor in self.leftMotors:
                GPIO.output(motor.stepPin, GPIO.HIGH)
                
            for motor in self.rightMotors:
                GPIO.output(motor.stepPin, GPIO.HIGH)
            #time.sleep(1000)
            start = time.time()
            while(time.time() - start <0.005):
                pass
            
            cm = steps / (20/math.pi)
            if current_direction == 0:
                current_y = current_y + cm
            if current_direction == 90:
                current_x = current_x + cm
            if current_direction == 180:
                current_y = current_y - cm
            if current_direction == 270:
                current_x = current_x - cm
        
def getSteps(cm):
    #one turn (360 degrees) == 83 cm
    steps = cm * (20 / math.pi)
    return steps
#200 = 1 rotation
#wheel circumference: 100*pi mm
#10 cm = 200/pi

def getStepsPerAngle(theta):
    steps = getSteps(theta / 4.63)
    return steps

def goToPlace(robot, x_coor, y_coor):
    x_dist = x_coor - current_x
    y_dist = y_coor - current_y
    
    if x_dist > 0 :
        #go to the right
        robot.right(getStepsPerAngle(90))
        robot.forward(getSteps(x_dist))
    if x_dist < 0:
        #go to the left
        robot.left(getStepsPerAngle(90))
        robot.forward(getSteps(x_dist))
    if y_dist > 0:
        #go up
        robot.forward(getSteps(y_dist))
    if y_dist < 0:
        #go down
        robot.right(180)
        robot.forward(getSteps(y_dist))
    
# steps = getSteps(83)
# print(steps)
# step = 13
# rightdir = 11
# leftStep = 31
# leftDir = 18
servo1 = 32
servo2 = 35
servo3 = 33
servo4 = 12
GPIO.setmode(GPIO.BOARD)
# GPIO.setup(step, GPIO.OUT)
# GPIO.setup(rightdir, GPIO.OUT)
# GPIO.setup(leftStep, GPIO.OUT)
# GPIO.setup(leftDir, GPIO.OUT)

# rightMotor = Motor(rightdir, step)
# rightMotor.forward(steps)
# leftMotor = Motor(leftDir, leftStep)
# leftMotor.forward(steps)

# lefts = [leftMotor]
# rights = [rightMotor]
# RC = RobotControl(lefts, rights)
# RC.forward(steps)
# RC.left(steps)
# RC.left(steps)

# testing servo
# servo_one = Servo(servo1)
# servo_two = Servo(servo2)
# servo_three = Servo(servo3)
# servo_four = Servo(servo4)

# servo_one.setpos(12)
# time.sleep(5)
# servo_one.setpos(2)
# time.sleep(5)
# servo_two.setpos(12)
# time.sleep(5)
# servo_four.setpos(12)
# time.sleep(5)
# servo_three.setpos(12)
# time.sleep(5)



#GPIO.setup(servo1, GPIO.OUT)
#servo = GPIO.PWM(servo1, 50)
#servo.start(0);
#print("waiting for 1 second")
#time.sleep(1)
#servo.ChangeDutyCycle(12)
#time.sleep(2)
#print("Rotaing at intervals of 12 degrees")
#duty =2
#while duty <= 17:
 #   servo.ChangeDutyCycle(duty)
 #   time.sleep(1)
 #   duty = duty+1
#print("Turning back to 0 degrees")
#servo.ChangeDutyCycle(2)
#time.sleep(2)
#servo.ChangeDutyCycle(0)
#servo.stop()
# duration = 30 #seconds
# now = time.time()
# while(time.time() < now+duration):
#     motor.forward()
    #GPIO.output(dir, GPIO.HIGH)

# motor.stepsPerRevolution = -200
# now = time.time()
# while(time.time() < now + duration):
#     motor.forward()



steps = getSteps(31.4)
print(steps)
rightStep = 31
rightdir = 18
leftStep = 13
leftDir = 15
GPIO.setmode(GPIO.BOARD)
GPIO.setup(rightStep, GPIO.OUT)
GPIO.setup(rightdir, GPIO.OUT)
GPIO.setup(leftStep, GPIO.OUT)
GPIO.setup(leftDir, GPIO.OUT)
# 
rightMotor = Motor(rightdir, rightStep)
rightMotor.forward(steps)
time.sleep(2)
leftMotor = Motor(leftDir, leftStep)
leftMotor.forward(steps)

lefts = [leftMotor]
rights = [rightMotor]
RC = RobotControl(lefts, rights)

#time.sleep(40)
#goToPlace(RC, 185.42, 93.98)

#testing sensor  
    
sensorL = 16
sensorR = 11
sensorF = 37
GPIO.setup(sensorL,GPIO.IN)
GPIO.setup(sensorR,GPIO.IN)
GPIO.setup(sensorF,GPIO.IN)
# 
# rightMotor = Motor(dir, step)
# leftMotor = Motor(leftDir, leftStep)
#
#motor = Motor(dir, step)
#duration = 30 #seconds
#now = time.time()
#while(time.time() < now+duration):
#    motor.forward()
#    GPIO.output(dir, GPIO.HIGH)

#motor.stepsPerRevolution = -200
#now = time.time()
#while(time.time() < now + duration):
#    motor.forward()

# #set the behaviour of led as output
#

# while True:
#     RC.right(getStepsPerAngle(45))
#     RC.forward(getSteps(89.8))
#     RC.left(getStepsPerAngle(135))
#     RC.forward(getSteps(127))
#     RC.left(getStepsPerAngle(135))
#     RC.forward(getSteps(89.8))
#     RC.left(getStepsPerAngle(90))
#     time.sleep(20)

# DON'T GET RID OF THIS!!!
# while True:
#     if (not GPIO.input(sensorL) and not GPIO.input(sensorR)) or not GPIO.input(sensorF):
#         RC.backwards(getSteps(10))
#         print("backward")
#     elif (not GPIO.input(sensorL)):
#         RC.right(getStepsPerAngle(15))
#         print("right")
#     elif (not GPIO.input(sensorR)):
#         RC.left(getStepsPerAngle(15))
#         print("left")
#     else:
#         RC.forward(getSteps(2.5))
#         print("forward")
#  
#     for i in range (0,10000):
#         pass

GPIO.cleanup()