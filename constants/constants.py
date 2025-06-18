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

    WHEEL_DIAMETER = 25  # Durchmesser der Räder in mm
    AXLE_TRACK = 104  # Abstand zwischen den Rädern in mm
    MOTOR_FRONT = Ports.MOTOR_DRIVE_FRONT
    MOTOR_BACK = Ports.MOTOR_DRIVE_BACK
    DRIVE_SPEED = 100  # Geschwindigkeit in mm/s
    BLOCK_CLOSE_UP_SPEED = 150  # leave this at 50 mm/s
    CLOSE_UP_TIME = (
        650  # if BLOCK_CLOSE_UP_SPEED is changed, change this too (50 mm/s = 3500 ms)
    )
    TURN_SPEED = 10
    TURN_COUNTER_CLOCKWISE = -190
    TURN_CLOCKWISE = 190
    TURN_DEGREE = 180


class Sensors:
    """Sensors default values"""

    OBSTACLE_DISTANCE = 100  # Distanz in mm, um ein Hindernis zu erkennen
    ABYSS_DISTANCE_PERCENT = 10


class EV3Speaker:
    """Primarily used for beeping"""

    VOLUME = 60  # Volume in %
    BEEP_DURATION = 1000  # Duration in ms


# ToDo: change these values
class Colors:
    """RGB values for colors"""

    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
