from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (
    Motor,
    TouchSensor,
    ColorSensor,
    InfraredSensor,
    UltrasonicSensor,
    GyroSensor,
)
from modules.sensoric_unit import SensoricUnit
from modules.graper import Graper
from modules.driving_unit import DrivingUnit
from constants.constants import Ports, Movement, EV3Speaker


class Robot:
    """Roboter-Klasse, die den EV3-Roboter verwaltet."""

    def __init__(self):
        self.ev3 = EV3Brick()
        self.driving_unit = DrivingUnit(robot=self)
        self.graper = Graper()
        self.sensoric_unit = SensoricUnit()

        self.ev3.speaker.set_volume(EV3Speaker.VOLUME)
        self.ev3.speaker.set_speech_options(language="en", voice="m3", speed=180, pitch=50)

        # Initialize sensors
        # self.color_sensor = ColorSensor(Ports.COLOR_SENSOR_PORT)
        # self.gyro_sensor = GyroSensor(Ports.GYRO_SENSOR_PORT)
        # self.touch_sensor = TouchSensor(Ports.TOUCH_SENSOR_PORT)
