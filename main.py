#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from constants.constants import Ports, Movement, EV3Speaker
from modules.robot import Robot

robot = Robot()

robot.ev3.speaker.set_volume(EV3Speaker.VOLUME)  # Set volume to 100%
robot.ev3.speaker.beep()  # Beep to indicate the start of the program

robot.graper.move_up() # Move the grapper up

drive_base = DriveBase(Motor(Ports.MOTOR_DRIVE_FRONT), Motor(Ports.MOTOR_DRIVE_BACK), Movement.WHEEL_DIAMETER, Movement.AXLE_TRACK)
drive_base.drive(200, 0)  # Move forward at the default speed
wait(2000)  # Wait for 2 seconds
drive_base.stop()  # Stop moving

motor_open_close = Motor(Ports.MOTOR_GRAPPER_OPEN_CLOSE)
motor_open_close.run_target(-1000, 1800, Stop.HOLD, True)
motor_open_close.run_target(-1000, -600, Stop.HOLD, True)  # Move to 90 degrees
print("Greifer nach oben bewegt.")
motor_open_close.stop()
print("Greifer gestoppt.")   

robot.graper.move_down()  # Move the grapper down

robot.ev3.speaker.beep()  # Beep to indicate the start of the program