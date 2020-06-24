import pdb

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
        
