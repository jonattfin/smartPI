
class Rule(object):
    """ represents the base class rule implemented by all other rules """

    def __init__(self, rule_id, periodicity=0):
        """ sets the parameters needed by the rule """
        self.rule_id = rule_id
        self.periodicity = periodicity

    def execute(self):
        """ execute the rule """
        pass
