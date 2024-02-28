from collections import namedtuple
from pyvis.network import Network

Graph = namedtuple("Graph", ["nodes", "edges", "is_directed"])

def show(graph, output_filename):
    """
    Saves an HTML file locally, returns a pyvis Network instance of the graph
    """
    g = Network(directed=graph.is_directed)
    g.add_nodes(graph.nodes)
    g.add_edges(graph.edges)
    g.show(output_filename)
    return g

nodes = range(4)
edges = [
    (0,1),
    (1,2),
    (2,3),
    (3,0),
    (0,2),
]

G = Graph(nodes, edges, is_directed=False)

show(G, "basic.html")
