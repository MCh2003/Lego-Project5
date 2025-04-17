from pybricks.ev3devices import Motor, TouchSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from ..constants.constants import Ports

class Graper:
    def __init__(self, motor_port=Ports.MOTOR_GRAPPER, sensor_port=Ports.TOUCH_SENSOR_PORT):
        self.motor = Motor(motor_port)
        self.sensor = TouchSensor(sensor_port)  # Linker Sensor erkennt das Objekt

    def detect_and_grap(self):
        """Wartet auf eine Erkennung und greift das Objekt."""
        print("Warten auf Erkennung...")
        while not self.sensor.pressed():
            wait(10)

        print("Objekt erkannt! Bewege den Greifer nach unten...")
        self.motor.run_angle(500, 800)  # Greifer nach unten bewegen

        print("Greife das Objekt...")
        self.motor.run_angle(500, -400)  # Objekt greifen

        print("Greifvorgang abgeschlossen.")

    def release_object(self):
        """Öffnet den Greifer, um das Objekt loszulassen."""
        print("Objekt wird losgelassen...")
        self.motor.run_angle(500, 400)  # Greifer öffnen (Gegenteil vom Greifen)

        print("Greifer ist geöffnet.")

