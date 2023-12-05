def _swap(in_list: list[int], i: int, j: int):
    temp = in_list[i]
    in_list[i] = in_list[j]
    in_list[j] = temp


def _bubble_up(in_list: list[int], loc: int):

    if loc <= 0:
        return

    parent = None
    if loc % 2 == 0:
        parent = loc//2 - 1
    else:
        parent = loc//2

    if in_list[loc] > in_list[parent]:
        _swap(in_list, loc, parent)
        _bubble_up(in_list, parent)


def _max_heapify(in_list: list[int]):
    """
    For building the max heap at the beginning of the process.

    :param in_list:
    :return:
    """
    i = len(in_list) - 1
    while i > 0:
        _bubble_up(in_list, i)
        i = i - 1


def _correct_down(in_list: list[int], heap_end: int):
    """
    For correcting the heap after the top element is swapped
    :param in_list:
    :param heap_end:
    :return:
    """

    start = 0
    next_start = start

    while True:

        left = start * 2 + 1
        # if left lies outside the heap boundary,
        # there is nothing left to check
        if left > heap_end:
            break

        if in_list[left] > in_list[start]:
            _swap(in_list, left, start)
            next_start = left

        right = start * 2 + 2
        # if right lies outside the heap boundary,
        # there is nothing left to check
        if right > heap_end:
            break

        if in_list[right] > in_list[start]:
            _swap(in_list, right, start)
            next_start = right

        # The is already intact
        if next_start == start:
            break
        start = next_start
        # print("Moving to next_start", next_start)


def heap_sort(in_list: list[int]):
    """
    Goal - sort in ascending order.
    1. Create a Max heap.
    2. In a loop -
        a. swap the top most element to the bottom
        b. reduce the heap limit by 1
        c. correct the heap

    :param in_list:
    :return:
    """
    if in_list is None or len(in_list) < 2:
        return

    _max_heapify(in_list)
    print("List after heapification", in_list)

    heap_end = len(in_list) - 1
    while heap_end > 0:
        _swap(in_list, 0, heap_end)
        heap_end = heap_end - 1
        _correct_down(in_list, heap_end)
        # print("List state", in_list, "heap end", heap_end)


if __name__ == "__main__":

    in_list = [1, 6, 8, 2, 3]
    heap_sort(in_list)
    print(in_list)

    in_list = [100, 6, 8, 2, 3, 987, 6, 86]
    heap_sort(in_list)
    print(in_list)

    in_list = [100, 6]
    heap_sort(in_list)
    print(in_list)

    in_list = [6, 100]
    heap_sort(in_list)
    print(in_list)
