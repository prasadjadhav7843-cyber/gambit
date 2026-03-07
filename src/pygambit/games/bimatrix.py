"""
we created a new file for 2 player games,which be include common 2 player 
games,for example prisoner's dilemma etc.

These game are used for teaching example of game theory etc.
"""

import pygambit


def prisoners_dilemma(cooperate_reward=3, defect_temptation=5,
                      exploited_payoff=0, punishment=1):
    """
     We create an Prisoners Dilemma game.
    """
    g = pygambit.Game.new_table([2, 2])
    g.title = "Prisoner's Dilemma"

    g.players[0].label = "Player 1"
    g.players[1].label = "Player 2"

    g.players[0].strategies[0].label = "Cooperate"
    g.players[0].strategies[1].label = "Defect"       
    g.players[1].strategies[0].label = "Cooperate"
    g.players[1].strategies[1].label = "Defect"

    g[0, 0]["Player 1"] = cooperate_reward
    g[0, 0]["Player 2"] = cooperate_reward

    g[0, 1]["Player 1"] = exploited_payoff
    g[0, 1]["Player 2"] = defect_temptation

    g[1, 0]["Player 1"] = defect_temptation
    g[1, 0]["Player 2"] = exploited_payoff

    g[1, 1]["Player 1"] = punishment
    g[1, 1]["Player 2"] = punishment

    return g


def matching_pennies():
    """
    We create a Matching Pennies game.
    """
    g = pygambit.Game.new_table([2, 2])
    g.title = "Matching Pennies"

    g.players[0].label = "Matcher"
    g.players[1].label = "Mismatcher"

    g.players[0].strategies[0].label = "Heads"
    g.players[0].strategies[1].label = "Tails"
    g.players[1].strategies[0].label = "Heads"
    g.players[1].strategies[1].label = "Tails"

    g[0, 0]["Matcher"] = 1
    g[0, 0]["Mismatcher"] = -1

    g[0, 1]["Matcher"] = -1
    g[0,1 ]["Mismatcher"] = 1

    g[1, 0]["Matcher"] = -1
    g[1, 0 ]["Mismatcher"] = 1

    g[1, 1]["Matcher"] = 1
    g[1, 1]["Mismatcher"] = -1

    return g


def battle_of_the_sexes(preferred=2, nonpreferred=1):
    """
    We create a battle of the sexes game
    """
    g = pygambit.Game.new_table([2, 2])
    g.title = "Battle of the Sexes"

    g.players[0].label = "Player 1"
    g.players[1].label = "Player 2"

    g.players[0].strategies[0].label = "Opera"
    g.players[0].strategies[1].label = "Football"
    g.players[1].strategies[0].label = "Opera"
    g.players[1].strategies[1].label = "Football"

    g[0, 0]["Player 1"] = preferred
    g[0, 0]["Player 2"] = nonpreferred  

    g[0, 1]["Player 1"] = 0
    g[0, 1]["Player 2"] = 0     

    g[1, 0]["Player 1"] = 0
    g[1, 0]["Player 2"] = 0

    g[1, 1]["Player 1"] = nonpreferred
    g[1, 1]["Player 2"] = preferred

    return g


def coordination_game(reward=2, mismatch=0):
    """
    We create a coordination game
    """
    g = pygambit.Game.new_table([2, 2])
    g.title = "Coordination Game"

    g.players[0].label = "Player 1"
    g.players[1].label = "Player 2"

    g.players[0].strategies[0].label = "A"
    g.players[0].strategies[1].label = "B"
    g.players[1].strategies[0].label = "A"
    g.players[1].strategies[1].label = "B"

    g[0, 0]["Player 1"] = reward
    g[0, 0]["Player 2"] = reward

    g[0, 1]["Player 1"] = mismatch
    g[0, 1]["Player 2"] = mismatch

    g[1, 0]["Player 1"] = mismatch
    g[1, 0]["Player 2"] = mismatch

    g[1, 1]["Player 1"] = reward
    g[1, 1]["Player 2"] = reward

    return g


