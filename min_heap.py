def min_heapify(heap: list, i: int):
    size = len(heap)
    min_ind = i + 1
    l = 2 * min_ind
    r = l + 1
    if l <= size and heap[l - 1].key < heap[min_ind - 1].key:
        min_ind = l
    if r <= size and heap[r - 1].key < heap[min_ind - 1].key:
        min_ind = r
    if min_ind != i + 1:
        heap[i], heap[min_ind - 1] = heap[min_ind - 1], heap[i]
        min_heapify(heap, min_ind - 1)


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


def decrease_key(heap: list, x: int, key):
    if key < heap[x].key:
        heap[x].key = key
        while x > 0 and heap[int(x / 2)].key > heap[x].key:
            parent = int(x / 2)
            heap[parent], heap[x] = heap[x], heap[parent]
            x = parent
