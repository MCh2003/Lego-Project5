from pybricks.ev3devices import (
    Motor,
    TouchSensor,
    ColorSensor,
    InfraredSensor,
    UltrasonicSensor,
    GyroSensor,
)
from constants.constants import Ports, Sensors
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait


class Graper:
    """Greifer-Klasse, die den Greifer des Roboters verwaltet."""
    class Constants:
        DOWN_ANGLE = 0
        UP_ANGLE = -45
        UP_DOWN_SPEED = 50

        OPEN_ANGLE = 720
        CLOSE_ANGLE = 30
        OPEN_CLOSE_SPEED = 320

    def __init__(self):
        print("Initializing Graper...")
        self.motor_up_down = Motor(Ports.MOTOR_GRAPPER_UP_DOWN)
        print("Motor Up Down initialized")
        self.motor_open_close = Motor(Ports.MOTOR_GRAPPER_OPEN_CLOSE)

    def is_block_detected(self):
        return self.ultrasoncic_sensor.distance() < Sensors.OBSTACLE_DISTANCE

    def move_up_down_to(self, speed=Constants.UP_DOWN_SPEED, target_angle=Constants.UP_ANGLE):
        """Moves the graper to a specific angle."""
        print("move graper")
        self.motor_up_down.run_target(speed, target_angle, Stop.HOLD, True)

    def hold(self):
        angle = self.motor_up_down.angle()
        self.motor_up_down.run_target(100, angle, Stop.HOLD, False)

    def open(self) -> int:
        """Opens the grapper and returns the angle of the grapper."""
        print("open grapper")
        prev_angle = self.motor_open_close.angle()
        self.motor_open_close.run_target(Graper.Constants.OPEN_CLOSE_SPEED, Graper.Constants.OPEN_ANGLE, Stop.HOLD, True)
        return prev_angle

    def close(self):
        """Closes the grapper."""
        self.motor_open_close.run_target(Graper.Constants.OPEN_CLOSE_SPEED, Graper.Constants.CLOSE_ANGLE, Stop.HOLD, True)

    def back_to_origin(self):
        """Moves the grapper back to the origin."""
        self.motor_open_close.run_angle(120, -30, Stop.HOLD, True)

    def bbl(self):
        """Moves the grapper back to the origin."""
        self.motor_open_close.run_target(120, 0, Stop.HOLD, True)

    def up(self):
        self.move_up_down_to(Graper.Constants.UP_DOWN_SPEED, Graper.Constants.UP_ANGLE)

    def down(self):
        self.move_up_down_to(Graper.Constants.UP_DOWN_SPEED, Graper.Constants.DOWN_ANGLE)
