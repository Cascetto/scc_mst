from grapher import *
from printer import *


def part_1():
    g = create_unoriented_graph(5, 10)
    print_graph(g, "prim", suppress_output=False)
    prim(g)


def part_2():
    smin = 3
    smax = 10
    threesold = 70
    tries = 10
    xaxis = []
    yaxis = []

    for s in range(smin, smax):
        y_entry = 0
        for t in range(tries):
            g = create_graph(s, 100, threesold)
            print_graph(g, f"scc{tries}_{s}x{s}_oriented_graph", suppress_output=True)
            d, f, pi = DFS(g)
            gt = inverse_graph(g)
            print_graph(gt, f"scc{tries}_{s}x{s}_inverted_graph", suppress_output=True)
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
            y_entry += SCC(gt, order, t + 1, suppress_output=True)[3]
        xaxis.append(s)
        yaxis.append(y_entry / tries)
    plot_data(xaxis, yaxis, "number of nodes", "number of sccs")


if __name__ == '__main__':
    part_1()
    part_2()
