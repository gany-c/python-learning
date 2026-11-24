def _swap(in_list: [int], i: int, j: int):

    temp = in_list[i]
    in_list[i] = in_list[j]
    in_list[j] = temp


def _compare_n_swap(in_list: [int], i: int, j: int):

    if in_list[j] < in_list[i]:
        _swap(in_list, i, j)


def _place_pivot(in_list: [int], start: int, end: int) -> int:
    """
    Your understanding of the pivot placing is fuzzy around the edges,
    Some corner cases are getting missed, understand it carefully.
    :param in_list:
    :param start:
    :param end:
    :return:
    """

    pivot = in_list[start]
    i = start + 1
    j = end

    while i < j:

        # mistake made - had it originally as in_list[i] <= pivot
        # this causes an infinite loop when items are the same
        while i <= j and in_list[i] <= pivot:
            i = i + 1

        while i < j and in_list[j] > pivot:
            j = j - 1

        if i < j:
            _swap(in_list, i, j)
            """
            # mistake made - fails when the last non-compared element is at i = j
            i = i + 1
            j = j - 1
           """

    # print("start = ", start, "pivot pos = ", i-1 )
    if start != i - 1:
        _swap(in_list, start, i - 1)
    return i - 1


def _quick_sort_rec(in_list: [int], start: int, end: int):

    if start >= end:
        return

    if end - start == 1:
        _compare_n_swap(in_list, start, end)
        return

    pivot_pos = _place_pivot(in_list, start, end)

    _quick_sort_rec(in_list, start, pivot_pos - 1)
    _quick_sort_rec(in_list, pivot_pos + 1, end)


def quick_sort(in_list: [int]):

    if in_list and len(in_list) > 1:
        _quick_sort_rec(in_list, 0, len(in_list) - 1)

    return in_list


if __name__ == "__main__":

    print(quick_sort([]))
    print(quick_sort([5]))
    print(quick_sort([5, 2]))
    print(quick_sort([2, 5]))
    print(quick_sort([5, 2, 3]))
    print(quick_sort([5, 2, 3, 1]))
    print(quick_sort([0, 5, 2, 3, 1]))
    print(quick_sort([0, 5, 2, 3, 1, 100]))
    print(quick_sort([99, 88, 77, 66, 55]))
    print(quick_sort([5, 3, 8, 2]))
    print(quick_sort([5, 8, 2, 3]))
    print(quick_sort([5, 5, 5]))
