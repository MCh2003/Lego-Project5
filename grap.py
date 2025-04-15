from pybricks.ev3devices import Motor, TouchSensor
from pybricks.parameters import Port
from pybricks.tools import wait

class GrapUnit:
    def __init__(self):
        self.motor = Motor(Port.A)               # Greifer-Motor
        self.sensor = TouchSensor(Port.S2)       # Linker Sensor über dem Objekt

    def grapObject(self):
        print("Warten auf Erkennung mit dem Sensor...")

        while not self.sensor.pressed():
            wait(10)  # 10ms warten

        print("Objekt erkannt. Bewege Greifer nach unten.")
        self.motor.run_angle(500, 800)  # z.B. 800° – anpassen je nach Mechanik

        print("Schließe den Greifer.")
        self.motor.run_angle(500, -400)  # z.B. -400° für Greifen – auch anpassbar

        print("Fertig gegrapet.")
