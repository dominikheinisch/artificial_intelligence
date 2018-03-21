import matplotlib.pyplot as plt
import networkx as nx

G = nx.erdos_renyi_graph(4, 0)
pos = nx.spring_layout(G)

# nodes
nodelist = [2, 0]
colorlist = ['g', 'b']
nx.draw_networkx_nodes(G, pos=pos, node_size=700, nodelist=nodelist, node_color=colorlist, node_shape='*')
nodelist = [3, 1]
colorlist = ['y', 'r']
nx.draw_networkx_nodes(G, pos=pos, node_size=700, nodelist=nodelist, node_color=colorlist, node_shape='s')

# edges
matrix_edged = [[0, 1, 1, 0],
                [1, 0, 1, 1],
                [1, 1, 0, 1],
                [0, 1, 1, 0]]
edges = []
for i in range(len(matrix_edged)):
    for j in range(i, len(matrix_edged[i])):
        if matrix_edged[i][j] == 1:
            edges.append((i, j))
nx.draw_networkx_edges(G, pos=pos, edgelist=edges)

labels = {2: 2, 3: 3, 0: 'zero', 1: 1}
nx.draw_networkx_labels(G, pos, labels, font_size=10, font_color='w')
plt.axis('off')
plt.show()
