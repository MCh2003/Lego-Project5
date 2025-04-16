#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.parameters import Port
from drivingUnit import DrivingUnit  # DrivingUnit self.robot verwendet.
from grap import Graper  # Erweiterte Version mit einer release()-Methode
from pybricks.ev3devices import ColorSensor

# Farbsensor-Klasse
class ColorDetector:
    def __init__(self, port=Port.S3):
        self.sensor = ColorSensor(port)

    def get_color(self):
        # Liefert eine voreingestellte Farbe oder, falls keiner erkannt wird, die RGB-Werte.
        col = self.sensor.color()
        if col is not None:
            return col
        return self.sensor.rgb()

# Einfache Funktionen zum Fahren zwischen Such- und Stapelbereich.
def go_to_stack_area(driving):
    print("Fahre zum Stapelbereich...")
    driving.startMoving()  # Zum Beispiel eine Geradeausfahrt
    wait(1000)

def go_to_search_area(driving):
    print("Fahre zurück zum Suchbereich...")
    driving.startMoving()
    wait(1000)

def main():
    ev3 = EV3Brick()
    ev3.speaker.beep()
    
    driving = DrivingUnit()
    graper = Graper()  # Greifer: motor an Port.A, Sensor an Port.S2
    color_detector = ColorDetector()  # Farbsensor an Port.S3

    target_color = None  # Ziel-Farbe wird beim ersten erkannten Block gesetzt

    while True:
        current_color = color_detector.get_color()
        print("Erkannte Farbe:", current_color)
        
        if current_color is not None:
            if target_color is None:
                target_color = current_color
                print("Ziel-Farbe festgelegt:", target_color)
            
            if current_color == target_color:
                print("Block entspricht der Ziel-Farbe.")
                # Greifen des Blocks
                graper.detect_and_grap()
                # Zum Stapelbereich fahren
                go_to_stack_area(driving)
                # Block ablegen (release-Methode in grap.py muss implementiert sein)
                graper.release_object()
                # Zurück zum Suchbereich
                go_to_search_area(driving)
            else:
                print("Block hat nicht die Ziel-Farbe. Ignoriere den Block.")
        wait(500)

if __name__ == '__main__':
    main()
