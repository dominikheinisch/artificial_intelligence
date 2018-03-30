import numpy as np


def generate_adjacency_matrix_graph_coloring(side):
    nodes_size = side * side
    adjacency_matrix = np.zeros(shape=(nodes_size, nodes_size), dtype=np.int8)
    grid = np.arange(nodes_size).reshape(side, side)
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


def generate_double_adjacency_matrix_graph_coloring(adjacency_matrix):
    size = adjacency_matrix.shape[0]
    double_adjacent_matrix = np.zeros(shape=(size, size), dtype=np.int8)
    for row in range(size):
        for col in range(size):
            if adjacency_matrix[row][col]:
                double_adjacent_matrix[row] = np.logical_or(double_adjacent_matrix[row], adjacency_matrix[col])
    np.fill_diagonal(double_adjacent_matrix, 0)
    return double_adjacent_matrix


def generate_adjacency_matrix_latin_square(side):
    nodes_size = side * side
    adjacency_matrix = np.zeros(shape=(nodes_size, nodes_size), dtype=np.int8)
    for i in range(nodes_size):
        for j in range(nodes_size):
            if i // side == j // side:
                adjacency_matrix[i, j] = 1
            if i % side == j % side:
                adjacency_matrix[i, j] = 1
    np.fill_diagonal(adjacency_matrix, 0)
    return adjacency_matrix
