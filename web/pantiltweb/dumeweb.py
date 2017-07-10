#!/usr/bin/env python
import uArmRobot
import time
import pantilthat
from sys import exit

serialport = "/dev/ttyACM0"  # for linux like system
myRobot = uArmRobot.robot(serialport)

try:
    from flask import Flask, render_template
except ImportError:
    exit("This script requires the flask module\nInstall with: sudo pip install flask")


myRobot.debug = True   # Enable / Disable debug output on screen, by default disabled
myRobot.connect()
myRobot.mode(0)   # Set mode to Normal
app = Flask(__name__)
speed = 3000

time.sleep(1)
myRobot.goto(200,0,100,6000)

@app.route('/')
def home():
    return render_template('gui.html')

@app.route('/api/<direction>/<int:angle>')
def api(direction, angle):
    if angle < 0 or angle > 180:
        return "{'error':'out of range'}"

    angle -= 90

    if direction == 'left':
        myRobot.gotorel(0,angle,0,speed)
        return "{{'moving':{}}}".format(angle)

    elif direction == 'right':
         myRobot.gotorel(0,-angle,0,speed)
        return "{{'moving':{}}}".format(angle)

    elif direction == 'up':
        myRobot.gotorel(0,0,angle,speed)
        return "{{'moving':{}}}".format(angle)

    elif direction == 'down':
        myRobot.gotorel(0,0,-angle,speed)
        return "{{'moving':{}}}".format(angle)

    elif direction == 'forward':
        myRobot.gotorel(angle,0,0,speed)
        return "{{'moving':{}}}".format(angle)

    elif direction == 'back':
        myRobot.gotorel(-angle,0,0,speed)
        return "{{'moving':{}}}".format(angle)        

    return "{'error':'invalid direction'}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9595, debug=True)
