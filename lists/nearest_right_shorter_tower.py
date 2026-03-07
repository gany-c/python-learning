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


def nearest_left_smaller_number(in_list: List[int]) -> List[int]:

   # print("in_list ", in_list)
   reversed_list = in_list[::-1]
   # print("reversed_list ", reversed_list)
   index_list = nearest_right_smaller_number(reversed_list)
   # print("index_list ", index_list)
   out_list = []

   for i in index_list:
       if i == -1:
           out_list.append(-1)
       else:
           comp_index = len(in_list) - i - 1
           out_list.append(comp_index)

   return out_list[::-1]


def nearest_smaller_number(in_list: List[int]) -> List[int]:

    closest_right_numbers = nearest_right_smaller_number(in_list)
    closest_left_numbers = nearest_left_smaller_number(in_list)

    output = []

    for index, left_val in enumerate(closest_left_numbers):
        right_val = closest_right_numbers[index]

        if right_val == -1 and left_val == -1:
            output.append(-1)
        elif right_val == -1:
            output.append(left_val)
        elif left_val == -1:
            output.append(right_val)
        else:
            left_diff = index - left_val
            right_diff = right_val - index

            if left_diff > right_diff:
                output.append(right_val)
            else:
                output.append(left_val)

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

    #########
    input = [6, 5, 4, 3]
    print("left final output = ", nearest_left_smaller_number(input))

    input = [5, 10, 6, 8, 3]
    print("left final output = ", nearest_left_smaller_number(input))

    #########
    input = [5, 10, 6, 8, 3]
    print("both sides final output = ", nearest_smaller_number(input))
