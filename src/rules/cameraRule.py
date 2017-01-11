from picamera import PiCamera
from time import sleep
from datetime import datetime
import distutils.dir_util
import os

from .rule import Rule

class CameraRule(Rule):
    """ represents the rule that will take pictures """

    def __init__(self, periodicity, displays):
        super().__init__('CAMERA_RULE', periodicity)
        self.displays = displays
        self.camera = PiCamera()

    def create_image(self):
        now = datetime.now()

        filename = now.strftime("%H.%M.%S_%Y-%m-%d.jpg")
        path = '{0}_{1}'.format(now.month, now.day)

        distutils.dir_util.mkpath(path)
        self.camera.capture(os.path.join(path, filename))

    def execute(self):
        self.create_image()
        sleep(5)

        for display in self.displays:
            display.write(0)
            sleep(0.5)
            display.write(10)
            sleep(0.5)
            display.write(0)



