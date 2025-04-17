from ..modules.robot import Robot
from ..constants.constants import EV3Speaker
from .constant_module_demo import ExampleModule

robot = Robot()

robot.ev3.speaker.set_volume(EV3Speaker.VOLUME)
# 500 is the default frequency in Hz
robot.ev3.speaker.beep(500, EV3Speaker.BEEP_DURATION)