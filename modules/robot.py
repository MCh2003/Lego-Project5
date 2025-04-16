from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from .grap import Graper
from .drivingUnit import DrivingUnit
from ..constants.constants import Ports, Movement

class Robot:
    """Roboter-Klasse, die den EV3-Roboter verwaltet.
    """
    def __init__(self):
        self.ev3 = EV3Brick()
        self.driving_unit = DrivingUnit()
        self.graper = Graper(motor_port=Ports.MOTOR_GRAPPER, sensor_port=Ports.COLOR_SENSOR_PORT)

        # Initialize sensors
        self.color_sensor = ColorSensor(Ports.COLOR_SENSOR_PORT)
        self.gyro_sensor = GyroSensor(Ports.GYRO_SENSOR_PORT)
        self.touch_sensor = TouchSensor(Ports.TOUCH_SENSOR_PORT)
