import RPi.GPIO as GPIO
from .rule import Rule
import random

class ButtonRule(Rule):
    """ represents the rule that will handle the button press event """

    def __init__(self, settings, periodicity, displays):
        super().__init__('BUTTON_RULE', settings.periodicity)
        self.settings = settings
        self.displays = displays

        GPIO.setmode(GPIO.BCM)

        self.pins = {4: 'blue', 17: 'red', 27: 'green', 22: 'yellow'}
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT)

    def execute(self):
        current_value = self.settings.sp_interface.readADC(self.settings.pin_no)

        if (current_value == 1023):
            random_index = random.randint(0, len(self.pins) - 1)

            index = 0
            for pin, color in self.pins.items():
                # turn on led
                GPIO.output(pin, True)
                # send data to display
                self.displays[index].write( (index + 1) * 2)
                time.sleep(0.5)
                # turn off led
                GPIO.output(pin, False)

                index = index + 1
                if index >= random_index:
                    break;

























    def execute(self):



        for display, param in zip(self.displays, params):
            display.write(param)

if __name__ == '__main__':
    rule = PsutilRule(10)
    rule.execute()
