from typing import List


def _single_rotate(in_list: List[int]) -> List[int]:
    """
    making errors even in small pieces of code.
    typos, missing return statements
    :param in_list:
    :return:
    """

    temp = in_list[0]

    for i, v in enumerate(in_list):

        if i == 0:
            continue

        in_list[i-1] = v

    in_list[len(in_list) - 1] = temp

    return in_list


def left_rotate(in_list: List[int], n: int) -> List[int]:

    if not in_list:
        return in_list

    if len(in_list) < 2:
        return in_list

    opt_n = n % len(in_list)

    for i in range(0, opt_n):
        _single_rotate(in_list)

    return in_list

