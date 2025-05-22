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

        INIT_UP_ANGLE = -32
        INIT_OPEN_ANGLE = 720

        DOWN_ANGLE = -15
        UP_ANGLE = -45
        UP_DOWN_SPEED = 50

        OPEN_ANGLE = 720
        CLOSE_ANGLE = 20  # 30 vorher gewesen
        OPEN_CLOSE_SPEED = 320

    def __init__(self):
        print("Initializing Graper...")
        self.motor_up_down = Motor(Ports.MOTOR_GRAPPER_UP_DOWN)
        print("Motor Up Down initialized")
        self.motor_open_close = Motor(Ports.MOTOR_GRAPPER_OPEN_CLOSE)

    def init(self):
        self.up(Graper.Constants.INIT_UP_ANGLE)
        self.hold()
        self.open(3 * Graper.Constants.INIT_OPEN_ANGLE)

    def move_up_down_to(self, target_angle, speed=Constants.UP_DOWN_SPEED):
        """Moves the graper to a specific angle."""
        print("move graper")
        self.motor_up_down.run_target(speed, target_angle, Stop.HOLD, True)

    def hold(self):
        angle = self.motor_up_down.angle()
        print("holding graper at", angle)
        self.motor_up_down.run_target(100, angle, Stop.HOLD, False)

    def open(self, target_angle=Constants.OPEN_ANGLE) -> int:
        """Opens the grapper and returns the angle of the grapper."""
        print("open grapper at", target_angle)
        prev_angle = self.motor_open_close.angle()
        self.motor_open_close.run_target(
            Graper.Constants.OPEN_CLOSE_SPEED, target_angle, Stop.HOLD, True
        )
        return prev_angle

    def close(self):
        """Closes the grapper."""
        self.motor_open_close.run_target(
            Graper.Constants.OPEN_CLOSE_SPEED,
            Graper.Constants.CLOSE_ANGLE,
            Stop.HOLD,
            True,
        )

    def back_to_origin(self):
        """Moves the grapper back to the origin."""
        self.motor_open_close.run_angle(120, -30, Stop.HOLD, True)

    def bbl(self):
        """Moves the grapper back to the origin."""
        self.motor_open_close.run_time(-320, 1000, Stop.HOLD, True)

    def up(self, target_angle=Constants.UP_ANGLE):
        self.move_up_down_to(target_angle, Graper.Constants.UP_DOWN_SPEED)

    def down(self, target_angle=Constants.DOWN_ANGLE):
        self.move_up_down_to(target_angle, Graper.Constants.UP_DOWN_SPEED)
