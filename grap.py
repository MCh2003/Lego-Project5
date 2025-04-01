from pybricks.ev3devices import Motor, TouchSensor
from pybricks.parameters import Port
from pybricks.tools import wait

class Graper:
    def __init__(self, motor_port=Port.A, sensor_port=Port.S2):
        self.motor = Motor(motor_port)
        self.sensor = TouchSensor(sensor_port)  # Linker Sensor erkennt das Objekt

    def detect_and_grap(self):
        """Wartet auf eine Erkennung und greift das Objekt."""
        print("Warten auf Erkennung...")
        while not self.sensor.pressed():  # Wartet auf Objekterkennung
            wait(10)

        print("Objekt erkannt! Bewege den Greifer nach unten...")
        self.motor.run_angle(500, 90)  # Greifer nach unten bewegen

        print("Greife das Objekt...")
        self.motor.run_angle(500, -45)  # Objekt greifen

        print("Greifvorgang abgeschlossen.")
