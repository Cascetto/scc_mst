import math
import random
from min_heap import *
from graphviz import Digraph


class Node:

    def __init__(self, index: int):
        self.index = index
        self.key = math.inf
        self.previus = None


def create_graph(size: int, max_weight: float):
    graph = [[0 for j in range(size)] for i in range(size)]
    for i in range(size):
        for j in range(size):
            if i != j:
                graph[i][j] = random.randint(0, int(max_weight))
    return graph


def create_unoriented_graph(size: int, max_weight: float):
    graph = [[0 for j in range(size)] for i in range(size)]
    for i in range(size):
        for j in range(i, size):
            if i != j:
                graph[i][j] = graph[j][i] = random.randint(0, int(max_weight))
    return graph


def inverse_graph(graph: list) -> list:
    gt = graph
    for i in range(len(graph)):
        for j in range(len(graph)):
            gt[j][i] = graph[i][j]
    return gt


def prim(graph: list):
    queue = []
    for i in range(len(graph)):
        queue.append(Node(i))
    decrease_key(queue, random.randint(0, len(queue) - 1), 0)
    result = []
    while len(queue) > 0:
        u = extract_min(queue)
        for v_index in range(len(graph[u.index])):
            v = find_element_by_index(queue, v_index)
            if v is not None and queue[v].key > graph[u.index][v_index] > 0:
                queue[v].previus = u
                decrease_key(queue, v, graph[u.index][v_index])
        result.append(u)
    return result


def DFS_visit(graph: list, node: int, color: list, previus: list, time: list, start: list, final: list):
    time[0] += 1
    start[node] = time[0]
    color[node] = 'grey'
    for i in range(len(graph[node])):
        if graph[node][i] > 60 and color[i] == 'white':
            previus[i] = node
            DFS_visit(graph, i, color, previus, time, start, final)
    color[node] = 'black'
    time[0] += 1
    final[node] = time[0]


def DFS(graph: list, print_graph: bool = False):
    color = ['white'] * len(graph)
    previus = [None] * len(graph)
    start = final = [0] * len(graph)
    time = [0]
    added = [False] * len(graph)
    check_order = [i for i in range(len(graph))]
    random.shuffle(check_order)
    for node in check_order:
        if color[node] == 'white':
            DFS_visit(graph, node, color, previus, time, start, final)

        if print_graph:
            dot = Digraph(f"Noda esplorato {node}")
            for i in range(len(color)):
                if color[i] == 'black' and not added[i]:
                    dot.node(str())
            for i in range(len(previus)):
                if previus[i] is not None:
                    dot.edge(str(previus[i]), str(i))
            dot.view()
    return start, final, previus


def SCC(graph: list, order: list, print_graph: bool = False):
    color = ['white'] * len(graph)
    previus = [None] * len(graph)
    start = final = [0] * len(graph)
    time = [0]
    for node in order:
        if color[node] == 'white':
            DFS_visit(graph, node, color, previus, time, start, final)

        if print_graph:
            dot = Digraph(f"Noda esplorato {node}")
            for node in range(len(color)):
                if color[node] != 'white':
                    dot.node(str(node))
            for i in range(len(previus)):
                if previus[i] is not None:
                    dot.edge(str(previus[i]), str(i))
            dot.view()
    return start, final, previus