import random
import numpy as np
from Agent import Agent
from collections.abc import Iterable
'''
details:
2 agents engage in a 50/50 gamble where they gamble x% of the poorer ones money and the winner receives the amount from the loser
1 run of the game consists of random interactions so 50 pairs of trades are made by 50 agents playing against another agent randomly
when skill isn't equal each of them will have a skill/total_skill chance of winning
'''


class Game:
    
    def __init__(self, agents: list[Agent], trade_percentage: float) -> None:
        self.agents = agents
        if not (0 < trade_percentage <= 1):
            raise ValueError("trade percentage wasn't between 0 and 1")
        self.trade_percent = trade_percentage


    def make_partners(self) -> Iterable[tuple[Agent, Agent]]:
        agents_copy = self.agents[:]
        random.shuffle(agents_copy)
        for i in range(0, len(agents_copy)-1, 2):
            yield (agents_copy[i], agents_copy[i+1])


    def trade(self, agent1: Agent, agent2: Agent) -> None:
        '''
        take the 2 skill chances of winning and then determine the winner
        with each agent having a probability of winning to be agent_skill/agent_skill_sum
        and then subtract the trade_percent of the poorer agents money from the loser and
        add it to the winners balance
        '''
        winner = random.choices([agent1, agent2], [agent1.skill, agent2.skill])[0] # if weights don't sum to 1 then it takes agent_skill/(agent1.skill+agent2.skill) as agent skill
        amount = self.trade_percent * min(agent1.balance, agent2.balance)
        if winner == 1:
            agent1.balance += amount
            agent2.balance -= amount
        else:
            agent2.balance += amount
            agent1.balance -= amount


    def play(self, runs):
        
        for _ in range(runs):

            for agent1, agent2 in self.make_partners(): # odd number of agents means one agent won't get to play
                self.trade(agent1, agent2)