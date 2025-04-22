from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from ..constants.constants import Movement, Ports

class DrivingUnit:
    def __init__(self, left_motor_port=Movement.MOTOR_FRONT, right_motor_port=Movement.MOTOR_BACK,
                  wheel_diameter=Movement.WHEEL_DIAMETER, axle_track=Movement.AXLE_TRACK):
        self.DriveBase(Motor(Ports.MOTOR_DRIVE_FRONT), Motor(Ports.MOTOR_DRIVE_BACK), Movement.WHEEL_DIAMETER, Movement.AXLE_TRACK)

    def startMoving(self):
        self.drive_base.drive_base.drive(1000, 0)

    def stopMoving(self):
        self.drive_base.stop()