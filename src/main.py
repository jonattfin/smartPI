from ruleEngine import RuleEngine
from spInterface import SpInterface
from display import Display
from rules import HumidityRule, TemperatureRule, LuminosityRule

from collections import namedtuple

def main():
    rule_engine = RuleEngine()
    sp_interface = SpInterface()

    Settings = namedtuple('Settings', 'periodicity sp_interface pin_no number_of_reads time_between_reads')

    rule_engine.add(HumidityRule(Settings(3, sp_interface, 1, 1, 1), Display('humidity')))
    rule_engine.add(TemperatureRule(Settings(5, sp_interface, 0, 1, 1), Display('temperature')))
    rule_engine.add(LuminosityRule(Settings(10, sp_interface, 0, 1, 1), Display('luminosity')))

    rule_engine.execute()

if __name__ == '__main__':
    main()
