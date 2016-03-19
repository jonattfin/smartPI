from .spRule import SpRule

class LuminosityRule(SpRule):
    """ represents the rule that will handle the luminosity """

    def __init__(self, settings, display):
        super().__init__('LUMINOSITY_RULE', settings)
        self.display = display

    def execute(self):
        raw_value = SpRule.execute(self)
        self.display.write(raw_value)
