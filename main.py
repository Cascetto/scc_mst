from grapher import *
from graphviz import Digraph

if __name__ == '__main__':
    s = 5
    # g = create_unoriented_graph(s, 5)
    #
    # result = prim(g)
    # dot = Digraph("2")
    # for node in result:
    #     if node.previus is not None:
    #         dot.edge(str(node.previus.index), str(node.index), str(node.key))
    # dot.view()

    g = create_graph(s, 100)
    d = Digraph("1")
    for i in range(s):
        d.node(str(i))
    for i in range(s):
        for j in range(s):
            if g[i][j] > 60:
                d.edge(str(i), str(j), str(g[i][j]))
    d.view()

    d, f, pi = DFS(g)

    gt = inverse_graph(g)

    order = []
    l = len(f)
    for i in range(l):
        m = 0
        v = -1
        for j in range(l):
            if f[j] > v:
                v = f[j]
                m = j
        order.append(m)
        f[m] = -1
    SCC(gt, order, True)
