"""
Generators for standard two-player (bimatrix) games.

These are commonly used as test cases and teaching examples in game theory.
Reference: http://bimatrix-games.github.io/bimatrix-generators/
"""

import pygambit


def prisoners_dilemma(cooperate_reward=3, defect_temptation=5,
                      sucker_payoff=0, punishment=1):
    """
    Create a Prisoner's Dilemma game.

    Parameters
    ----------
    cooperate_reward : int, default 3
        Payoff when both players cooperate.
    defect_temptation : int, default 5
        Payoff for defecting when opponent cooperates.
    sucker_payoff : int, default 0
        Payoff for cooperating when opponent defects.
    punishment : int, default 1
        Payoff when both players defect.

    Returns
    -------
    pygambit.Game
        A 2x2 normal form game.
    """
    g = pygambit.Game.new_table([2, 2])
    g.title = "Prisoner's Dilemma"
    g.players[0].label = "Player 1"
    g.players[1].label = "Player 2"
    g.players[0].strategies[0].label = "Cooperate"
    g.players[0].strategies[1].label = "Defect"
    g.players[1].strategies[0].label = "Cooperate"
    g.players[1].strategies[1].label = "Defect"

    # Both cooperate
    g[0, 0][0] = cooperate_reward
    g[0, 0][1] = cooperate_reward
    # P1 defects, P2 cooperates
    g[1, 0][0] = defect_temptation
    g[1, 0][1] = sucker_payoff
    # P1 cooperates, P2 defects
    g[0, 1][0] = sucker_payoff
    g[0, 1][1] = defect_temptation
    # Both defect
    g[1, 1][0] = punishment
    g[1, 1][1] = punishment

    return g


def battle_of_the_sexes(preferred=2, nonpreferred=1):
    """
    Create a Battle of the Sexes game.

    Parameters
    ----------
    preferred : int, default 2
        Payoff for attending preferred event together.
    nonpreferred : int, default 1
        Payoff for attending non-preferred event together.

    Returns
    -------
    pygambit.Game
        A 2x2 normal form game.
    """
    g = pygambit.Game.new_table([2, 2])
    g.title = "Battle of the Sexes"
    g.players[0].label = "Player 1"
    g.players[1].label = "Player 2"
    g.players[0].strategies[0].label = "Opera"
    g.players[0].strategies[1].label = "Football"
    g.players[1].strategies[0].label = "Opera"
    g.players[1].strategies[1].label = "Football"

    # Both choose Opera
    g[0, 0][0] = preferred
    g[0, 0][1] = nonpreferred
    # P1 Opera, P2 Football
    g[0, 1][0] = 0
    g[0, 1][1] = 0
    # P1 Football, P2 Opera
    g[1, 0][0] = 0
    g[1, 0][1] = 0
    # Both choose Football
    g[1, 1][0] = nonpreferred
    g[1, 1][1] = preferred

    return g


def matching_pennies():
    """
    Create a Matching Pennies game.

    Returns
    -------
    pygambit.Game
        A 2x2 zero-sum normal form game.
    """
    g = pygambit.Game.new_table([2, 2])
    g.title = "Matching Pennies"
    g.players[0].label = "Matcher"
    g.players[1].label = "Mismatcher"
    g.players[0].strategies[0].label = "Heads"
    g.players[0].strategies[1].label = "Tails"
    g.players[1].strategies[0].label = "Heads"
    g.players[1].strategies[1].label = "Tails"

    # Both Heads
    g[0, 0][0] = 1
    g[0, 0][1] = -1
    # Heads, Tails
    g[0, 1][0] = -1
    g[0, 1][1] = 1
    # Tails, Heads
    g[1, 0][0] = -1
    g[1, 0][1] = 1
    # Both Tails
    g[1, 1][0] = 1
    g[1, 1][1] = -1

    return g


def coordination_game(reward=2, mismatch=0):
    """
    Create a Coordination game.

    Parameters
    ----------
    reward : int, default 2
        Payoff when both players choose same strategy.
    mismatch : int, default 0
        Payoff when players choose different strategies.

    Returns
    -------
    pygambit.Game
        A 2x2 normal form game.
    """
    g = pygambit.Game.new_table([2, 2])
    g.title = "Coordination Game"
    g.players[0].label = "Player 1"
    g.players[1].label = "Player 2"
    g.players[0].strategies[0].label = "A"
    g.players[0].strategies[1].label = "B"
    g.players[1].strategies[0].label = "A"
    g.players[1].strategies[1].label = "B"

    g[0, 0][0] = reward
    g[0, 0][1] = reward
    g[0, 1][0] = mismatch
    g[0, 1][1] = mismatch
    g[1, 0][0] = mismatch
    g[1, 0][1] = mismatch
    g[1, 1][0] = reward
    g[1, 1][1] = reward

    return g


def rock_paper_scissors():
    """
    Create a Rock-Paper-Scissors game.

    Returns
    -------
    pygambit.Game
        A 3x3 zero-sum normal form game.
    """
    g = pygambit.Game.new_table([3, 3])
    g.title = "Rock Paper Scissors"
    g.players[0].label = "Player 1"
    g.players[1].label = "Player 2"

    strategies = ["Rock", "Paper", "Scissors"]
    for i, s in enumerate(strategies):
        g.players[0].strategies[i].label = s
        g.players[1].strategies[i].label = s

    # Payoff matrix: 1 = win, -1 = loss, 0 = draw
    payoffs = [
        [(0, 0),  (-1, 1), (1, -1)],   # Rock
        [(1, -1), (0, 0),  (-1, 1)],   # Paper
        [(-1, 1), (1, -1), (0, 0)]     # Scissors
    ]

    for i in range(3):
        for j in range(3):
            g[i, j][0] = payoffs[i][j][0]
            g[i, j][1] = payoffs[i][j][1]

    return g