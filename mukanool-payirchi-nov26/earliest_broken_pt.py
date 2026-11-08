from typing import List


def find_breaking_pt(in_list: List, start: int, end: int) -> int:
    """
    :param in_list: list of app build statuses, either passed or broken
    :param start: start of range to check
    :param end: end of range to check
    :return: the first point where the build breaks
    """

    # This was a bug, you had <= first and it will fail in a list with a single broken
    # Write all test cases
    if end < start:
        return -1

    if in_list[start] == "broken":
        return start

    if in_list[end] == "passed":
        return -1

    mid = (start + end) // 2

    if in_list[mid] == "passed":
        return find_breaking_pt(in_list, mid + 1, end)
    else:
        # narrow escape here, what if mid = start = 0, but you are already checking
        if in_list[mid - 1] == "passed":
            return mid
        else:
            return find_breaking_pt(in_list, start, mid - 1)


if __name__ == "__main__":
    print(find_breaking_pt(["passed", "passed", "broken", "broken"], 0, 3))
    print(find_breaking_pt(["passed", "passed", "passed", "passed"], 0, 3))
    print(find_breaking_pt(["broken", "broken", "broken", "broken"], 0, 3))
    print(find_breaking_pt(["passed"], 0, 0))
    print(find_breaking_pt(["broken"], 0, 0))
    print(find_breaking_pt(["passed", "broken"], 0, 1))
