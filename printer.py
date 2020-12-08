from graphviz import Digraph
import matplotlib.pyplot as plt


def print_prim(nodes: list, graph_size: int, iteration: int):
    graph = [[0 for _ in range(graph_size)] for _ in range(graph_size)]
    for node in nodes:
        if node.previus is not None:
            graph[node.previus.index][node.index] = node.key
    print_graph(graph, f"prim_iteration_{iteration}", suppress_output=True)


def print_graph(graph: list, name: str, suppress_output: bool = False):
    l = len(graph)
    nodes = [i for i in range(l)]
    edges = []
    for i in range(l):
        for j in range(l):
            if graph[i][j] > 0:
                edges.append((i, j, graph[i][j]))
    _print_graph(nodes, edges, name, suppress_output=suppress_output)


def _print_graph(nodes: list, edges: list, name: str, weighted: bool = True, suppress_output: bool = False):
    graph = Digraph(name=name, filename=f"output/graph_{name}", format="PDF")
    for node in nodes:
        graph.node(str(node), str(node))
    if weighted:
        for edge in edges:
            graph.edge(str(edge[0]), str(edge[1]), str(edge[2]))
    else:
        for edge in edges:
            graph.edge(str(edge[0]), str(edge[1]))
    if not suppress_output:
        graph.view()
    graph.render(format="svg")


def plot_data(xaxis: list, yaxis: list, xlabel: str = "", ylabel: str = ""):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(xaxis, yaxis)
    plt.show()