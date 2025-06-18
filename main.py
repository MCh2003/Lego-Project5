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
from constants.constants import Ports, Movement, EV3Speaker, Colors
from modules.robot import Robot
from modules.sensoric_unit import SensoricUnit


def optional_close_grapper(robot: Robot):
    resetting = False
    for _ in range(100):
        if Button.CENTER not in robot.ev3.buttons.pressed():
            resetting = True
            break
        wait(50)

    while resetting and Button.UP not in robot.ev3.buttons.pressed():
        robot.graper.close_by_angle()
        wait(50)
    robot.graper.motor_open_close.reset_angle(0)


robot = Robot()
robot.ev3.speaker.beep()

robot.graper.up()
robot.graper.hold()
optional_close_grapper(robot)

colors = [Colors.RED, Colors.BLUE, Colors.WHITE]

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
            current_color = robot.process_detected_block(sw, colors)
            sw_color.resume()
            blocks_checked += 1

        if current_color is not None:
            print("current_color is not none")
            detected_color = robot.process_detected_block(sw, colors)
            if detected_color == current_color:
                blocks_checked += 1
            sw_color.resume()

        if blocks_skipped < blocks_to_skip or (current_color is None):
            blocks_skipped += 1
            sw.pause()
            continue

        if closest_color == current_color:
            print("Lifting block")
            robot.lift_stone(current_color, colors)

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

                robot.move_back_to_origin(blocks_checked, sw)

                robot.driving_unit.turn_clockwise()

                # ToDo: stacking blocks logic
                robot.drop_stone_arm_open_up_hold()

                robot.driving_unit.turn_counter_clockwise()
            else:
                print("Block dropped")
        else:
            print("Wrong color")
            robot.graper.up()
            robot.graper.hold()
            blocks_to_skip += 1

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
