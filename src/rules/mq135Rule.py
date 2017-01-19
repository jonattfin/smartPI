from .spRule import SpRule

class MQ135Rule(SpRule):
    """ represents the rule that will handle the MQ135 sensor """

    def __init__(self, settings, displays):
        super().__init__('MQ135', settings, displays)
