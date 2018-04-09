from csp.simulations import MultipleSimulation, SimulationType, SolutionType


if __name__ == "__main__":
    sim = MultipleSimulation(SimulationType.GRAPH_COLORING, SolutionType.BACKTRACKING, 3, 9, True, False)
    # sim = MultipleSimulation(SimulationType.GRAPH_COLORING, SolutionType.BACKTRACKING, 1, 17, False, False)
    # sim = MultipleSimulation(SimulationType.LATIN_SQUARE, SolutionType.BACKTRACKING, 1, 17, False, False)
    sim.run()
