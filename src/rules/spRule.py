from .rule import Rule
import time

class SpRule(Rule):
    """ represents the SP base class rule implemented by SP rules """

    def __init__(self, id, settings):
        """ sets the parameters needed by the rule """

        super().__init__(id, settings.periodicity)
        self.settings = settings

    def execute(self):
        """ execute the rule """
        values = []

        # we'll do more than one read to calculate an average of the readings
        for i in range(self.settings.number_of_reads):

            # read the current value from the sp interface
            current_value = self.settings.sp_interface.readADC(self.settings.pin_no)
            values.append(current_value)

            time.sleep(self.settings.time_between_reads)

        # calculate the average, and rounds it to 2 decimals
        value = round((sum(values) / len(values)), 2)
        print('sending rawValue {0} for rule {1}', format(value, self.id))
        return value
