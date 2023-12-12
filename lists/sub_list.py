def _is_list_match(in_list, sub_list, start):

    for i in range(len(sub_list)):
        if sub_list[i] != in_list[start + i]:
            return False

    return True


def is_sub_list(in_list: list[int], sub_list: list[int]) -> bool:

    if in_list is None or sub_list is None or len(in_list) == 0 or \
            len(sub_list) == 0 or len(in_list) < len(sub_list):
        raise ValueError("invalid lists provided as input")

    for i in range(len(in_list) - len(sub_list) + 1):
        print(i)
        if _is_list_match(in_list, sub_list, i):
            return True

    return False


if __name__ == "__main__":

     out_val = is_sub_list([1, 3, 5, 7], [3, 5])
     print("out_val = ", out_val)

     out_val = is_sub_list([1, 3, 5, 7], [ 5, 1])
     print("out_val = ", out_val)
