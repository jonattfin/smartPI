from .spRule import SpRule

class HumidityRule(SpRule):
    """ represents the rule that will handle the humidity """

    def __init__(self, settings, displays):
        super().__init__('HUMIDITY_RULE', settings, displays)
