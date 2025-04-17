from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from ..constants.constants import Movement

class DrivingUnit:
    def __init__(self, left_motor_port=Movement.MOTOR_LEFT, right_motor_port=Movement.MOTOR_RIGHT,
                  wheel_diameter=Movement.WHEEL_DIAMETER, axle_track=Movement.AXLE_TRACK):
        self.robot = DriveBase(Motor(left_motor_port), Motor(right_motor_port), wheel_diameter, axle_track)

    def startMoving(self):
        self.robot.straight(1000)