def rock_paper_scissors():  
    """
    We create a rock paper scissors game
    """
    g = pygambit.Game.new_table([3, 3])
    g.title = "Rock Paper Scissors"

    g.players[0].label = "Player 1"
    g.players[1].label = "Player 2"

    g.players[0].strategies[0].label = "Rock"
    g.players[0].strategies[1].label = "Paper"
    g.players[0].strategies[2].label = "Scissors"
    g.players[1].strategies[0].label = "Rock"
    g.players[1].strategies[1].label = "Paper"
    g.players[1].strategies[2].label = "Scissors"

    g[0, 0]["Player 1"] = 0
    g[0, 0]["Player 2"] = 0

    g[0, 1]["Player 1"] = -1
    g[0, 1]["Player 2"] = 1

    g[0, 2]["Player 1"] = 1
    g[0, 2]["Player 2"] = -1

    g[1, 0]["Player 1"] = 1
    g[1, 0]["Player 2"] = -1

    g[1, 1]["Player 1"] = 0
    g[1, 1]["Player 2"] = 0

    g[1, 2]["Player 1"] = -1
    g[1, 2]["Player 2"] = 1

    g[2, 0]["Player 1"] = -1
    g[2, 0]["Player 2"] = 1

    g[2, 1]["Player 1"] = 1
    g[2, 1]["Player 2"] = -1

    g[2, 2]["Player 1"] = 0
    g[2, 2]["Player 2"] = 0 

    return g


def ranking_game(m=2):
    """
    We create a Ranking game with m effort levels.
    """
    g = pygambit.Game.new_table([m, m])
    g.title = "Ranking Game"

    g.players[0].label = "Player 1"
    g.players[1].label = "Player 2"

    g.players[0].strategies[0].label = "Effort 1"
    g.players[0].strategies[1].label = "Effort 2"
    g.players[1].strategies[0].label = "Effort 1"
    g.players[1].strategies[1].label = "Effort 2"

    g[0, 0]["Player 1"] = 0
    g[0, 0]["Player 2"] = 0

    g[0, 1]["Player 1"] = -1
    g[0, 1]["Player 2"] = 0

    g[1, 0]["Player 1"] = 0
    g[1, 0]["Player 2"] = -1

    g[1, 1]["Player 1"] = -1
    g[1, 1]["Player 2"] = -1

    return g


def sgc_game(m=3):
    """
    We create an SGC game.
    """
    g = pygambit.Game.new_table([m, m])
    g.title = "SGC Game"

    g.players[0].label = "Player 1"
    g.players[1].label = "Player 2"

    g.players[0].strategies[0].label = "Action 1"
    g.players[0].strategies[1].label = "Action 2"
    g.players[0].strategies[2].label = "Action 3"
    g.players[1].strategies[0].label = "Action 1"
    g.players[1].strategies[1].label = "Action 2"
    g.players[1].strategies[2].label = "Action 3"

    g[0, 0]["Player 1"] = 0
    g[0, 0]["Player 2"] = 0

    g[0, 1]["Player 1"] = 0
    g[0, 1]["Player 2"] = 1

    g[0, 2]["Player 1"] = 0
    g[0, 2]["Player 2"] = 1

    g[1, 0]["Player 1"] = 1
    g[1, 0]["Player 2"] = 0

    g[1, 1]["Player 1"] = 0
    g[1, 1]["Player 2"] = 0

    g[1, 2]["Player 1"] = 0
    g[1, 2]["Player 2"] = 1

    g[2, 0]["Player 1"] = 1
    g[2, 0]["Player 2"] = 0

    g[2, 1]["Player 1"] = 1
    g[2, 1]["Player 2"] = 0

    g[2, 2]["Player 1"] = 0
    g[2, 2]["Player 2"] = 0

    return g
