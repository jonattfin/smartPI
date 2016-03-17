
class TemperatureRule(object):
    """ represents the rule that will handle the temperature """

    def __init__(self):
        self.id = 'TEMPERATURE_RULE'
        self.periodicity = 5

    def execute(self):
        print('temperature rule executed')
