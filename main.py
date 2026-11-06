import random
from Agent import Agent
'''
details:
2 agents engage in a 50/50 gamble where they gamble x% of the poorer ones money and the winner receives the amount from the loser
once an agents wealth reaches 0 they are removed from the game
1 run of the game consists of random interactions so 50 pairs of trades are made by 50 agents playing against another agent randomly
'''


class Game:
    
    def __init__(self, agents: list[Agent]) -> None:
        self.agents = agents

    def make_partners(self) -> list[tuple[Agent, Agent]]:
        agents_copy = self.agents[:]
        result = []
        
        for i in range(len(self.agents)//2):
            i2 = random.randrange(0, len(agents_copy))
            agents_copy.pop(i2)
            result.append((self.agents[i], self.agents[i2]))

        return result
    
    def play(self, runs):
        
        for _ in range(runs):
            partnered_agents = set()

            for i in range(len(self.agents)//2): # odd number of agents means one agent won't get to play
                