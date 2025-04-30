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


def calibrate_colors(robot: Robot):
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

robot.graper.hold()
colors = calibrate_colors(robot)
robot.ev3.speaker.beep()
sw = StopWatch()
is_block_left = len(colors) > 0
blocks_checked = 0

# block_detected = True
while is_block_left:
    robot.driving_unit.start_moving()
    sw.resume()

    # ToDo: put this stuff into separate functions
    # Check for block -> color
    if robot.sensoric_unit.is_block_detected():
        print("Block detected")
        sw.pause()
        blocks_checked += 1

        robot.driving_unit.start_moving(Movement.BLOCK_CLOSE_UP_SPEED)
        wait(Movement.CLOSE_UP_TIME)
        robot.driving_unit.stop_moving()

        detected_color = robot.sensoric_unit.get_color()
        print("Detected color: ", detected_color)
        closest_color = SensoricUnit.closest_color(detected_color, colors, 50)
        if closest_color is not None:
            print("Closest color: ", closest_color)
            # ToDo: logic for what to do with color - pickup etc.

    # Check for abyss
    if robot.sensoric_unit.is_abyss_detected():
        print("Abyss detected")
        is_block_left = False
        time_left = sw.time()

        # move back foreach checked block
        for i in range(0, blocks_checked):
            robot.driving_unit.start_moving_back(Movement.BLOCK_CLOSE_UP_SPEED)
            wait(Movement.CLOSE_UP_TIME)
        blocks_checked = 0

        robot.driving_unit.start_moving_back()
        sw.reset()
        while time_left > sw.time():
            if robot.sensoric_unit.is_block_detected():
                print("Block detected")
                is_block_left = True
            wait(50)

        sw.pause()
        sw.reset()

    wait(100)

robot.driving_unit.stop_moving()
robot.ev3.speaker.beep()
