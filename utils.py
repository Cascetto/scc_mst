def print_matrix(matrix: list, m: int, n: int):
    for i in range(m):
        print(matrix[i * n: i * n + n])


def print_adj(adj: list):
    for node in adj:
        print(node)
