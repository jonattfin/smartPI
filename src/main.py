from ruleEngine import RuleEngine
from spInterface import SpInterface
from display import Display
from rules import HumidityRule, TemperatureRule, LuminosityRule, PsutilRule, ButtonRule

from collections import namedtuple

def main():

    sp_interface = SpInterface()
    Settings = namedtuple('Settings', 'periodicity sp_interface pin_no number_of_reads time_between_reads')

    temp_rule = TemperatureRule(Settings(10*60, sp_interface, 0, 5, 2), [Display('temperature')])
    humidity_rule = HumidityRule(Settings(10*60, sp_interface, 1, 5, 2), [Display('humidity')])
    luminosity_rule = LuminosityRule(Settings(5*60, sp_interface, 2, 5, 2), [Display('luminosity')])
    psutil_rule = PsutilRule(1*60, [Display('cpu'), Display('memory')])

    led_displays = [Display('blue_led'), Display('red_led'), Display('green_led'), Display('yellow_led')]
    button_rule = ButtonRule(Settings(3, sp_interface, 3, 0, 0), led_displays)

    # add the rules
    rule_engine = RuleEngine()
    rule_engine.add_many([button_rule, psutil_rule, temp_rule, humidity_rule, luminosity_rule])

    # fire up the engine
    rule_engine.execute()

if __name__ == '__main__':
    main()
