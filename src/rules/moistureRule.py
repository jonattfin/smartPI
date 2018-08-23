from .spRule import SpRule

class MoistureRule(SpRule):
    """ represents the rule that will handle the moisture """

    def __init__(self, settings, displays):
        super().__init__('MOISTURE_RULE', settings, displays)
