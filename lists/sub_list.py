"""
Implement a method 'find' that will find the starting index (zero based)
where the second list occurs as a sub-list in the first list.

It should return -1 if the sub-list cannot be found.
Arguments are always given, not empty.
Sample Input 1 list1 = (1, 2, 3) list2 = (2, 3) Sample Output 1
Explanation As second list (2, 3) is sub-list in first list (1, 2, 3) at index 1
Sample Input 2 list1 = (1, 2, 3) list2 = (3, 2) Sample Output -1

"""


def _is_list_match(in_list, sub_list, start):

    for i in range(len(sub_list)):
        if sub_list[i] != in_list[start + i]:
            return False

    return True


def get_sub_list_index(in_list: list[int], sub_list: list[int]) -> int:

    if in_list is None or sub_list is None or len(in_list) == 0 or \
            len(sub_list) == 0 or len(in_list) < len(sub_list):
        raise ValueError("invalid lists provided as input")

    for i in range(len(in_list) - len(sub_list) + 1):
        print(i)
        if _is_list_match(in_list, sub_list, i):
            return i

    return -1


if __name__ == "__main__":

     out_val = get_sub_list_index([1, 3, 5, 7], [3, 5])
     print("out_val = ", out_val)

     out_val = get_sub_list_index([1, 3, 5, 7], [5, 1])
     print("out_val = ", out_val)
