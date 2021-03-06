from .rule import Rule
import time

class SpRule(Rule):
    """ represents the SP base class rule implemented by SP rules """

    def __init__(self, id, settings, displays):
        """ sets the parameters needed by the rule """

        super().__init__(id, settings.periodicity)
        self.settings = settings
        self.displays = displays

    def convert(self, value):
        return value;

    def read(self):
        """ execute the rule """
        values = []

        # we'll do more than one read to calculate an average of the readings
        for i in range(self.settings.number_of_reads):

            # read the current value from the sp interface
            current_value = self.settings.sp_interface.readADC(self.settings.pin_no)
            values.append(current_value)

            time.sleep(self.settings.time_between_reads)

        # calculate the average, and rounds it to 2 decimals
        return round((sum(values) / len(values)), 2)

    def execute(self):
        value = self.read()
        converted_value = self.convert(value)

        for display in self.displays:
            display.write(converted_value)
