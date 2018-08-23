from ruleEngine import RuleEngine
from spInterface import SpInterface
from display import Display
from api import CommonApi, LedApi

from rules import HumidityRule, TemperatureRule, LuminosityRule, MQ135Rule, MoistureRule
# from rules import MotionRule, CameraRule
from rules import PsutilRule

from collections import namedtuple

def main():

    sp_interface = SpInterface()
    Settings = namedtuple('Settings', 'periodicity sp_interface pin_no number_of_reads time_between_reads')

    temp_rule = TemperatureRule(Settings(10*60, sp_interface, 0, 5, 2), [Display('temperature')])
    humidity_rule = HumidityRule(Settings(15*60, sp_interface, 2, 5, 2), [Display('humidity')])
    luminosity_rule = LuminosityRule(Settings(7*60, sp_interface, 4, 5, 2), [Display('luminosity')])
    moisture_rule = MoistureRule(Settings(5*60, sp_interface, 6, 3, 2), [Display('moisture')])

    # motion_rule = MotionRule(Settings(1*60, sp_interface, 3, 5, 2), [Display('presence')])
    # mq135_rule = MQ135Rule(Settings(2*60, sp_interface, 4, 3, 2), [Display('mq135')])
    # camera_rule = CameraRule(1*60, [Display('image')])
    # psutil_rule = PsutilRule(4*60, [Display('cpu'), Display('memory'), Display('hdd')])

    # led_displays = [Display('blue_led'), Display('red_led'), Display('green_led'), Display('yellow_led')]
    # led_apis = [LedApi(color=2), LedApi(color=1), LedApi(color=4), LedApi(color=3)]
    # button_rule = ButtonRule(Settings(1*60, sp_interface, 3, 0, 0), led_displays)

    # add the rules
    rule_engine = RuleEngine()
    rule_engine.add_many([temp_rule, humidity_rule, luminosity_rule, moisture_rule])

    # fire up the engine
    rule_engine.execute()

if __name__ == '__main__':
    main()
