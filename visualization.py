#https://stackoverflow.com/questions/29572623/plot-networkx-graph-from-adjacency-matrix-in-csv-file

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def show_graph_with_labels(adjacency_matrix, mylabels):
    rows, cols = np.where(np.array(adjacency_matrix) == 1)
    edges = zip(rows.tolist(), cols.tolist())
    gr = nx.Graph()
    gr.add_edges_from(edges)
    nx.draw(gr, node_size=500, labels=mylabels, with_labels=True)
    plt.show()

def show_graph(adjacency_matrix):
    rows, cols = np.where(np.array(adjacency_matrix) == 1)
    edges = zip(rows.tolist(), cols.tolist())
    gr = nx.Graph()
    gr.add_edges_from(edges)
    nx.draw(gr, node_size=500)
    plt.show()