import time
from datetime import datetime, timedelta

class RuleEngine(object):
    """ The rule engine keeps a number of rules, and executes them by time"""

    def __init__(self):
        """create a new rule engine"""
        self.rules = []
        self.ruleExecutions = {}

    @property
    def length(self):
        """returns the number of rules in the rule engine."""
        return len(self.rules)

    def add(self, rule):
        """add a new rule to the rule engine."""
        self.rules.append(rule)

    def add_many(self, rules):
        """add many rules to the rule engine."""
        self.rules.extend(rules)

    def executeRuleAndKeepTime(self, rule):
        rule.execute()
        current_time = datetime.now()
        print(current_time)
        self.ruleExecutions[rule.id] = current_time

    def execute(self):
        """execute the rules from the rule engine."""

        while True:
            for rule in self.rules:
                if not rule.id in self.ruleExecutions:
                    self.executeRuleAndKeepTime(rule)

                ruleExecutorTime = self.ruleExecutions[rule.id]

                if (datetime.now() - ruleExecutorTime).seconds >= rule.periodicity:
                    self.executeRuleAndKeepTime(rule)

            time.sleep(1)
