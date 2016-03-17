from ruleEngine import RuleEngine
from rules.humidityRule import HumidityRule
from rules.temperatureRule import TemperatureRule
from rules.luminosityRule import LuminosityRule

def main():
    ruleEngine = RuleEngine()

    ruleEngine.add(HumidityRule())
    ruleEngine.add(TemperatureRule())
    ruleEngine.add(LuminosityRule())
    ruleEngine.execute()

main()
