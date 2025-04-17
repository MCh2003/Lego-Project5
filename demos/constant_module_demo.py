from pybricks.hubs import EV3Brick

class ExampleModule:
    def __init__(self, brick: EV3Brick):
        self.brick = brick

    def example(self):
        self.brick.speaker.set_volume(100)
        self.brick.speaker.beep()
        self.foo = "Hello World"