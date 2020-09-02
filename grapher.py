import random
from math import inf
from graphviz import Digraph

from typing import List

from min_heap import *


class Node:

    def __init__(self, i, k):
        self.key = k
        self.index = i
        self.previus = None

    def print(self):
        print(self.index, self.key, self.previus.index if self.previus is not None else "First")


# def create_graph(number_of_nodes: int, max_weight: int = 1) -> list:
#     graph = [0] * (number_of_nodes * number_of_nodes)
#     for i in range(number_of_nodes):
#         for j in range(number_of_nodes):
#             if i != j:
#                 graph[i * number_of_nodes + j] = random.randint(0, max_weight)
#     return graph
#
#
# def mst_prim(graph: list):
#     n = int(sqrt(len(graph)))
#     key = [inf] * n
#     previus = [None] * n
#     r = random.randint(0, n - 1)
#     create_heap(key)
#     decrease_key(key, r, 0)
#     while len(key) > 0:
#         u = extract_min(graph)
#         for v in graph[]


def find_node(nodes: List[Node], index: int):
    for i in range(len(nodes)):
        if index == nodes[i].index:
            return i
    return -1


def create_graph(number_of_nodes: int, max_weight: int = 1) -> list:
    adj = []
    dot = Digraph('Graph')
    for u in range(number_of_nodes):
        dot.node(str(u))
        adj.append([])
        for v in range(number_of_nodes):
            (adj[u]).append(random.randint(0, max_weight) if u != v else 0)
    for i in range(len(adj)):
        for j in range(len(adj[i])):
            if adj[i][j] > 0:
                dot.edge(str(i), str(j), str(adj[i][j]))
    dot.view()
    return adj


def mst_prim(graph: list) -> list:
    dot = Digraph('MST')
    result = list()
    n = len(graph)
    for i in range(n):
        dot.node(str(i))
    nodes = [Node(i, inf) for i in range(n)]
    r = random.randint(0, n - 1)
    create_heap(nodes)
    nodes[r].key = 0
    while len(nodes) > 0:
        u = extract_min(nodes)
        # for w in range(len(graph[u.index])):
        #     v = find_node(nodes, w)
        #     if u.key > graph[u.index][w] > 0 and v >= 0:
        #         nodes[v].previus = u
        #         decrease_key(nodes, v, graph[u.index][w])

        for v in nodes:
            w = graph[u.index][v.index]
            if v.key > w > 0:
                v.previus = u
                decrease_key(nodes, v, w)
        result.append(u)
    for node in result:
        if node.previus is not None:
            dot.edge(str(node.previus.index), str(node.index), str(node.key))
    dot.view()
    return result
