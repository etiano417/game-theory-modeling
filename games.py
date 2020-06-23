class NormalFormGame:
    """
    construct a new normal form game

    takes a list of player names, an actions list corresponding to the 
    list of players, and a rules function mapping tuples of actions to 
    tuples of payoffs.
    """
    def __init__(players, actions, rules):
        if not validate_game_parameters(players, actions, rules):
            raise ValueError("bad model parameters")
        this.players = players
        this.actions = actions
        this.rules = rules

    def validate_game_parameters(players, actions, rules):
        valid = players.len > 0
        valid = valid and actions.len == players.len
        return valid
        
