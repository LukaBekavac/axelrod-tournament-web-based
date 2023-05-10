from axelrod.action import Action
from axelrod.player import Player

C, D = Action.C, Action.D

class Luka(Player):
    name = "Luka - Checkmate"
    classifier = {
        "memory_depth": 1,
        "stochastic": False,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def strategy(self, opponent: Player) -> Action:
        """Actual strategy definition that determines player's action."""
        # If it's the first round, cooperate
        if len(self.history) == 0:
            return C
        # If it's the last round, defect
        elif len(self.history) == 9:
            return D
        # Otherwise, mimic the opponent's previous action
        else:
            return opponent.history[-1]
