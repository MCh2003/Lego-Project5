from ..modules.robot import Robot

class ExampleModule:
    def __init__(self, robot: Robot):
        self.robot = robot

    def example(self):
        self.robot.ev3.speaker.beep()
        self.robot.driving_unit.startMoving()
        self.robot.graper.detect_and_grap()