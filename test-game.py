import unittest
from games import DecisionProblem

action_1 = "left"
action_2 = "middle"
action_3 = "right"

outcome_1 = "Boston"
outcome_2 = "New York"
outcome_3 = "Cleveland"

class DecisionProblemConstruction(unittest.TestCase):
        
    def setUp(self):
        self.actions = frozenset([action_1, action_2, action_3])
        
    def outcome_function(self, action): 
        outcome_map = {
            action_1: outcome_1,
            action_2: outcome_2,
            action_3: outcome_3,
        }
            
        return outcome_map[action]

    def incomplete_outcome_function(self, action): 
        outcome_map = {
            action_1: outcome_1,
            action_3: outcome_3,
        }
            
        return outcome_map[action]     
    
    def preference_function(self, outcome_first, outcome_second):
        preference_map = {
            (outcome_1,outcome_1): 0,
            (outcome_1,outcome_2): 1,
            (outcome_1,outcome_3): 1,
            (outcome_2,outcome_1): -1,
            (outcome_2,outcome_2): 0,
            (outcome_2,outcome_3): 1,
            (outcome_3,outcome_1): -1,
            (outcome_3,outcome_2): -1,
            (outcome_3,outcome_3): 0,
        }

        return  preference_map[(outcome_first, outcome_second)]
   
    def incomplete_preference_function(self, outcome_first, outcome_second):
        preference_map = {
            (outcome_1,outcome_1): 0,
            (outcome_1,outcome_2): 1,
            (outcome_1,outcome_3): 1,
            (outcome_2,outcome_2): 0,
            (outcome_2,outcome_3): 1,
            (outcome_3,outcome_1): -1,
            (outcome_3,outcome_2): -1,
            (outcome_3,outcome_3): 0,
        }

        return  preference_map[(outcome_first, outcome_second)]

    def test_construction(self):
        assert DecisionProblem(self.actions, self.outcome_function, 
            self.preference_function) != None

    def test_construction_missing_actions(self):
        with self.assertRaises(Exception):
            DecisionProblem(None, self.outcome_function, self.preference_function)

    def test_construction_no_actions(self):
        with self.assertRaises(ValueError):
            DecisionProblem(frozenset([]), self.outcome_function, self.preference_function)

    def test_construction_missing_outcome_function(self):
        with self.assertRaises(Exception):
            DecisionProblem(self.actions, None, self.preference_function)

    def test_construction_undefined_outcomes(self):
        with self.assertRaises(Exception):
            DecisionProblem(self.actions, self.incomplete_outcome_function, self.preference_function)

    def test_construction_undefined_preferences(self):
        with self.assertRaises(Exception):
            DecisionProblem(self.actions, self.outcome_function, self.incomplete_preference_function)


if __name__ == "__main__":
    unittest.main()
        
