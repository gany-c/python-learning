"""
In place merge will not work with simple swaps. The second list pointer will not move

Each 2nd list item has to be placed in the right place in the first list.
and then the remaining items have to be moved.

def _in_place_merge(in_list: list[int], start: int, mid: int, end: int):

    i = start
    j = mid

    while i < mid and j <= end:

        if in_list[i] > in_list[j]:
            _swap(in_list, i, j)
            i = i + 1
        else:
            
"""


def merge(in_list: list[int], start: int, mid: int, end: int):
    """

    :param in_list: input list of integers
    :param start: start of first array
    :param mid: start of second array, first array ends at mid - 1
    :param end: end of sencod array, last element of second array is here
    :return: void
    """

    combined_size = end - start + 1
    temp = [None] * combined_size

    i = start
    j = mid
    temp_index = 0

    # merge
    while i < mid and j <= end:

        if in_list[i] <= in_list[j]:
            temp[temp_index] = in_list[i]
            i = i + 1
        else:
            temp[temp_index] = in_list[j]
            j = j + 1

        temp_index = temp_index + 1


    # residues, they can be inside an if-else block, but doesn't make a difference.
    while i < mid:
        temp[temp_index] = in_list[i]
        i = i + 1
        temp_index = temp_index + 1

    while j <= end:
        temp[temp_index] = in_list[j]
        j = j + 1
        temp_index = temp_index + 1

    # print("temporary sorted array", temp)
    # copy back to main array
    i = start
    for m in temp:
        in_list[i] = m
        i = i + 1


def merge_sort_recurse(in_list, start, end):
    """
    Go to 1 item length level, start merging upwards
    :param in_list:
    :param start:
    :param end:
    :return:
    """
    # print("start and end are ", start, end)
    if start < end:
        # integer division
        mid = (start + end)//2
        merge_sort_recurse(in_list, start, mid)
        merge_sort_recurse(in_list, mid+1, end)
        merge(in_list, start, mid+1, end)


def merge_sort(in_list: list[int]):

    if in_list is None or len(in_list) <= 1:
        return

    end = len(in_list)-1

    merge_sort_recurse(in_list, 0, end)


if __name__ == "__main__":
    """
    print("Testing merges:")
    in_list = [1, 2, 3, 100, 5, 6]
    merge(in_list, 0, 4, 5)
    print(in_list)

    in_list = [5, 6, 1, 2, 3, 100]
    merge(in_list, 0, 2, 5)
    print(in_list)

    in_list = [1, 3, 5, 7, 9, 11, 2, 4, 6, 8, 10]
    merge(in_list, 0, 6, 10)
    print(in_list)

    in_list = [5, 3]
    merge(in_list, 0, 1, 1)
    print(in_list)
    """


    print("Testing mergesort:")

    in_list = [3, 23, 13, 100, 5, 6]
    merge_sort(in_list)
    print(in_list)

    in_list = [99, 88, 77, 6674, 789, 0, 3, 3, 2, 1, 0]
    merge_sort(in_list)
    print(in_list)

    in_list = [6674]
    merge_sort(in_list)
    print(in_list)

    in_list = [1, 2, 6674]
    merge_sort(in_list)
    print(in_list)

    in_list = [88, 80]
    merge_sort(in_list)
    print(in_list)
