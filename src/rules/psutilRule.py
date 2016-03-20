import psutil

from .rule import Rule

class PsutilRule(Rule):
    """ represents the rule that will handle the computer resources """

    def __init__(self, periodicity, displays):
        super().__init__('PSUTIL_RULE', periodicity)
        self.displays = displays

    def execute(self):
        params = [
            psutil.cpu_percent(),
            psutil.virtual_memory().percent
        ]

        for display, param in zip(self.displays, params):
            print(param)
            # self.display.write(param)

if __name__ == '__main__':
    rule = PsutilRule(10)
    rule.execute()
