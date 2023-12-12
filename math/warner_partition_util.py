def _get_all_subsets_for_given_sum(in_list, target, path_set, path_sum, index, out_set):
    if index == len(in_list) - 1:
        if in_list[index] + path_sum == target:
            out_set.add(frozenset(path_set | {in_list[index]}))
    else:
        if in_list[index] + path_sum == target:
            out_set.add(frozenset(path_set | {in_list[index]}))
        else:
            if in_list[index] + path_sum < target:
                _get_all_subsets_for_given_sum(in_list,
                                              target,
                                              path_set | {in_list[index]},
                                              path_sum + in_list[index],
                                              index + 1,
                                              out_set)

            _get_all_subsets_for_given_sum(in_list,
                                          target,
                                          path_set,
                                          path_sum,
                                          index + 1,
                                          out_set)

        # This has to be run in all cases
        _get_all_subsets_for_given_sum(in_list, target, set(), 0, index + 1, out_set)


def _get_all_subsets_for_given_sum_wrapper(in_list: list[int], target: int) -> list[set[int]]:
    path_set = set()
    path_sum = 0
    index = 0
    out_set = set()

    _get_all_subsets_for_given_sum(in_list, target, path_set, path_sum, index, out_set)
    out_list = []

    for sum_set in out_set:
        out_list.append(sum_set)
    return out_list


def _is_disjoint_set(in_set_1, in_set_2):
    for i in in_set_1:
        if i in in_set_2:
            return False

    return True


def _is_fully_new_set(explored_sets, sub_set):
    for old_set in explored_sets:
        if not _is_disjoint_set(old_set, sub_set):
            return False

    return True


def _get_disjoint_set_rec(output_set, path_of_sub_sets, sub_set_list, k):
    # print("params = output_set: ", output_set, "path_of_sub_sets: ", path_of_sub_sets, sub_set_list, k)

    for sub_set in sub_set_list:
        if sub_set not in path_of_sub_sets and _is_fully_new_set(path_of_sub_sets, sub_set):
            if k == 1:
                new_set = frozenset(path_of_sub_sets | {sub_set})
                if new_set not in output_set:
                    output_set.add(new_set)
                # we use the '+' instead of append, because we don't want
                # update to the existing set. We want a new set.
            else:
                _get_disjoint_set_rec(output_set, path_of_sub_sets | {sub_set}, sub_set_list, k - 1)


def _get_disjoint_set_wrapper(sub_set_list, k):
    if not sub_set_list or len(sub_set_list) < k:
        print("Input values are not valid")
        raise ValueError(sub_set_list, k)

    output_set = set()
    path_set = set()
    _get_disjoint_set_rec(output_set, path_set, sub_set_list, k)
    return output_set


def get_all_3_subset_equal_sum(in_list: list[int]):
    """
    Given a list of unique positivie integers, find all ways in which
    the list can be split into  3 subsets such that their sums are equal
    :param in_list: List of distinct integers
    :return: Set of triplets, where triplet has 3 subsets. There is no overlap
    of numbers among the subsets and they add up to the same sum.
    """
    if not in_list or len(in_list) == 0:
        raise ValueError("Input is not valid")

    print("in_list", in_list)
    list_sum = sum(in_list)
    print("list_sum", list_sum)

    if list_sum % 3 != 0:
        raise ValueError("This list cannot be partitioned "
                         "into 3 equal subsets")

    sub_set_sum = list_sum // 3
    print("sub_set_sum", sub_set_sum)

    list_subsets = _get_all_subsets_for_given_sum_wrapper(in_list, sub_set_sum)

    """
    for sum_sub_set in list_subsets:
        print(sum_sub_set)    
    """

    return _get_disjoint_set_wrapper(list_subsets, 3)


if __name__ == "__main__":
    print("Get all 3 subset-combinations with equal sum")

    # in_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    # in_list = [1, 2, 3, 4, 5, 6]
    in_list = [1, 2, 3, 4, 5, 6, 7, 8]
    triple_subset_combinations = get_all_3_subset_equal_sum(in_list)

    for triplet in triple_subset_combinations:
        print(triplet)
        sum_list =[]
        for subset in triplet:
            sum_list.append(sum(subset))
        print(sum_list)

    print("data type of final output: ", type(triple_subset_combinations))
    print("Length of final output", len(triple_subset_combinations))
