def parent(i: int):
    return int(i / 2)


def left_child(i: int):
    return i * 2


def right_child(i: int):
    return (i * 2) + 1


def min_heapify(heap: list, index: int):
    size = len(heap)
    minimum = index + 1
    left = left_child(minimum)
    right = left + 1
    if left <= size and heap[left - 1].key < heap[minimum - 1].key:
        minimum = left
    if right <= size and heap[right - 1].key < heap[minimum - 1].key:
        minimum = right
    if minimum != index + 1:
        heap[index], heap[minimum - 1] = heap[minimum - 1], heap[index]
        min_heapify(heap, minimum - 1)


# def min_heapify(heap: list, i: int):
#     size = len(heap)
#     min_ind = i + 1
#     l = 2 * min_ind
#     r = l + 1
#     if l <= size and heap[l - 1].key < heap[min_ind - 1].key:
#         min_ind = l
#     if r <= size and heap[r - 1].key < heap[min_ind - 1].key:
#         min_ind = r
#     if min_ind != i + 1:
#         heap[i], heap[min_ind - 1] = heap[min_ind - 1], heap[i]
#         min_heapify(heap, min_ind - 1)


def create_heap(heap: list):
    for i in reversed(range(int(len(heap) / 2))):
        min_heapify(heap, i)


def extract_min(heap: list):
    if len(heap) == 1:
        ext = heap[0]
        heap.pop()
        return ext
    elif len(heap) > 1:
        ext = heap[0]
        heap[0] = heap[-1]
        heap.pop()
        min_heapify(heap, 0)
        return ext


def find_element(heap: list, element):
    for i in range(len(heap)):
        if heap[i] == element:
            return i
    return None


def find_element_by_index(heap: list, index: int):
    for i in range(len(heap)):
        if heap[i].index == index:
            return i
    return None


def decrease_key(heap: list, index: int, key: float):
    if key < heap[index].key:
        heap[index].key = key
        index += 1
        p = parent(index)
        while index > 1 and heap[p - 1].key > heap[index - 1].key:
            heap[p - 1], heap[index - 1] = heap[index - 1], heap[p - 1]
            index = parent(index)
            p = parent(index)


from random import randint


class obj:
    def __init__(self):
        self.key = randint(10, 100)

    def print(self):
        print(self.key, sep=', ')