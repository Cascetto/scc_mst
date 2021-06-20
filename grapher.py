import math
import random
from min_heap import *
from printer import print_prim, _print_graph


class Node:

    def __init__(self, index: int):
        self.index = index
        self.key = math.inf
        self.previus = None


def create_graph(size: int, max_weight: float, min_weight: int = 0):
    graph = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            w = random.randint(0, int(max_weight))
            if i != j and w >= min_weight:
                graph[i][j] = w
    return graph


def create_unoriented_graph(size: int, max_weight: float):
    graph = [[0 for j in range(size)] for i in range(size)]
    for i in range(size):
        for j in range(i, size):
            if i != j:
                graph[i][j] = graph[j][i] = random.randint(0, int(max_weight))
    return graph


def inverse_graph(graph: list) -> list:
    gt = [[] * len(graph) for _ in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph)):
            gt[i].append(graph[j][i])
    return gt


def prim(graph: list):
    queue = []
    for i in range(len(graph)):
        queue.append(Node(i))
    decrease_key(queue, random.randint(0, len(queue) - 1), 0)
    result = []
    iteration = 1
    while len(queue) > 0:
        u = extract_min(queue)
        for v_index in range(len(graph[u.index])):
            v = find_element_by_index(queue, v_index)
            if v is not None and queue[v].key > graph[u.index][v_index] > 0:
                queue[v].previus = u
                decrease_key(queue, v, graph[u.index][v_index])
        result.append(u)
        print_prim(result, len(graph), iteration)
        iteration += 1
    return result


def DFS_visit(graph: list, node: int, color: list, previus: list, time: list, start: list, final: list):
    time[0] += 1
    start[node] = time[0]
    color[node] = 'grey'
    for i in range(len(graph[node])):
        if graph[node][i] > 0 and color[i] == 'white':
            previus[i] = node
            DFS_visit(graph, i, color, previus, time, start, final)
    color[node] = 'black'
    time[0] += 1
    final[node] = time[0]


def DFS(graph: list):
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
    return start, final, previus


def SCC(graph: list, order: list, tries: int, suppress_output: bool = False):
    color = ['white'] * len(graph)
    previus = [None] * len(graph)
    added = [False] * len(graph)
    scc_nodes = []
    start = final = [0] * len(graph)
    time = [0]
    for node in order:
        if color[node] == 'white':
            DFS_visit(graph, node, color, previus, time, start, final)

        scc = []
        for i in range(len(color)):
            if color[i] == 'black' and not added[i]:
                added[i] = True
                scc.append(i)
        if len(scc) > 0:
            scc_nodes.append(scc)
    used = []
    edge = []
    for scc in scc_nodes:
        for node in scc:
            for i in range(len(graph[node])):
                if graph[node][i] > 0:
                    for s in scc_nodes:
                        if i in s and s != scc and not [scc, s] in used:
                            s1 = []
                            for n in scc:
                                s1.append(n)
                            s2 = []
                            for n in s:
                                s2.append(n)
                            # s1 = ""
                            # for n in scc:
                            #     s1 += f"{str(n)}, "
                            # s1 = s1[0: len(s1) - 2]
                            # s2 = ""
                            # for n in s:
                            #     s2 += f"{str(n)}, "
                            # s2 = s2[0: len(s2) - 2]
                            edge.append((s1, s2))
                            used.append([scc, s])
    _print_graph(scc_nodes, edge, f"scc{tries}_{len(graph)}x{len(graph)}_result", False, suppress_output=suppress_output)
    return start, final, previus, len(scc_nodes)
