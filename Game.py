import random
from Agent import Agent
from collections.abc import Iterable
'''
details:
2 agents engage in a 50/50 gamble where they gamble x% of the poorer ones money and the winner receives the amount from the loser
1 run of the game consists of random interactions so 50 pairs of trades are made by 50 agents playing against another agent randomly
'''


class Game:
    
    def __init__(self, agents: list[Agent], trade_percentage: float) -> None:
        self.agents = agents
        self.trade_percent = trade_percentage

    def make_partners(self) -> Iterable[tuple[Agent, Agent]]:
        agents_copy = self.agents[:]
        
        for i in range(len(self.agents)//2):
            i2 = random.randrange(0, len(agents_copy))
            agents_copy.pop(i2)
            yield (self.agents[i], self.agents[i2])

    def trade(self, agent1: Agent, agent2: Agent):
        winner = random.randint(1, 2)
        amount = self.trade_percent * min(agent1.balance, agent2.balance)
        if winner == 1:
            agent1.balance += amount
            agent2.balance -= amount
        else:
            agent2.balance += amount
            agent1.balance -= amount

    def play(self, runs):
        
        for _ in range(runs):
            
            for partners in self.make_partners(): # odd number of agents means one agent won't get to play
                self.trade(partners[0], partners[1])