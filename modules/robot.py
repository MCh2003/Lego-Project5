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

    def move_color_sensor_to_block(self):
        self.driving_unit.start_moving(Movement.BLOCK_CLOSE_UP_SPEED)
        wait(Movement.CLOSE_UP_TIME)
        self.driving_unit.stop_moving()

    def move_back_to_origin(self, blocks_checked: int, sw: StopWatch) -> bool:
        is_block_left = False
        # move back foreach checked block
        for i in range(0, blocks_checked):
            self.driving_unit.start_moving_back(Movement.BLOCK_CLOSE_UP_SPEED)
            wait(Movement.CLOSE_UP_TIME)
        blocks_checked = 0

        self.driving_unit.start_moving_back()
        time_left = sw.time()
        sw.reset()
        while time_left > sw.time():
            if self.sensoric_unit.is_block_detected():
                print("Block detected")
                is_block_left = True
            wait(50)

        sw.pause()
        sw.reset()

        return is_block_left

    def process_detected_block(self, sw: StopWatch, colors: list[tuple[int, int, int]], blocks_checked: int) -> int:
        sw.pause()

        self.move_color_sensor_to_block()

        detected_color = self.sensoric_unit.get_color()
        print("Detected color: ", detected_color)
        closest_color = SensoricUnit.closest_color(detected_color, colors, 50)

        if closest_color is not None:
            print("Closest color: ", closest_color)
            self.handle_color_action(closest_color)

        return blocks_checked
