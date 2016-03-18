from .rule import Rule

class SpRule(Rule):
    """ represents the SP base class rule implemented by SP rules """

    def __init__(self, id, periodicity, sp_interface, pin_no):
        """ sets the parameters needed by the rule """
        super().__init__(id, periodicity)
        self.sp_interface = sp_interface
        self.pin_no = pin_no

    def execute(self):
        """ execute the rule """
        return self.sp_interface.readADC(self.pin_no)
