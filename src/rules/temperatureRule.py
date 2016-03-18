from .spRule import SpRule

class TemperatureRule(SpRule):
    """ represents the rule that will handle the temperature """

    def __init__(self, periodicity, sp_interface, pin_no, display):
        super().__init__('TEMPERATURE_RULE', periodicity, sp_interface, pin_no)
        self.display = display

    def execute(self):
        raw_value = SpRule.execute(self)

        voltage = value * 3.3
        voltage /= 1024.0
        tempCelsius = (voltage-0.5)*100

        self.display.write(tempCelsius)
