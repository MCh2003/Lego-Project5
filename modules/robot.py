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
        self.ev3.speaker.set_speech_options(
            language="en", voice="m3", speed=180, pitch=50
        )

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

    def scan_color(
        self, colors: list[tuple[int, int, int]]
    ) -> tuple[int, int, int] | None:
        detected_color = self.sensoric_unit.get_color()
        print("Detected color:", detected_color)
        return self.sensoric_unit.closest_color(detected_color, colors, 50)

    def process_detected_block(
        self,
        sw: StopWatch,
        current_color: tuple[int, int, int] | None,
        colors: list[tuple[int, int, int]],
        blocks_checked: int,
        sw_color=None,
    ) -> tuple[int, int, int]:
        """
        Handles the process when a block is detected:
        - Pauses the stopwatch
        - Approaches the block
        - Scans the block color
        - Executes an action (place and reset)
        """

        self.move_color_sensor_to_block()
        sw.pause()
        if sw_color is not None:
            sw_color.pause
        wait(1000)

        detected_color = self.sensoric_unit.get_color()
        print("Detected color: ", detected_color)
        closest_color = self.sensoric_unit.closest_color(detected_color, colors, 50)
        print("Closest color: ", closest_color)

        if current_color is None:
            print("checked that first block is")
            self.handle_color_action(closest_color, blocks_checked)
            return closest_color

        if current_color is not None:
            print("checked that not first block is")
            if closest_color == current_color:
                print("checked for same block")
                self.handle_color_action(closest_color, blocks_checked)
                return current_color  # type: ignore

        return detected_color  # type: ignore

    def lift_stone(self):
        self.graper.down()
        print("downed")
        wait(100)
        self.graper.close()
        print("closed")
        wait(100)
        self.graper.up()
        print("upped")
        self.graper.hold()

        self.ev3.speaker.say("OOOOF")

    def drop_stone_arm_open_up_hold(self):
        """
        Drops the stone and resets graper to idle state.
        """
        self.graper.down()
        self.graper.open()
        self.graper.up()
        self.graper.hold()

    def place_block_at_position(self, blocks_checked: int):
        """
        Places a block on the ground precisely and moves slightly backwards.
        """
        print("Placing block...")
        self.graper.down()
        wait(300)
        self.graper.open()
        wait(300)
        self.graper.up()
        self.driving_unit.start_moving_back(speed=30)
        wait(1000)
        self.driving_unit.stop_moving()

    def rotate_to_placing_pose(self):
        """
        Rotates to block place position
        """
        self.driving_unit.turn_degrees(Movement.TURN_DEGREE)

    def reset_rotation(self):
        """
        Rotates to block place position
        """
        self.driving_unit.turn_degrees(-Movement.TURN_DEGREE)

    def reset_to_driving_pose(self):
        """
        Returns the robot to a driving-ready state after placing a block.
        """
        print("Resetting to driving pose...")
        self.graper.hold()
        self.driving_unit.start_moving(speed=40)
        wait(1000)
        self.driving_unit.stop_moving()

    def handle_color_action(self, color: tuple[int, int, int], blocks_checked: int):
        """
        Executes an action when a known block color is detected.
        """
        print("Handling color action for color:", color)
        self.lift_stone()
        self.rotate_to_placing_pose()
        if blocks_checked == 0:
            self.place_block_at_position(blocks_checked)
        self.reset_rotation()
        self.reset_to_driving_pose()
