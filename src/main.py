
import time
from collections import namedtuple

from ruleEngine import RuleEngine
from spInterface import SpInterface
from display import Display
from api import CommonApi

from rules import HumidityRule, TemperatureRule, LuminosityRule, MQ135Rule
from rules import MotionRule, CameraRule
from rules import PsutilRule

from collections import namedtuple

import requests
import json
from datetime import datetime


def main():

    sp_interface = SpInterface()
    Settings = namedtuple(
        'Settings', 'periodicity sp_interface pin_no number_of_reads time_between_reads')

    temp_rule = TemperatureRule(
        Settings(10*60, sp_interface, 0, 3, 2), [Display('temperature')])
    humidity_rule = HumidityRule(
        Settings(15*60, sp_interface, 1, 3, 2), [Display('humidity')])
    luminosity_rule = LuminosityRule(
        Settings(7*60, sp_interface, 2, 3, 2), [Display('luminosity')])
    mq135_rule = MQ135Rule(
        Settings(2*60, sp_interface, 4, 2, 2), [Display('mq135')])

    print('reading location...')

    send_url = 'http://freegeoip.net/json'

    r = requests.get(send_url)
    j = json.loads(r.text)
    lat = j['latitude']
    long = j['longitude']

    print('location is ', lat, long)

    while True:
        print('reading sensors...')

        temperature = temp_rule.read()
        convertedTemp = temp_rule.convert(temperature)

        humidity = humidity_rule.read()
        luminosity = luminosity_rule.read()
        gas = mq135_rule.read()

        params = {
            'guid': 'eb203991-4b2a-4950-b57c-18f397315a78',
            'latitude': lat,
            'longitude': long,
            'timespan': datetime.now(),
            'temperature': convertedTemp, 'humidity': humidity,
            'luminosity': luminosity, 'co2': gas}

        print('sending data to heroku...')

        api = CommonApi('https://api-cleanaircluj.herokuapp.com/api/Resources')
        api.write(params)

        time.sleep(60)


if __name__ == '__main__':
    main()
