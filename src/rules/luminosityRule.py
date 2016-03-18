from .spRule import SpRule

class LuminosityRule(SpRule):
    """ represents the rule that will handle the luminosity """

    def __init__(self, periodicity, sp_interface, pin_no, display):
        super().__init__('LUMINOSITY_RULE', periodicity. sp_interface, pin_no)
        self.display = display

    def execute(self):
        raw_value = SpRule.execute(self)
        # transform the value
        self.display.write(raw_value)
