from Game import Game
from Agent import Agent
import matplotlib.pyplot as plt


agents = [Agent(str(i), 100) for i in range(1000)]
game = Game(agents, 0.1)
game.play(100)


def generate_sorted_graph_points() -> tuple[list, list]:
    y_vals = [round(a.balance, 2) for a in sorted(game.agents, key=lambda agent: agent.balance)]
    x_vals = [i for i in range(1, len(agents)+1)]
    return (x_vals, y_vals)

points = generate_sorted_graph_points()
plt.plot(points[0], points[1])
plt.show() 