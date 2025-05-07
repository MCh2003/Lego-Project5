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
from pybricks.tools import wait, StopWatch


class Robot:
    """Roboter-Klasse, die den EV3-Roboter verwaltet."""

    def __init__(self):
        self.ev3 = EV3Brick()
        self.driving_unit = DrivingUnit()
        self.graper = Graper()
        self.sensoric_unit = SensoricUnit()

        self.ev3.speaker.set_volume(EV3Speaker.VOLUME)
        self.ev3.speaker.set_speech_options(language="en", voice="m3", speed=180, pitch=50)

        # Initialize sensors
        # self.color_sensor = ColorSensor(Ports.COLOR_SENSOR_PORT)
        # self.gyro_sensor = GyroSensor(Ports.GYRO_SENSOR_PORT)
        # self.touch_sensor = TouchSensor(Ports.TOUCH_SENSOR_PORT)

    def move_back_to_origin(self, blocks_checked: int, time_left: int) -> bool:
        sw = StopWatch()
        is_block_left = False
        # move back foreach checked block
        for i in range(0, blocks_checked):
            self.driving_unit.start_moving_back(Movement.BLOCK_CLOSE_UP_SPEED)
            wait(Movement.CLOSE_UP_TIME)
        blocks_checked = 0

        self.driving_unit.start_moving_back()
        sw.resume()
        while time_left > sw.time():
            if self.sensoric_unit.is_block_detected():
                print("Block detected")
                is_block_left = True
            wait(50)

        return is_block_left
