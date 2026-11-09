

class Agent:
    def __init__(self, name: str, balance: float, skill: float) -> None:
        self.name = name
        self.balance = balance
        self.skill = skill # describes the chance of winning in a trade against someone with a lower skill