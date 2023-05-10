"""Code retrieved from Axelrod rand.py strategy"""

from axelrod.action import Action
from axelrod.player import Player

C, D = Action.C, Action.D


class Philipp(Player):
    """A player who randomly chooses between cooperating and defecting.
    This strategy came 15th in Axelrod's original tournament.
    Names:
    - Random: [Axelrod1980]_
    - Lunatic: [Tzafestas2000]_
    """

    name = "Philipp - Random"
    classifier = {
        "memory_depth": 0,  # Memory-one Four-Vector = (p, p, p, p)
        "stochastic": True,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def __init__(self, p: float = 0.5) -> None:
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
        self.p = p

    def strategy(self, opponent: Player) -> Action:
        """Actual strategy definition that determines player's action."""
        print(opponent)
        print(len(opponent.history))
        print("-----------------")
        print("################# Opponedt History: ", opponent.history)
        if len(opponent.history) == 0:
            print("################# Played: ", "C")
            return C
        if len(opponent.history) > 2 and opponent.history[-1] == C:
            print("################# Played: ", "D")
            return D
        if opponent.history[-1] == C:
            print("################# Played: ", "C")
            return C
        if opponent.history[-1] == D:
            print("################# Played: ", "D")
            return D
        return opponent.history[-1]

    def _post_init(self):
        super()._post_init()
        if self.p in [0, 1]:
            self.classifier["stochastic"] = False
        # Avoid calls to _random, if strategy is deterministic
        # by overwriting the strategy function.
        if self.p <= 0:
            self.strategy = self.tit_for_tat
        if self.p >= 1:
            self.strategy = self.cooperate

    @classmethod
    def tit_for_tat(cls, opponent: Player) -> Action:
        if len(opponent.history) == 0:
            return C
        return opponent.history[-1]

    @classmethod
    def cooperate(cls, opponent: Player) -> Action:
        return C

    @classmethod
    def cooperate(cls, opponent: Player) -> Action:
        return C

    @classmethod
    def defect(cls, opponent: Player) -> Action:
        return D
