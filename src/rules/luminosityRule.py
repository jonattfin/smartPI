from .spRule import SpRule

class LuminosityRule(SpRule):
    """ represents the rule that will handle the luminosity """

    def __init__(self, settings, displays):
        super().__init__('LUMINOSITY_RULE', settings, displays)
