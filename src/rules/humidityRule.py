
class HumidityRule(object):
    """ represents the rule that will handle the humidity """

    def __init__(self):
        self.id = 'HUMIDITY_RULE'
        self.periodicity = 10

    def execute(self):
        print('humidity rule executed')
