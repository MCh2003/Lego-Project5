from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

class DrivingUnit:
    def __init__(self):
        robot = DriveBase(Motor(Port.C), Motor(Port.D), wheel_diameter=55.5, axle_track=104)


    def startMoving(self):
        robot.straight(1000)
    
    
