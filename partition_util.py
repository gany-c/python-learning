def _explore_subset_sums(path: list[int], current_sum: int, start: int, input_list: list[int], target: int) -> list[int]:

    # print(f" DEBUG 0 path = {path}")
    # THE LISTS ARE CONCATENATED USING '+' INSTEAD OF append()
    # append() WORKS IN-PLACE, AND RETURNS None - THUS, THE INVOKED METHOD GETS None
    if (current_sum + input_list[start]) == target:
        # print("debug 1")
        return path + [input_list[start]]
    elif start == len(input_list) - 1:
        # print("debug 2")
        return None
    else:

        out_path = None
        # if the current item fits into the list, with more room, explore a solution with it
        if current_sum + input_list[start] < target:
            # print(f"debug 3 path = {path}")
            # print(f"debug 3 start = {start}")
            # print(f"debug 3 input_list[start] = {input_list[start]}")

            out_path = _explore_subset_sums(path + [input_list[start]],
                                        current_sum + input_list[start],
                                        start + 1,
                                        input_list,
                                        target)

        # regardless of smaller or larger, explore a solution without the current item
        if not out_path:
            # print(f"debug 3.5 path = {path}")
            out_path = _explore_subset_sums(path, current_sum, start + 1, input_list, target)

        """
        # explore subsets starting at current point
        The starting point could be smaller than target - upper list sum difference
        It could be larger
        Or it could be larger than the target itself - In this case we could use an additional condition to filter it.
        """
        if not out_path:
            # print("debug 4")
            out_path = _explore_subset_sums([input_list[start]], input_list[start], start + 1, input_list, target)

        return out_path


def get_subset_sum(target: int, input_list: list[int]) -> list[int]:
    """
    Check if any of the possible subsets adds up to a target sum
    :param target:
    :param input_list:
    :return: returns the first such subset found.
    """

    if target < 0 or len(input_list) <= 0:
        return []

    path = []
    current_sum = 0
    start = 0

    return _explore_subset_sums(path, current_sum, start, input_list, target)


def get_k_subsets_of_equal_sum(k: int, input_list: list[int]) -> list[list[int]]:
    """
    determine if it is possible to split the input list into k equal sum subsets,
    and return 1 such combination of subsets
    :param k:
    :param input_list: distinct positive numbers
    :return:
    """

    if k <= 0 or len(input_list) <= 0:
        return None

    list_sum = sum(input_list)

    if (list_sum % k) != 0:
        # print("It is not possible to split the list")
        return None

    subset_sum = list_sum/k
    out_list = []

    # We can skip the recursive search for the last subset/ iteration, It is already there as the remainder
    while k > 1:
        # print(f" Debug 1  subset_sum = {subset_sum} ")
        # print(f" Debug 1  input_list = {input_list} ")
        subset = get_subset_sum(subset_sum, input_list)
        # print(f" Debug 2  sum set = {subset}")
        out_list.append(subset)
        # GETTING THE DIFFERENCE OF 2 LISTS. '-' DOESN'T WORK
        input_list = [x for x in input_list if x not in subset]
        k = k - 1

    out_list.append(input_list)

    return out_list


if __name__ == "__main__":
    """
    ALL OF THESE TEST-CASES WORK, COMMENTED OUT TO AVOID CLUTTER
    tgt = 10
    in_list = [1, 2, 3, 4, 5, 6]
    print(f" sum set = {get_subset_sum(tgt, in_list)}")

    in_list = [200, 4, 5, 6, 1, 2, 3]
    print(f" sum set = {get_subset_sum(tgt, in_list)}")

    tgt = 192
    print(f" sum set = {get_subset_sum(tgt, in_list)}")

    tgt = 7
    in_list = [1, 5, 4, 2, 6, 3]
    print(f" Final sum set = {get_subset_sum(tgt, in_list)}")

    """
    list_of_lists = get_k_subsets_of_equal_sum(3, [1, 5, 4, 2, 6, 3])
    print(f"list of lists = {list_of_lists}")

