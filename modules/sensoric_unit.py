from constants.constants import Ports
from pybricks.ev3devices import InfraredSensor, ColorSensor, UltrasonicSensor
from constants.constants import Sensors


class SensoricUnit:
    def __init__(
        self,
        infrared_sensor_port=Ports.INFRARED_SENSOR_PORT,
        color_sensor_port=Ports.COLOR_SENSOR_PORT,
        ultrasonic_sensor_port=Ports.ULTRASOUND_SENSOR_PORT,
    ):
        self.infrared_sensor = InfraredSensor(infrared_sensor_port)
        self.color_sensor = ColorSensor(color_sensor_port)
        self.ultrasonic_sensor = UltrasonicSensor(ultrasonic_sensor_port)

    def is_abyss_detected(self) -> bool:
        return self.infrared_sensor.distance() > Sensors.ABYSS_DISTANCE_PERCENT

    def is_block_detected(self) -> bool:
        return self.ultrasonic_sensor.distance(True) < Sensors.OBSTACLE_DISTANCE

    def get_color(self):
        return self.color_sensor.rgb()
