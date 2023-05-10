"""Code retrieved from Axelrod rand.py strategy"""

from axelrod.action import Action
from axelrod.player import Player
import random

C, D = Action.C, Action.D


class Lukas(Player):
    """A player who randomly chooses between cooperating and defecting.
    This strategy came 15th in Axelrod's original tournament.
    Names:
    - Random: [Axelrod1980]_
    - Lunatic: [Tzafestas2000]_
    """

    name = "Lukas - Generous Tit-For-Tat"
    classifier = {
        "memory_depth": 0,   # Memory-one Four-Vector = (p, p, p, p)
        "stochastic": True,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def __init__(self) -> None:
        """
        Parameters
        ----------
        p, float
            The probability to cooperate
        Special Cases
        -------------
        Random(0) is equivalent to Defector
        Random(1) is equivalent to Cooperator
        """
        super().__init__()
        self.num_rounds_defect = 2
        self.defecting_rounds = 0
        self.round_number = 0


    def strategy(self, opponent: Player) -> Action:
        """Actual strategy definition that determines player's action."""
        self.round_number += 1

        if(self.round_number == 10):
            return self.defect(opponent=opponent)
        
        if len(opponent.history) == 0:
            return self.cooperate(opponent=opponent)
        
        if opponent.history[-1] == D:
            self.defecting_rounds = self.num_rounds_defect
            return self.defect(opponent=opponent)
        
        if self.defecting_rounds > 0:
            self.defecting_rounds -= 1
            random_number = random.randint(0, 1)
            if random_number == 1:
                return self.cooperate(opponent=opponent)
            else:
                return self.defect(opponent=opponent)

        return self.cooperate(opponent=opponent)
        

    @classmethod
    def cooperate(cls, opponent: Player) -> Action:
        return C

    @classmethod
    def defect(cls, opponent: Player) -> Action:
        return D