from grapher import *
from min_heap import *
from utils import print_adj

if __name__ == '__main__':
    g = create_graph(5, 3)
    r = mst_prim(g)
    print(r)
    for line in r:
        print(line.print())
    print_adj(g)
