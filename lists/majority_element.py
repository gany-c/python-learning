"""
The majority element in an array is defined as the element that appears
more than ⌊n/2⌋ times, where n is the length of the array.
In other words, it is the element that occurs most frequently
and makes up more than half of the array.

Given an array of integers, the task is to find the majority element and return it.
If there is no majority element, If there is no majority element,
the algorithm should indicate that.

Examples:

Input: [3, 3, 4, 2, 4, 4, 2, 4, 4]
Output: 4

Input: [1, 2, 3, 4, 4, 4, 4]
Output: 4

Input: [1, 2, 3, 4, 5]
Output: -1

Input: [2, 2, 2, 3, 3, 4, 4, 4, 4]
Output: -1
"""


def _find_majority_candidate(in_list: list[int]) -> int:

    count = 0
    major_el = None

    for el in in_list:
        # print("element = ", el, "count = ", count, "major_el", major_el)

        if count == 0:
            # Either starting, or major element has been reset
            count = 1
            major_el = el
        elif el == major_el:
            count += 1
        else:
            count -= 1

    return major_el


def find_majority_element(in_list: list[int]) -> int:
    """
    The solution is 2 pass -
    1. First pass is to find a candidate obj, can be majority element or most recent candidate
    2. Second pass will verify this.
    :param in_list:
    :return:
    """
    if not in_list or len(in_list) == 0:
        raise ValueError("Invalid list is provided as input")

    candidate = _find_majority_candidate(in_list)
    count = 0

    for elem in in_list:
        if elem == candidate:
            count += 1

    if count > len(in_list) // 2:
        return candidate
    else:
        return -1


if __name__ == "__main__":
    in_list = [3, 3, 4, 2, 4, 4, 2, 4, 4]
    print(find_majority_element(in_list))

    print(find_majority_element([1, 2, 3, 4, 4, 4, 4]))

    print(find_majority_element([1, 2, 3, 4, 5]))

    print(find_majority_element([2, 2, 2, 3, 3, 4, 4, 4, 4]))
