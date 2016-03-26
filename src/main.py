from ruleEngine import RuleEngine
from spInterface import SpInterface
from display import Display
from api import CommonApi, LedApi;
from rules import HumidityRule, TemperatureRule, LuminosityRule, PsutilRule, ButtonRule

from collections import namedtuple

def main():

    sp_interface = SpInterface()
    Settings = namedtuple('Settings', 'periodicity sp_interface pin_no number_of_reads time_between_reads')

    temp_rule = TemperatureRule(Settings(10*60, sp_interface, 0, 5, 2), [Display('temperature'), CommonApi('temperatures')])
    humidity_rule = HumidityRule(Settings(15*60, sp_interface, 1, 5, 2), [Display('humidity'), CommonApi('humidities')])
    luminosity_rule = LuminosityRule(Settings(7*60, sp_interface, 2, 5, 2), [Display('luminosity'), CommonApi('luminosities')])
    # psutil_rule = PsutilRule(4*60, [Display('cpu'), Display('memory')])

    led_displays = [Display('blue_led'), Display('red_led'), Display('green_led'), Display('yellow_led')]
    led_apis = [LedApi(color=2), LedApi(color=1), LedApi(color=4), LedApi(color=3)]
    button_rule = ButtonRule(Settings(1*60, sp_interface, 3, 0, 0), led_displays + led_apis)

    # add the rules
    rule_engine = RuleEngine()
    rule_engine.add_many([button_rule, temp_rule, humidity_rule, luminosity_rule])

    # fire up the engine
    rule_engine.execute()

if __name__ == '__main__':
    main()
