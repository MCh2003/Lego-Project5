from constants.constants import Ports
from pybricks.ev3devices import InfraredSensor, ColorSensor
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
        self.ultrasonic_sensor = InfraredSensor(ultrasonic_sensor_port)

    def is_abyss_detected(self) -> bool:
        return self.infrared_sensor.distance() > Sensors.ABYSS_DISTANCE_PERCENT

    def get_color(self):
        """Returns the color of the sensor. If no color is detected, returns the RGB value."""
        print("get_color")
        col = self.color_sensor.color()
        if col is not None:
            print("get_color: ", col)
            return col
        return self.color_sensor.rgb()
