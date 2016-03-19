from .spRule import SpRule

class HumidityRule(SpRule):
    """ represents the rule that will handle the humidity """

    def __init__(self, settings, display):
        super().__init__('HUMIDITY_RULE', settings)
        self.display = display

    def execute(self):
        raw_value = SpRule.execute(self)
        self.display.write(raw_value)
