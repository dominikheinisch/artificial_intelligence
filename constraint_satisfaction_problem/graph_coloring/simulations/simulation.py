from constraint_satisfaction_problem.graph_coloring import generate_grid_graph
from constraint_satisfaction_problem.graph_coloring import GraphColoring
from constraint_satisfaction_problem.graph_coloring import print_grid_graph


class Simulation(object):
    SIDE = 3

    def __init__(self, side=SIDE):
        self.side = side

    def run(self):
        adjacency_matrix = generate_grid_graph(self.side)
        gc = GraphColoring(side=self.side, adjacency_matrix=adjacency_matrix)
        gc.solve_backtracking()
        print(gc.nodes_colors)
        print_grid_graph(gc.adjacency_matrix.tolist(), (gc.nodes_colors / 2 + 1).tolist())
        return gc.min_colors_size, gc.nodes_colors, gc.simulation_time
