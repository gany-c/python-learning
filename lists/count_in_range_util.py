"""
https://prepinsta.com/atlassian-coding-questions-and-answers/

The above link has an over complicated solution.

The task is to determine the number of elements within a specified range
in an unsorted array. Given an array of size n, the goal is to count
the elements that fall between two given values, i and j, inclusively.
Examples:

Input:
Array: [1, 3, 3, 9, 10, 4]
Range 1: i = 1, j = 4
Range 2: i = 9, j = 12

Output:
For Range 1: 4
For Range 2: 2
"""


def get_count_range(in_list: list[int], min: int, max:int) -> int:

    if not in_list or len(in_list) == 0:
        raise ValueError("Invalid list")

    if min > max:
        raise ValueError("Min should be lesser than Max")

    count = 0

    for i in in_list:
        if min <= i and i <= max:
            count += 1

    return count


if __name__ == "__main__":
    in_list = [1, 3, 3, 9, 10, 4]
    print(get_count_range(in_list, 1, 4))
    print(get_count_range(in_list, 9, 12))
