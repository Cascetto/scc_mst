from grapher import *
from printer import *

from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

import numpy as np


def part_1():
    g = create_unoriented_graph(5, 10)
    print_graph(g, "prim", suppress_output=False)
    prim(g)


def part_2():
    smin = 3
    smax = 20
    threesold = 70
    tries = 1
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
    return xaxis, yaxis


def scc_test(number_of_nodes: int, threshold: int, number_of_tries: int):
    result = 0
    for t in range(number_of_tries):
        g = create_graph(number_of_nodes, 100, threshold)
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
        result += SCC(gt, order, t + 1, suppress_output=True)[3]
    return float(result) / number_of_tries


def scc_test_bootstrap():
    nodes_min = 4
    nodes_step = 2
    thresold_min = 10
    threeold_max = 90 # == 10 + 1 * 80
    thresold_step = 1

    tries = 15
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    x = [nodes_min + i * nodes_step for i in range(80)]
    y = [thresold_min + i * thresold_step for i in range(80)]
    z = [[scc_test(nodes, threshold, tries) for nodes in x] for threshold in y]
    X = np.array(x)
    xlen = len(x)
    Y = np.array(y)
    ylen = len(y)
    X, Y = np.meshgrid(X, Y)
    Z = np.array(z)

    colortuple = ('y', 'b')
    colors = np.empty(X.shape, dtype=str)
    for y in range(ylen):
        for x in range(xlen):
            colors[x, y] = colortuple[(x + y) % len(colortuple)]

    surf = ax.plot_surface(X, Y, Z, facecolors=colors, linewidth=0)
    ax.set_xlabel("Numero di nodi")
    ax.set_ylabel("Probabilità di assegnazione di un arco")
    ax.set_zlabel("Numero di SCCs")
    plt.show()




if __name__ == '__main__':
    # part_1()
    part_2()
    # scc_test_bootstrap()
