#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

class ColorDetector:
    def __init__(self, port=Port.S3):
        # Initialisiert den Farbsensor am angegebenen Port.
        self.sensor = ColorSensor(port)

    def get_color(self):
        # Versucht zuerst, den vordefinierten Farbwert zu lesen.
        detected = self.sensor.color()
        if detected is not None:
            return detected
        # Falls keine vordefinierte Farbe erkannt wird, lese die RGB-Werte.
        return self.sensor.rgb()

def main():
    ev3 = EV3Brick()
    ev3.speaker.beep()
    color_detector = ColorDetector()  # Standardmäßig Port.S3

    while True:
        color = color_detector.get_color()
        print("Erkannte Farbe/Werte:", color)
        wait(500)

if __name__ == '__main__':
    main()
