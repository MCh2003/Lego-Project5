#!/usr/bin/env pybricks-micropython
import math
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (
    Motor,
    TouchSensor,
    ColorSensor,
    InfraredSensor,
    UltrasonicSensor,
    GyroSensor,
)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from constants.constants import Ports, Movement, EV3Speaker
from modules.robot import Robot
from modules.sensoric_unit import SensoricUnit


def calibrate_colors(robot: Robot) -> list[tuple[int, int, int]]:
    robot.ev3.speaker.say("Calibrate Colors")

    colors = []
    while Button.UP not in robot.ev3.buttons.pressed():
        curr_color = robot.sensoric_unit.get_color()
        robot.ev3.screen.print(curr_color)

        if Button.CENTER in robot.ev3.buttons.pressed():
            if len(colors) >= 3:
                robot.ev3.speaker.say("Error: Too many colors")
                robot.ev3.screen.print("Error: Too many colors")
                wait(2000)
                exit(0)
            else:
                robot.ev3.speaker.beep()
                colors.append(curr_color)
                print("added: ", curr_color)
                robot.ev3.screen.print("added: ", curr_color)
                wait(100)

    robot.ev3.speaker.say("Colors calibrated")
    return colors


def block_detect_test(robot: Robot) -> bool:
    """Test if a block is detected."""
    i = 0
    while (i < 1):
        robot.driving_unit.start_moving()
        if robot.sensoric_unit.is_block_detected():
            robot.driving_unit.stop_moving()
            robot.ev3.speaker.say("Block detected")
            robot.ev3.speaker.beep()
            robot.driving_unit.start_moving()
            wait(500)
            i += 1

    wait(50)
    robot.driving_unit.stop_moving()
    return True


def quality_test_abyss(robot: Robot) -> bool:
    """Test if an abyss is detected."""

    while (robot.sensoric_unit.is_abyss_detected() is False):
        robot.driving_unit.start_moving()
        wait(0)

    robot.driving_unit.stop_moving()
    robot.ev3.speaker.say("AAAAAAAAAAAAA")
    robot.ev3.speaker.beep()
    wait(1000)
    return True


def quality_test_lift_block(robot: Robot) -> bool:
    i = 0
    while (i < 5):
        print("downed")
        wait(100)
        robot.graper.close()
        print("closed")
        wait(100)
        robot.graper.up()
        print("upped")
        robot.graper.hold()
        wait(3500)
        robot.graper.down()
        robot.graper.open()
        print("opened")
        wait(100)
        robot.ev3.speaker.say("done")
        i += 1

    return True


def turn_and_turn_back_test(robot: Robot) -> bool:
    """Turn the robot and turn back to the original position."""
    robot.driving_unit.turn_counter_clockwise()
    wait(1000)

    # robot.driving_unit.turn_clockwise()
    robot.driving_unit.start_moving()
    wait(1000)
    robot.driving_unit.stop_moving()
    return True


def abyss_drive_back_test(robot: Robot) -> bool:
    """Test if the robot drives back when an abyss is detected."""
    s = StopWatch()

    s.resume()
    robot.driving_unit.start_moving()
    while (robot.sensoric_unit.is_abyss_detected() is False):
        wait(0)
    s.pause()

    r = StopWatch()
    r.resume()
    robot.driving_unit.start_moving_back()
    while (r.time() < s.time()):
        wait(50)
    robot.driving_unit.stop_moving()

    robot.ev3.speaker.say("Abyss reset")
    robot.ev3.speaker.beep()
    wait(1000)
    return True


robot = Robot()
robot.ev3.speaker.beep()


# while (True):
#     robot.graper.bbl()


# robot.graper.init()
# robot.driving_unit.turn_degrees(180)


# region colortest
# colors = calibrate_colors(robot)
# robot.ev3.speaker.beep()
# endregion

# region block_detect_test
robot.graper.up()
robot.graper.hold()
block_detect_test(robot)
# endregion block_detect_test(robot)

# region quality_test_abyss
# quality_test_abyss(robot)
# endregion quality_test_abyss(robot)

# region quality_test_lift_block
# quality_test_lift_block(robot)
# endregion quality_test_lift_block(robot)


# region turn_and_turn_back_test
# turn_and_turn_back_test(robot)
# endregion turn_and_turn_back_test(robot)

# region abyss_drive_back_test
# abyss_drive_back_test(robot)
# endregion abyss_drive_back_test(robot)

wait(10000)
# while True:
#     robot.graper.back_to_origin()


# robot.driving_unit.turn_clockwise()
# robot.ev3.speaker.beep()
# wait(10000)

robot.graper.init()
# robot.driving_unit.turn_degrees(180)


colors = calibrate_colors(robot)
robot.ev3.speaker.beep()

sw = StopWatch()
sw_color = StopWatch()
is_block_left = len(colors) > 0
blocks_checked = 0
blocks_to_skip = 0
blocks_skipped = 0
current_color = None
closest_color = None

robot.ev3.speaker.say("Starting")
# block_detected = True
while is_block_left:
    robot.driving_unit.start_moving()
    sw.resume()

    # Check for block -> color
    if robot.sensoric_unit.is_block_detected():
        print("Block detected")

        if current_color is None:
            print("First block")
            current_color = robot.process_detected_block(
                sw, current_color, colors, blocks_checked
            )
            sw_color.resume()
            blocks_checked += 1

        if current_color is not None:
            print("current_color is not none")
            detected_color = robot.process_detected_block(
                sw, current_color, colors, blocks_checked, sw_color
            )
            if detected_color == current_color:
                blocks_checked += 1
            sw_color.resume()

        """
        if blocks_skipped < blocks_to_skip:
            blocks_skipped += 1
            sw.pause()
            continue



        if closest_color == current_color:
            print("Lifting block")

            # Check if block is still there
            closest_color = robot.scan_color(colors)
            if (closest_color is not None) and (closest_color == current_color):
                print("Block still there")
                # Drive back to the block
                wait(1000)
                robot.graper.down()
                robot.graper.open()
                print("Block dropped")
                wait(1000)
                robot.graper.up()
                robot.graper.hold()
                robot.graper.bbl()
                exit(0)
                # robot.move_back_to_origin(blocks_checked, sw)

                # robot.driving_unit.turn_clockwise()

                # # ToDo: stacking blocks logic
                # robot.drop_stone_arm_open_up_hold()

                # robot.driving_unit.turn_counter_clockwise()
            else:
                print("Block dropped")
        else:
            print("Wrong color")
            robot.graper.up()
            robot.graper.hold()
            blocks_to_skip += 1




        # graper is down and open
        ## closest_color = robot.process_detected_block(sw, colors)
        blocks_checked = robot.process_detected_block(sw, colors, blocks_checked)
    """
    # Check for abyss
    if robot.sensoric_unit.is_abyss_detected():
        print("Abyss detected")
        current_color = None
        is_block_left = robot.move_back_to_origin(blocks_checked, sw)
        blocks_to_skip = 0
        blocks_skipped = 0
    wait(100)

robot.driving_unit.stop_moving()
robot.ev3.speaker.beep()
