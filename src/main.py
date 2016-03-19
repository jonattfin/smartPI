from ruleEngine import RuleEngine
from spInterface import SpInterface
from display import Display
from rules import HumidityRule, TemperatureRule, LuminosityRule

from collections import namedtuple

def main():
    rule_engine = RuleEngine()
    sp_interface = SpInterface()

    Settings = namedtuple('Settings', 'periodicity sp_interface pin_no number_of_reads time_between_reads')

    temp_rule = TemperatureRule(Settings(10*60, sp_interface, 0, 6, 10), Display('temperature'))
    humidity_rule = HumidityRule(Settings(10*60, sp_interface, 1, 6, 10), Display('humidity'))
    luminosity_rule = LuminosityRule(Settings(5*60, sp_interface, 2, 6, 10), Display('luminosity'))

    # add the rules
    rule_engine.add_many([humidity_rule, temp_rule, luminosity_rule])

    # fire up the engine
    rule_engine.execute()

if __name__ == '__main__':
    main()
