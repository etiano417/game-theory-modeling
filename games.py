import pdb

class DecisionProblem:
    """
    A choice a rational actor faces
    
    Properties:
        actions -- a set of actions available to the player
        outcome -- a function that accepts actions and returns outcomes
            (must be defined for every action)
        preference -- a function comparing two outcomes
    """
    def __init__(self, actions, outcome_function, preference_function): 
        if(actions == None):
            raise TypeError("must include actions set")
        if(outcome_function == None):
            raise TypeError("must include outcome function")
        
        outcomes = []
        for action in actions:
            outcome = outcome_function(action)
            outcomes.append(outcome)
            if(outcome == None):
                raise ValueError("outcome function not defined for action: " + action)

        if(len(actions) == 0):
            raise ValueError("actions set must not be empty")

        preferences_complete = check_preference_completeness(outcomes, preference_function)

        if(not preferences_complete):
            raise ValueError("preference function not defined for outcome: " + outcome_1 + "+" + outcome_2)

        self.actions = actions
        self.outcome_function = outcome_function
        self.preference_function = preference_function

def check_preference_completeness(outcomes, preference_function): 
    preferences_complete = True

    for outcome_1 in outcomes:
        for outcome_2 in outcomes:
            preference = preference_function(outcome_1, outcome_2)
            if(preference == None):
                preferences_complete = False

    return preferences_complete
    
class NormalFormGame:
    """
    construct a new normal form game

    takes a list of player names, an actions list corresponding to the 
    list of players, and a rules function mapping lists of actions to 
    lists of payoffs.
    """
    def __init__(self, players, actions, rules):
    
        valid = len(players) > 0
        valid = valid and len(actions) == len(players)

        if not valid:
            raise ValueError("bad model parameters")
        self.players = players
        self.actions = actions
        self.rules = rules

    """
    given a list of actions performed by each player, return the given 
    player's payoff
    """
    def payoff(self, player, actions):
        payoffs = self.rules(actions) 
        player_number = self.players.index(player)
        player_payoff = payoffs[player_number]
        return player_payoff

    """
    given a player and a dictionary mapping the other players in the game to actions, 
    show the best action for the given player
    """
    def best_response(self, responding_player, opponent_actions):

        #create a list of actions chosen by each player
        chosen_actions = []
        for player in self.players:
            if player != responding_player: 
                chosen_actions.append(opponent_actions[player])
            else: chosen_actions.append("")        
        
        pdb.set_trace()

        #find the index of the responding player
        responding_player_index = self.players.index(responding_player)

        #find the payoff of each of the player's potential actions
        payoffs = []
        for action in self.actions[responding_player_index]:
            chosen_actions[responding_player_index] = action
            result = self.rules(chosen_actions)
            payoff = result[responding_player_index]
            payoffs.append(payoff)

        #find which payoff is highest
        highest_payoff_index = -999
        highest_payoff = -10000000000000000
        for i in range(len(payoffs)):
            payoff = payoffs[i]
            if(payoff > highest_payoff):
                highest_payoff = payoff
                highest_payoff_index = i
        highest_payoff_action = self.actions[responding_player_index][highest_payoff_index]
        return highest_payoff_action
        
