from ..modules.robot import Robot
from .constant_module_demo import ExampleModule

robot = Robot()
demoFunction = ExampleModule(robot)

robot.ev3.speaker.beep()
demoFunction.example()