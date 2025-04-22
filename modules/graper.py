from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from constants.constants import Ports, Sensors
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait

class Graper:
    """Greifer-Klasse, die den Greifer des Roboters verwaltet."""
    def __init__(self):
        print("Initializing Graper...")
        self.motor_up_down = Motor(Ports.MOTOR_GRAPPER_UP_DOWN)
        print("Motor Up Down initialized")
        self.motor_open_close = Motor(Ports.MOTOR_GRAPPER_OPEN_CLOSE)
    
    def is_block_detected(self):
        return self.ultrasoncic_sensor.distance() < Sensors.OBSTACLE_DISTANCE

    def move_up(self):
        """Bewege den Greifer nach oben."""
        self.motor_up_down.run_target(100, -90, Stop.HOLD, False)  # Move to 90 degrees
        wait(3000)
        print("Greifer nach oben bewegt.")
        self.motor_up_down.stop()  
        print("Greifer gestoppt.")
    
    def move_down(self):
        """Bewege den Greifer nach unten."""
        self.motor_up_down.run_target(100, 90, Stop.HOLD, False)  # Move to 90 degrees
        print("Greifer nach unten bewegt.")
        wait(3000)  # Warte 1 Sekunde
        self.motor_up_down.stop()
        print("Greifer gestoppt.")
    
    def open(self):
        """Öffne den Greifer."""
        self.motor_open_close.run_target(10, -90, Stop.HOLD, False)  # Move to 90 degrees
        print("Greifer nach oben bewegt.")
        wait(3000)  # Warte 1 Sekunde
        self.motor_open_close.stop()
        print("Greifer gestoppt.")    

    def close(self):
        """Schließe den Greifer."""
        self.motor_open_close.run_target(10, 90, Stop.HOLD, False)
        print("Greifer nach oben bewegt.")
        wait(3000)  # Warte 1 Sekunde
        self.motor_open_close.stop()
        print("Greifer gestoppt.")    