from .spRule import SpRule

class TemperatureRule(SpRule):
    """ represents the rule that will handle the temperature """

    def __init__(self, settings, display):
        super().__init__('TEMPERATURE_RULE', settings)
        self.display = display

    def execute(self):
        raw_value = SpRule.execute(self)

        voltage = raw_value * 3.3
        voltage /= 1024.0
        tempCelsius = (voltage-0.5)*100

        self.display.write(tempCelsius)
