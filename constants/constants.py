from pybricks.parameters import Port, Color, Direction
from . import Graper, DrivingUnit
from pybricks.hubs import EV3Brick

class Ports:
    """Ports for the EV3 Brick"""
    # Motor Ports
    MOTOR_GRAPPER = Port.A
    MOTOR_DRIVE_LEFT = Port.C
    MOTOR_DRIVE_RIGHT = Port.D

    # Sensor Ports
    TOUCH_SENSOR_PORT = Port.S2 # Linker Sensor
    COLOR_SENSOR_PORT = Port.S3

    # ToDo: Richtiger Sensor ???
    GYRO_SENSOR_PORT = Port.S4


class Movement:
    """Movement default values"""
    WHEEL_DIAMETER = 55.5  # Durchmesser der Räder in mm
    AXLE_TRACK = 104  # Abstand zwischen den Rädern in mm
    MOTOR_LEFT = Ports.MOTOR_DRIVE_LEFT
    MOTOR_RIGHT = Ports.MOTOR_DRIVE_RIGHT
    DRIVE_SPEED = 200
    TURN_SPEED = 100 

class Sensors:
    """Sensors default values"""
    OBSTACLE_DISTANCE = 100  # Distanz in mm, um ein Hindernis zu erkennen

class EV3Speaker:
    """Primarily used for beeping"""
    VOLUME = 100  # Volume in %
    BEEP_DURATION = 1000  # Duration in ms
# ToDo: class Colors?