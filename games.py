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
    give a list of actions performed by each player, return the given 
    player's payoff
    """
    def payoff(self, player, actions):
        payoffs = self.rules(actions) 
        player_number = self.players.index(player)
        player_payoff = payoffs[player_number]
        return player_payoff

        
         
        
