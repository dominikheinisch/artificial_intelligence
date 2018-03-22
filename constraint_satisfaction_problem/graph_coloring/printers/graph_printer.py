import matplotlib.pyplot as plt
import networkx as nx

import constraint_satisfaction_problem.graph_coloring.any_graph_solver as mg

# number of possible colors without color white
COLOR_DICT = {1: 'r', 2: 'b', 3: 'g', 4: 'y', 5: 'm', 6: 'c', 7: 'k'}
NO_COLORS = len(COLOR_DICT)

# number of possible node shapes
NODE_SHAPE_DICT = {0: 'o', 1: '*', 2: 's', 3: 'v', 4: '.'}
NO_NODE_SHAPES = len(NODE_SHAPE_DICT)


# number of possible different nodes: 7 * 5 == 35
def print_(matrix_edged, nodes_values):
    size = len(nodes_values)

    # init graph
    G = nx.erdos_renyi_graph(size, 0.05)

    # posiotion
    pos = nx.spring_layout(G)

    # nodes
    map_index_shape_color = {}
    for i in range(size):
        shape = 0
        for j in range(NO_NODE_SHAPES):
            if nodes_values[i] > NO_COLORS:
                shape += 1
                nodes_values[i] -= NO_COLORS
        map_index_shape_color.update({i: (COLOR_DICT[nodes_values[i]], NODE_SHAPE_DICT[shape])})
    print(map_index_shape_color)

    shape_list = list(NODE_SHAPE_DICT.values())
    print(shape_list)
    for shape in shape_list:
        node_list = []
        color_list = []
        for i in range(size):
            if map_index_shape_color[i][1] == shape:
                node_list.append(i)
                color_list.append(map_index_shape_color[i][0])
        nx.draw_networkx_nodes(G, pos=pos, nodelist=node_list,
                               node_color=color_list, node_shape=shape,
                               node_size=700)

    # edges
    edges = []
    for i in range(len(matrix_edged)):
        for j in range(i, len(matrix_edged[i])):
            if matrix_edged[i][j] == 1:
                edges.append((i, j))
    nx.draw_networkx_edges(G, pos=pos, edgelist=edges)

    # labels
    labels = {}
    for node in G.nodes():
        labels[node] = node
    nx.draw_networkx_labels(G, pos, labels, font_size=12, font_color='w')

    # plot
    plt.axis('off')
    plt.savefig("100.png")  # save as png
    plt.show()

if __name__ == "__main__":
    a = mg.main()
    print(a)
    print_(a[0], a[1])