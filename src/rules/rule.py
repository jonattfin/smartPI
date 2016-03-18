
class Rule(object):
    """ represents the base class rule implemented by all other rules """

    def __init__(self, id, periodicity):
        """ sets the parameters needed by the rule """
        self.id = id
        self.periodicity = periodicity

    def execute(self):
        """ execute the rule """
        pass
