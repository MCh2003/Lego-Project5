from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port
from pybricks.tools import wait
from ..constants.constants import Ports, Sensors
from pybricks.pupdevices import UltrasonicSensor

class Graper:
    """Greifer-Klasse, die den Greifer des Roboters verwaltet."""
    # motor_up_down=Ports.MOTOR_GRAPPER_OPEN_CLOSE, motor_open_close=Ports.MOTOR_GRAPPER_UP_DOWN, sensor_port=Ports.INFRARED_SENSOR_PORT
    def __init__(self):
        print("Initializing Graper...")
        #self.motor_up_down = Motor(Ports.MOTOR_GRAPPER_UP_DOWN)
        print("Motor Up Down initialized")
        # self.motor_open_close = Motor(motor_up_down)
        # self.motor_open_close = Motor(motor_open_close)

        # self.ultrasoncic_sensor = UltrasonicSensor(sensor_port)  # Linker Sensor erkennt das Objekt

    # def detect_and_grap(self):
    #     """Wartet auf eine Erkennung und greift das Objekt."""
    #     print("Warten auf Erkennung...")
    #     while not self.sensor.pressed():
    #         wait(10)

    #     print("Objekt erkannt! Bewege den Greifer nach unten...")
    #     self.motor.run_angle(500, 800)  # Greifer nach unten bewegen

    #     print("Greife das Objekt...")
    #     self.motor.run_angle(500, -400)  # Objekt greifen

    #     print("Greifvorgang abgeschlossen.")

    # def release_object(self):
    #     """Öffnet den Greifer, um das Objekt loszulassen."""
    #     print("Objekt wird losgelassen...")
    #     self.motor.run_angle(500, 400)  # Greifer öffnen (Gegenteil vom Greifen)

    #     print("Greifer ist geöffnet.")

    def is_block_detected(self):
        return self.ultrasoncic_sensor.distance() < Sensors.OBSTACLE_DISTANCE

    def move_up(self):
        """Bewege den Greifer nach oben."""
        self.motor_up_down.run_angle(30, 10)
        print("Greifer nach oben bewegt.")
        wait(3000)  # Warte 1 Sekunde
        self.motor_up_down.stop()
        print("Greifer gestoppt.")
    
    def open(self):
        """Öffne den Greifer."""
        self.motor_open_close.run_angle(30, 10)
        print("Greifer nach oben bewegt.")
        wait(3000)  # Warte 1 Sekunde
        self.motor_open_close.stop()
        print("Greifer gestoppt.")    

    def close(self):
        """Schließe den Greifer."""
        self.motor_open_close.run_angle(-30, -10)
        print("Greifer nach oben bewegt.")
        wait(3000)  # Warte 1 Sekunde
        self.motor_open_close.stop()
        print("Greifer gestoppt.")    