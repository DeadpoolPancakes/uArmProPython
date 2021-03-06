# uArm Swift Pro - Python Library Example
# Created by: Richard Garsthagen - the.anykey@gmail.com
# V0.1 - June 2017 - Still under development

import uArmRobot
import time

#Configure Serial Port
#serialport = "com3"          # for windows 
serialport = "/dev/ttyACM0"  # for linux like system

# Connect to uArm 
myRobot = uArmRobot.robot(serialport)
myRobot.debug = False   # Enable / Disable debug output on screen, by default disabled
myRobot.connect()
myRobot.mode(0)   # Set mode to Normal

time.sleep(1)

# Move robot, command will complete when motion is completed
myRobot.goto(200,0,100,6000)
time.sleep(2)
myRobot.goto(100,50,200,6000)
time.sleep(2)
myRobot.goto(0,0,0,3000)
time.sleep(1)
# Turn on the pump
myRobot.gripper(True)
time.sleep(3)
myRobot.gripper(False)

# Send move command, but continue program
#myRobot.async_goto(200,150,250,3000)
#while myRobot.moving:
#    print ("Waiting to complete move")
#    time.sleep(0.5)

#Turn off the pump
#myRobot.pump(False)

# Send move command, but continue program
#myRobot.async_goto(200,0,100,6000)
#while myRobot.moving:
#    print ("Waiting to complete move")
#    time.sleep(0.5)


time.sleep(5)

#Disconnect serial connection
#myRobot.disconnect()




