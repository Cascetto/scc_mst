from grapher import *
from min_heap import *
from utils import print_adj

if __name__ == '__main__':
    g = create_graph(4, 3)
    result = mst_prim(g)
    for r in result:
        r.print()