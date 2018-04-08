from csp.simulations import MultipleSimulation, SimulationType, SolutionType


if __name__ == "__main__":
    sim = MultipleSimulation(SimulationType.GRAPH_COLORING, SolutionType.BACKTRACKING, 3, 5, True, False)
    sim.run()
