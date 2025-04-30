from pybricks.parameters import Port, Color, Direction
from pybricks.hubs import EV3Brick


class Ports:
    """Ports for the EV3 Brick"""

    # Motor Ports
    MOTOR_DRIVE_FRONT = Port.B
    MOTOR_DRIVE_BACK = Port.C

    # Motor Grapper Ports
    MOTOR_GRAPPER_OPEN_CLOSE = Port.A
    MOTOR_GRAPPER_UP_DOWN = Port.D

    # Sensor Ports
    ULTRASOUND_SENSOR_PORT = Port.S2
    COLOR_SENSOR_PORT = Port.S3
    INFRARED_SENSOR_PORT = Port.S4


class Movement:
    """Movement default values"""

    WHEEL_DIAMETER = 55.5  # Durchmesser der Räder in mm
    AXLE_TRACK = 104  # Abstand zwischen den Rädern in mm
    MOTOR_FRONT = Ports.MOTOR_DRIVE_FRONT
    MOTOR_BACK = Ports.MOTOR_DRIVE_BACK
    DRIVE_SPEED = 70  # Geschwindigkeit in mm/s
    TURN_SPEED = 10


class Sensors:
    """Sensors default values"""

    OBSTACLE_DISTANCE = 100  # Distanz in mm, um ein Hindernis zu erkennen
    ABYSS_DISTANCE_PERCENT = 10


class EV3Speaker:
    """Primarily used for beeping"""

    VOLUME = 100  # Volume in %
    BEEP_DURATION = 1000  # Duration in ms


# ToDo: class Colors?
