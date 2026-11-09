from Game import Game
from Agent import Agent
import matplotlib.pyplot as plt


trade_wager = 0.1
agent_number = 1000
starting_balance = 23
number_of_runs = 10000

agents = [Agent(str(i), starting_balance, 0.5) for i in range(agent_number)]
game = Game(agents, trade_wager)
game.play(number_of_runs)


def generate_sorted_graph_points() -> tuple[list, list]:
    y_vals = [round(a.balance, 2) for a in sorted(game.agents, key=lambda agent: agent.balance)]
    x_vals = [i for i in range(1, len(agents)+1)]
    return (x_vals, y_vals)



points = generate_sorted_graph_points()
plt.xlabel("Agent rank (poorest to richest)")
plt.ylabel("Balance")
plt.title("Distribution of Wealth")

plt.plot(points[0], points[1])
plt.show()