def _swap(in_list: list[int], pos1: int, pos2: int):

    temp = in_list[pos1]
    in_list[pos1] = in_list[pos2]
    in_list[pos2] = temp


def _place_pivot(in_list: list[int], start: int, end: int) -> int:

    pivot_pos = start
    pivot = in_list[pivot_pos]
    i = start + 1
    j = end

    while i < j:
        """
        The greater than equals will cause i to go past j 
        and may be even the list length by 1, (termination not inspection)
        That will not cause an index out of bounds error.
        """
        while i <= j and in_list[i] <= pivot:
            i = i + 1

        # print("stop point for i", i)

        while i < j and pivot < in_list[j]:
            j = j - 1

        # print("stop point for j", j)

        if i < j:
            _swap(in_list, i, j)

    if pivot_pos < i-1:
        _swap(in_list, pivot_pos, i-1)
        return i-1
    else:
        return pivot_pos


def quick_sort(in_list, start, end):

    if in_list is None or len(in_list) <= 0:
        return

    if end - start <= 0:
        return

    if end - start == 1:
        if in_list[start] > in_list[end]:
            _swap(in_list, start, end)
    else:

        pivot_pos = _place_pivot(in_list, start, end)

        if pivot_pos - start > 1:
            quick_sort(in_list, start, pivot_pos - 1)

        if end - pivot_pos > 1:
            quick_sort(in_list, pivot_pos + 1, end)


if __name__ == "__main__":
    print("Checking the Quicksort utilities")

    in_ist = [1, 2, 3, 4, 5, 6]
    _swap(in_ist, 1, 4)
    print(in_ist)

    in_list = [5, 1, 2, 6, 100, 101]
    pos = _place_pivot(in_list, 0, 5)
    print("1. pivot position", pos)
    print("1. After placing pivot", in_list)

    in_list = [1, 2, 5, 6, 100, 101]
    pos = _place_pivot(in_list, 0, 5)
    print("2. pivot position", pos)
    print("2. After placing pivot", in_list)

    in_list = [7, 10, 9, 8, 6, 5, 4]
    pos = _place_pivot(in_list, 0, 6)
    print("3. pivot position", pos)
    print("3. After placing pivot", in_list)

    in_list = [10, 9, 8, 6, 5, 4]
    pos = _place_pivot(in_list, 0, 5)
    print("4. pivot position", pos)
    print("4. After placing pivot", in_list)

    print("Checking Quicksort: ")

    in_ist = [1, 2, 3, 4, 5, 6]
    quick_sort(in_ist, 0,  5)
    print("0. After quicksort", in_ist)

    in_list = [5, 1, 2, 6, 100, 101]
    quick_sort(in_list, 0, 5)
    print("1. After quicksort", in_list)

    in_list = [1, 2, 5, 6, 100, 101]
    quick_sort(in_list, 0, 5)
    print("2. After quicksort", in_list)

    in_list = [7, 10, 9, 8, 6, 5, 4]
    quick_sort(in_list, 0, 6)
    print("3. After quicksort", in_list)

    in_list = [10, 9, 8, 6, 5, 4]
    quick_sort(in_list, 0, 5)
    print("4. After quicksort", in_list)
