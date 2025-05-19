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
from pybricks.parameters import Stop

class Robot:
    """
    Robot class to control the LEGO EV3 robot.
    Includes driving, grabbing, sensing, and color-based block handling.
    """

    def __init__(self):
        self.ev3 = EV3Brick()
        self.driving_unit = DrivingUnit()
        self.graper = Graper()
        self.sensoric_unit = SensoricUnit()

        self.ev3.speaker.set_volume(EV3Speaker.VOLUME)
        self.ev3.speaker.set_speech_options(language="en", voice="m3", speed=180, pitch=50)

    def move_color_sensor_to_block(self):
        self.driving_unit.start_moving(Movement.BLOCK_CLOSE_UP_SPEED)
        wait(Movement.CLOSE_UP_TIME)
        self.driving_unit.stop_moving()

    def move_back_to_origin(self, blocks_checked: int, sw: StopWatch) -> bool:
        is_block_left = False
        for _ in range(blocks_checked):
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

    def scan_color(self, colors: list[tuple[int, int, int]]) -> tuple[int, int, int] | None:
        detected_color = self.sensoric_unit.get_color()
        print("Detected color:", detected_color)
        return SensoricUnit.closest_color(detected_color, colors, 50)

    def process_detected_block(self, sw: StopWatch, colors: list[tuple[int, int, int]], blocks_checked: int) -> int:
        """
        Handles the process when a block is detected:
        - Pauses the stopwatch
        - Approaches the block
        - Scans the block color
        - Executes an action (place and reset)
        """
        sw.pause()
        self.move_color_sensor_to_block()
        self.graper.down()
        wait(1000)

        closest_color = self.scan_color(colors)

        if closest_color is not None:
            print("Closest color:", closest_color)
            self.handle_color_action(closest_color)

        return blocks_checked

    def lift_stone(self, color: tuple[int, int, int], colors: list[tuple[int, int, int]]):
        self.graper.close()
        self.graper.up()
        self.graper.hold()

        closest_color = self.scan_color(colors)
        if closest_color is None or closest_color != color:
            print("Block dropped")
            self.ev3.speaker.say("OOOOOOOF")

    def drop_stone_arm_open_up_hold(self):
        """
        Drops the stone and resets graper to idle state.
        """
        self.graper.down()
        self.graper.open()
        self.graper.up()
        self.graper.hold()

    def place_block_at_position(self):
        """
        Places a block on the ground precisely and moves slightly backwards.
        """
        print("Placing block...")
        self.graper.down()
        self.graper.open()
        wait(300)
        self.graper.up()
        self.driving_unit.start_moving_back(speed=30)
        wait(1000)
        self.driving_unit.stop_moving()

    def reset_to_driving_pose(self):
        """
        Returns the robot to a driving-ready state after placing a block.
        """
        print("Resetting to driving pose...")
        self.graper.hold()
        self.driving_unit.start_moving(speed=40)
        wait(1000)
        self.driving_unit.stop_moving()

    def handle_color_action(self, color: tuple[int, int, int]):
        """
        Executes an action when a known block color is detected.
        """
        print("Handling color action for color:", color)
        self.place_block_at_position()
        self.reset_to_driving_pose()
