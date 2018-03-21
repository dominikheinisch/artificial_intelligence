from constraint_satisfaction_problem.graph_coloring.simulations import SimulationGraphColoring
from constraint_satisfaction_problem.graph_coloring.simulations import SimulationLatinSquare


if __name__ == "__main__":
    for i in range(1, 10):
        s = SimulationGraphColoring(i)
        print(s.run())
    for i in range(1, 10):
        s = SimulationLatinSquare(i)
        print(s.run())