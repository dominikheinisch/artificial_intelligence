from csp.simulations import MultipleSimulation, SimulationType, SolutionType


if __name__ == "__main__":
    sim = MultipleSimulation(SimulationType.LATIN_SQUARE, SolutionType.FORWARD_CHECKING, 2, 5, False, True)
    # sim = MultipleSimulation(SimulationType.GRAPH_COLORING, SolutionType.BACKTRACKING, 1, 17, False, False)
    # sim = MultipleSimulation(SimulationType.LATIN_SQUARE, SolutionType.BACKTRACKING, 1, 17, False, False)
    sim.run()
