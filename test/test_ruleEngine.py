from unittest import TestCase
from src.ruleEngine import RuleEngine
from src.rules.rule import Rule

class RuleEngineTestCase(TestCase):
	def setUp(self):
		self.ruleEngine = RuleEngine()

	def test_zero_rules_on_new_rule_engine(self):
		self.assertTrue(self.ruleEngine.length == 0)

	def test_add_one_rule_to_the_rule_engine(self):
		self.ruleEngine.add(())
		self.assertTrue(self.ruleEngine.length == 1)

	def test_add_many_rules_to_the_rule_engine(self):
		self.ruleEngine.add_many([(), (), ()])
		self.assertTrue(self.ruleEngine.length == 3)

	def test_execute_all_the_rules(self):
		rules=[]
		rules.append(Rule(periodicity=3))
		rules.append(Rule(periodicity=5))

		self.ruleEngine.add_many(rules)
		self.assertTrue(self.ruleEngine.execute() == 2)
