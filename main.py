#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()

ev3.speaker.beep()
# Greifer initialisieren
grap = Graper(motor_port=Port.A, sensor_port=Port.S2)  # Falls andere Ports, anpassen
driving = DrivingUnit()


driving.startMoving()
# Greifer aktivieren, wenn ein Objekt erkannt wird
grap.detect_and_grap()

