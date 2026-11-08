from typing import List


def _search(in_list: List[int], start: int, end: int, target: int) -> int:

    # this check is enough to take care of all edge cases
    if start > end:
        return -1

    # start and mid will be the same under 2 conditions
    # 1. start = end
    # 2. start, end are adjacent
    mid = (start + end) // 2

    if in_list[mid] == target:
        return mid
    elif in_list[mid] > target:
        # 2 mistakes made here
        # 1. got the < and > swapped
        # 2. used mid again on RHS instead or target
        return _search(in_list, start, mid - 1, target)
    else:
        return _search(in_list, mid + 1, end, target)


def binary_search(in_list: List[int], target: int) -> int:

    if not in_list:
        return -1
    else:
        return _search(in_list, 0, len(in_list) - 1, target)


if __name__ == "__main__":

    print(binary_search([], 5))
    print(binary_search([4], 5))
    print(binary_search([5], 5))
    print(binary_search([1, 5], 5))
    print(binary_search([5, 55], 5))
    print(binary_search([1, 2, 7], 5))
    print(binary_search([1, 3, 5, 55], 5))

