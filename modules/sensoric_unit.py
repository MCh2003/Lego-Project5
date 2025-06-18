import math
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
        distance = self.ultrasonic_sensor.distance(False)
        print("Distance: ", distance)
        return distance < Sensors.OBSTACLE_DISTANCE

    def closest_color(self, detected_rgb: tuple[int, int, int] = (0, 0, 0), colors=[], tolerance=300) -> tuple[int, int, int] | None:
        min_distance = float("inf")
        best_match = None

        for color in colors:
            # Euclidean distance: https://en.wikipedia.org/wiki/Euclidean_distance
            distance = math.sqrt(
                (detected_rgb[0] - color[0]) ** 2
                + (detected_rgb[1] - color[1]) ** 2
                + (detected_rgb[2] - color[2]) ** 2
            )

            if distance < min_distance:
                min_distance = distance
                best_match = color

        return best_match if min_distance <= tolerance else None

    def get_color(self):
        return self.color_sensor.rgb()
