from typing import List
from enum import Enum


# so enums are available in python
class search_state(Enum):
    init = 0
    min_found = 1
    min_max_found = 2
    new_min_found = 3


def find_best_dates(in_list: List[int]) -> tuple[int, int, int]:
    """
    Given an array of stocks prices, find the best days to buy and sell

    :param in_list: prices on consecutive days
    :return: buying date index, selling date index, profit
    """

    if not in_list or len(in_list) < 2:
        return -1, -1, 0

    curr_state = search_state.init
    min_index = -1
    max_index = -1
    new_min_index = -1
    profit = 0

    for i, v in enumerate(in_list):

        if curr_state == search_state.init:
            min_index = i
            curr_state = search_state.min_found
        elif curr_state == search_state.min_found:
            if v < in_list[min_index]:
                min_index = i
            elif v > in_list[min_index]:
                max_index = i
                profit = v - in_list[min_index]
                curr_state = search_state.min_max_found
        elif curr_state == search_state.min_max_found:
            if v > in_list[max_index]:
                max_index = i
                profit = v - in_list[min_index]
            if v < in_list[min_index]:
                new_min_index = i
                curr_state = search_state.new_min_found
        elif curr_state == search_state.new_min_found:
            if v < in_list[new_min_index]:
                new_min_index = i
            elif v > in_list[new_min_index]:
                if v - in_list[new_min_index] > profit:
                    min_index = new_min_index
                    max_index = i
                    profit = v - in_list[new_min_index]
                    curr_state = search_state.min_max_found
                    new_min_index = -1

    if curr_state == search_state.min_max_found or curr_state == search_state.new_min_found:
        return min_index, max_index, profit
    else:
        return -1, -1, 0


if __name__ == "__main__":
    print(find_best_dates([1, 2, 5, 3, 7]))
    print(find_best_dates([2, 5, 3, 1, 7, 4]))
    print(find_best_dates([5, 5, 4, 4, 2, 2]))
    print(find_best_dates([4, 4, 4, 4, 4, 4]))


