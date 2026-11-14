from typing import List


def find_possible_pairs(ice_list: List[int], purse: int) -> (int, int):
    """
    You and a friend visit an ice cream parlor.
    You have a fixed amount of money, m, and want to buy exactly two ice creams,
    spending all your money.
    :param ice_list: list of ice cream prices
    :param purse: M
    :return:
    """

    if not ice_list or len(ice_list) < 2:
        return -1, -1

    ice_dict = {}
    for i, v in enumerate(ice_list):
        ice_dict[v] = i

    for i, v in enumerate(ice_list):
        pair = purse - v
        # mistake made, you used v instead of pair in the first check
        # keys is redundant
        if pair in ice_dict.keys() and ice_dict[pair] != i:
            return i, ice_dict[pair]

    return -1, -1


if __name__ == "__main__":
    print(find_possible_pairs([2, 3, 5, 8], 7))
    print(find_possible_pairs([2, 3, 5, 8], 9))
    print(find_possible_pairs([2, 3, 5, 8, 6], 9))
    print(find_possible_pairs([], 8))
