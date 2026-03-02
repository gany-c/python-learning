"""
Agoda - Thadavals

Given a list of unsorted numbers, for each number,
return the index of the closest smaller number to the right
"""
from typing import List


def nearest_right_smaller_number(in_list: List[int]) -> List[int]:

    output = [-1 for i in in_list]
    stack = []

    for index, value in enumerate(in_list):
        # print(index, value)

        if index == len(in_list) - 1:
            break

        stack.append((index, value))

        while len(stack) > 0:
            if stack[-1][1] > in_list[index + 1]:
                popped_tuple = stack.pop()
                popped_index = popped_tuple[0]
                output[popped_index] = index + 1
            else:
                break

    return output


if __name__ == '__main__':

    input = [6, 5, 4, 3]
    print("final output = ", nearest_right_smaller_number(input))

    input = [6, 7, 8, 9]
    print("final output = ", nearest_right_smaller_number(input))

    input = [6, 7, 8, 1]
    print("final output = ", nearest_right_smaller_number(input))

    input = [5, 10, 6, 8, 3]
    print("final output = ", nearest_right_smaller_number(input))

    input = [2, 7, 3, 5, 4, 6, 8, 1]
    print("final output = ", nearest_right_smaller_number(input))
