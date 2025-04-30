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

    def __init__(self):
        print("Initializing Graper...")
        self.motor_up_down = Motor(Ports.MOTOR_GRAPPER_UP_DOWN)
        print("Motor Up Down initialized")
        self.motor_open_close = Motor(Ports.MOTOR_GRAPPER_OPEN_CLOSE)

    def is_block_detected(self):
        return self.ultrasoncic_sensor.distance() < Sensors.OBSTACLE_DISTANCE

    def move_up(self):
        """Bewege den Greifer nach oben."""
        print("Greifer nach oben bewegt.")
        self.motor_up_down.run_target(100, -90, Stop.HOLD, False)  # Move to 90 degrees
        print("Greifer gestoppt.")

    def move_down(self):
        """Bewege den Greifer nach unten."""
        self.motor_up_down.run_target(100, 90, Stop.HOLD, True)  # Move to 90 degrees
        self.motor_up_down.stop()
        print("Greifer gestoppt.")

    def open(self) -> int:
        """Opens the grapper and retursn the angle of the grapper."""
        print("Open grapper")
        prev_angle = self.motor_open_close.angle()
        self.motor_open_close.run_target(300, 720, Stop.HOLD, True)
        print("Grapper stopped.")
        return prev_angle

    def close(self):
        """Schließe den Greifer."""
        print("Close grapper1")
        self.motor_open_close.run_target(300, 360, Stop.HOLD, True)
        print("Grapper stopped")
