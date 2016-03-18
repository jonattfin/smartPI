from ruleEngine import RuleEngine
from spInterface import SpInterface
from display import Display
from rules import HumidityRule, TemperatureRule, LuminosityRule

def main():
    rule_engine = RuleEngine()
    sp_interface = SpInterface()

    humidity_display = Display('humidity')
    rule_engine.add(HumidityRule(periodicity=10, sp_interface=sp_interface, pin_no=1, display=humidity_display))

    temperature_display = Display('temperature')
    rule_engine.add(TemperatureRule(periodicity=10, sp_interface=sp_interface, pin_no=0, display=temperature_display))

    luminosity_display = Display('luminosity')
    rule_engine.add(LuminosityRule(periodicity=10, sp_interface=sp_interface, pin_no=0, display=luminosity_display))

    rule_engine.execute()

if __name__ == '__main__':
    main()
