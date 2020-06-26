import unittest
from games import DecisionProblem

action_1a = "left"
action_1b = "middle"
action_1c = "right"

outcome_1a = "Boston"
outcome_1b = "New York"
outcome_1c = "Cleveland"

class DecisionProblemConstruction(unittest.TestCase):
        
    def setUp(self):
        self.actions_1 = frozenset([action_1a, action_1b, action_1c])
        
    def outcome_function_1(self, action): 
        outcome_map = {
            action_1a: outcome_1a,
            action_1b: outcome_1b,
            action_1c: outcome_1c,
        }
            
        return outcome_map(action)
        
    def preference_function_1(self, outcome):
        preference_map = {
            outcome_1a: -1,
            outcome_1b: 0,
            outcome_1c: 1,
        }
        
        return preference_map(outcome)
    
    def test_construction(self):
        assert DecisionProblem(self.actions_1, self.outcome_function_1, 
            self.preference_function_1) != None
            
if __name__ == "__main__":
    unittest.main()
        