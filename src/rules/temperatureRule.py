from .spRule import SpRule

class TemperatureRule(SpRule):
    """ represents the rule that will handle the temperature """

    def __init__(self, settings, displays):
        super().__init__('TEMPERATURE_RULE', settings, displays)

    def convert(self, value):
        voltage = raw_value * 3.3
        voltage /= 1024.0
        tempCelsius = (voltage-0.5)*100

        return tempCelsius
