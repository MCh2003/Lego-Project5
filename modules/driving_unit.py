from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from constants.constants import Movement, Ports
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Stop
from modules.robot import Robot


class DrivingUnit:
    def __init__(
        self,
        left_motor_port=Movement.MOTOR_FRONT,
        right_motor_port=Movement.MOTOR_BACK,
        wheel_diameter=Movement.WHEEL_DIAMETER,
        axle_track=Movement.AXLE_TRACK,
        robot=Robot(),
    ):
        self.drive_base = DriveBase(
            Motor(left_motor_port), Motor(right_motor_port),
            wheel_diameter, axle_track
        )
        self.lastDistance = self.drive_base.distance()
        self.robot = robot

    def start_moving(self, speed=Movement.DRIVE_SPEED, degrees=0):
        self.drive_base.drive(speed, degrees)

    def start_moving_back(self, speed=Movement.DRIVE_SPEED, degrees=0):
        print("start_moving_back: start")
        self.start_moving(speed=speed * -1, degrees=degrees)
        print("start_moving_back: end")

    def stop_moving(self):
        self.drive_base.stop()

    def is_driving(self):
        print("is_driving")
        print(self.drive_base.distance(), " ", self.lastDistance)
        result = self.drive_base.distance() != self.lastDistance
        self.lastDistance = self.drive_base.distance()
        return result

    def move_back_to_origin(self, blocks_checked: int, time_left: int) -> bool:
        sw = StopWatch()
        is_block_left = False
        # move back foreach checked block
        for i in range(0, blocks_checked):
            self.driving_unit.start_moving_back(Movement.BLOCK_CLOSE_UP_SPEED)
            wait(Movement.CLOSE_UP_TIME)
        blocks_checked = 0

        self.start_moving_back()
        sw.resume()
        while time_left > sw.time():
            if self.robot.sensoric_unit.is_block_detected():
                print("Block detected")
                is_block_left = True
            wait(50)

        return is_block_left
