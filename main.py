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
            robot.ev3.speaker.beep()
            colors.append(curr_color)
            print("added: ", curr_color)
            wait(100)

    robot.ev3.speaker.say("Colors calibrated")
    return colors


robot = Robot()
robot.ev3.speaker.beep()

robot.graper.up()
robot.graper.hold()
colors = calibrate_colors(robot)
robot.ev3.speaker.beep()

sw = StopWatch()
is_block_left = len(colors) > 0
blocks_checked = 0
blocks_to_skip = 0
blocks_skipped = 0
current_color = None

# block_detected = True
while is_block_left:
    robot.driving_unit.start_moving()
    sw.resume()

    # Check for block -> color
    if robot.sensoric_unit.is_block_detected():
        print("Block detected")

        if blocks_skipped < blocks_to_skip:
            blocks_skipped += 1
            sw.pause()
            robot.move_color_sensor_to_block()
            continue

        # graper is down and open
        closest_color = robot.process_detected_block(sw, colors)
        if closest_color is not None:
            print("Closest color: ", closest_color)
            blocks_checked += 1

            if current_color is None:
                print("First block")
                current_color = closest_color
                sw.reset()
                blocks_checked = 0

            if closest_color == current_color:
                print("Lifting block")
                robot.lift_stone(closest_color, colors)

                # Check if block is still there
                closest_color = robot.process_detected_block(sw, colors)
                if (closest_color is not None) and (closest_color == current_color):
                    print("Block still there")
                    # Drive back to the block
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
