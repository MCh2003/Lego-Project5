#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Initialize EV3 brick
ev3 = EV3Brick()

# Initialize color sensor on port 2
cs = ColorSensor(Port.S2)

# Dictionary to map color values
color_names = {
    Color.BLACK: "Black",
    Color.BLUE: "Blue",
    Color.GREEN: "Green",
    Color.YELLOW: "Yellow",
    Color.RED: "Red",
    Color.WHITE: "White",
    Color.BROWN: "Brown",
    None: "No Color"
}

# Sound the beep to start
ev3.speaker.beep()

while True:
    detected_color = cs.color()  # Get the detected color
    print(detected_color)  # Print the numeric color value
    wait(1000)  # Wait for 1 second before checking again


while cs.reflection() > 15:
    ev3.speaker.beep()
    wait(2)

