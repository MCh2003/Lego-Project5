from constants.constants import Ports
from pybricks.ev3devices import InfraredSensor
from constants.constants import Sensors

class AbyssDetector:
    def __init__(self, port=Ports.INFRARED_SENSOR_PORT):
        self.sensor = InfraredSensor(port)

    def is_abyss_detected(self) -> bool:
        return self.sensor.distance() > Sensors.ABYSS_DISTANCE_PERCENT