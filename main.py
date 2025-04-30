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


colors = [
    (0, 0, 0),  # Black
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (255, 255, 255)  # White
]

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

    if robot.sensoric_unit.is_abyss_detected():
        print("Abyss detected")
        is_block_left = False
        time_left = sw.time()

        # move back for block
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
                
            # ToDo: may cause inaccuracy
            wait(50)

        sw.pause()
        sw.reset()

    wait(100)

robot.driving_unit.stop_moving()
robot.ev3.speaker.beep()

# # robot.graper.move_up() # Move the grapper up

# # drive_base = DriveBase(Motor(Ports.MOTOR_DRIVE_FRONT), Motor(Ports.MOTOR_DRIVE_BACK), Movement.WHEEL_DIAMETER, Movement.AXLE_TRACK)
# # drive_base.drive(20, 0)  # Move forward at the default speed
# # wait(1000)  # Wait for 2 seconds
# # drive_base.stop()  # Stop moving

# # motor_open_close = Motor(Ports.MOTOR_GRAPPER_OPEN_CLOSE)
# # motor_open_close.run_target(-1000, 1800, Stop.HOLD, True)
# # motor_open_close.run_target(-1000, -600, Stop.HOLD, True)  # Move to 90 degrees
# # print("Greifer nach oben bewegt.")
# # motor_open_close.stop()
# # print("Greifer gestoppt.")

# # robot.graper.move_down()  # Move the grapper down

# # robot.ev3.speaker.beep()  # Beep to indicate the start of the program
