from .spRule import SpRule

class MotionRule(SpRule):
    """ represents the rule that will handle the motion """

    def __init__(self, settings, displays):
        super().__init__('MOTION_RULE', settings, displays)
