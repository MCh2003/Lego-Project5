from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from constants.constants import Movement, Ports
from pybricks.tools import wait
from pybricks.parameters import Stop


class DrivingUnit:
    def __init__(
        self,
        left_motor_port=Movement.MOTOR_FRONT,
        right_motor_port=Movement.MOTOR_BACK,
        wheel_diameter=Movement.WHEEL_DIAMETER,
        axle_track=Movement.AXLE_TRACK,
        brick=EV3Brick(),
    ):
        self.drive_base = DriveBase(
            Motor(left_motor_port), Motor(right_motor_port),
            wheel_diameter, axle_track
        )
        self.brick = brick

    def start_moving(self, speed=Movement.DRIVE_SPEED, degrees=0):
        self.brick.speaker.beep()
        self.drive_base.drive(speed, degrees)

    def start_moving_back_time(self, speed=Movement.DRIVE_SPEED, degrees=0, time=1000):
        print("start_moving_back_time: start")
        self.start_moving(speed=speed * -1)
        wait(time)
        self.stop_moving()
        print("start_moving_back_time: end")

    def stop_moving(self):
        self.drive_base.stop()

    def is_driving(self):
        return self.drive_base.done()
