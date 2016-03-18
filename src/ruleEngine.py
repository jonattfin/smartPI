import time
from datetime import datetime, timedelta

class RuleEngine(object):
    """ The rule engine keeps a number of rules, and executes them by time"""

    def __init__(self):
        """create a new rule engine"""
        self.rules = []
        self.rules_executions_time = {}

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

    def execute_rule_and_keep_time(self, rule):
        try:
            rule.execute()
            self.rules_executions_time[rule.id] = datetime.now()
        except Exception as e:
            # todo
            pass

    def execute(self):
        """execute the rules from the rule engine."""

        while True:
            for rule in self.rules:
                if not rule.id in self.rules_executions_time:
                    self.execute_rule_and_keep_time(rule)

                rule_execution_time = self.rules_executions_time[rule.id]

                if (datetime.now() - rule_execution_time).seconds >= rule.periodicity:
                    self.execute_rule_and_keep_time(rule)

            time.sleep(1)
