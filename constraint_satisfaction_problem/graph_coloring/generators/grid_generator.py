import numpy as np


def generate_grid_graph(side):
    nodes_size = side * side
    adjacency_matrix = np.zeros(shape=(nodes_size, nodes_size))
    grid = np.arange(nodes_size).reshape(side, side)
    for i in range(nodes_size):
        for j in range(nodes_size):
            pass
    for i in range(side):
        for j in range(side):
            if i > 0:
                adjacency_matrix[grid[i, j], grid[i - 1, j]] = 1
            if i + 1 < side:
                adjacency_matrix[grid[i, j], grid[i + 1, j]] = 1
            if j > 0:
                adjacency_matrix[grid[i, j], grid[i, j - 1]] = 1
            if j + 1 < side:
                adjacency_matrix[grid[i, j], grid[i, j + 1]] = 1
    return adjacency_matrix
