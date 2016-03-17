
class LuminosityRule(object):
    """ represents the rule that will handle the luminosity """

    def __init__(self):
        self.id = 'LUMINOSITY_RULE'
        self.periodicity = 3

    def execute(self):
        print('luminosity rule executed')
