from picamera import PiCamera
from time import sleep
from datetime import datetime

from .rule import Rule

class CameraRule(Rule):
    """ represents the rule that will take pictures """

    def __init__(self, periodicity, displays):
        super().__init__('CAMERA_RULE', periodicity)
        self.displays = displays
        self.camera = PiCamera()

    def execute(self):
        filename = datetime.now().strftime("%H.%M.%S_%Y-%m-%d.jpg")
        self.camera.capture(filename)
        sleep(5)

        display.write(0)
        display.write(1 * 10)
        display.write(0)



