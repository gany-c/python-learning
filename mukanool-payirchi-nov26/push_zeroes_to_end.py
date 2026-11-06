from typing import List


def swap(in_list: List[int], i: int, j: int):
    temp = in_list[i]
    in_list[i] = in_list[j]
    in_list[j] = temp


def push_zeroes_to_end(in_list: List[int]) -> List[int]:

    if not in_list:
        return in_list

    i = 0
    j = len(in_list) - 1

    while i < j:

        # mistake made, you didn't check the bounds
        # what if no zeroes are there
        while i < len(in_list) and in_list[i] != 0:
            i = i + 1

        # mistake made, you didn't check the bounds
        # what if everything is a 0
        while j >= 0 and in_list[j] == 0:
            j = j - 1

        if i < j:
            swap(in_list, i, j)

    return in_list


if __name__ == "__main__":
    print("Will push 0s to end")
    print(push_zeroes_to_end([0, 0, 1, 2, 3, 0, 4]))
    print(push_zeroes_to_end([0, 0, 0]))
    print(push_zeroes_to_end([1, 2, 3, 4]))
