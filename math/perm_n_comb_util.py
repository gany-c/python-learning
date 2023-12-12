"""
=========================================================================
Given N unique numbers, get all permutations of k <=  N numbers
=========================================================================
"""
def get_permutations_recursive(output_list, path_list, in_list, k):
    # print("params = ", output_list, path_list, in_list, k)

    for i in in_list:
        if i not in path_list:
            """
            Even though we are using the 'in' operator on path_list,
            it shouldn't be a set.. because the order matters in permutations.
            """
            if k == 1:
                output_list.append(path_list + [i])
                # we use the '+' instead of append, because we don't want
                # update to the existing set. We want a new set.
            else:
                get_permutations_recursive(output_list, path_list + [i], in_list, k - 1)


def get_permutations_wrapper(in_list, k):
    if not in_list or len(in_list) < k:
        print("Input values are not valid")
        raise ValueError(in_list, k)

    output_list = []
    path_list = []
    get_permutations_recursive(output_list, path_list, in_list, k)
    return output_list

"""
=========================================================================
Given N unique numbers, get all combinations of k <=  N numbers
=========================================================================
"""

def get_combinations_recursive(output_set, path_set, in_list, k):

    """
    # print("params = ", output_set, path_list, in_list, k)

    Notice that the output_set has global state across all paths, it is edited in place
    but the path_set retains its state only through 1 path i.e. the within all recursions of 1 inner loop

    """

    for i in in_list:
        if i not in path_set:
            if k == 1:
                new_set = frozenset(path_set | {i})
                if new_set not in output_set:
                    output_set.add(new_set)
                # we use the '+' instead of append, because we don't want
                # update to the existing set. We want a new set.
            else:
                get_combinations_recursive(output_set, path_set | {i}, in_list, k - 1)


def get_combinations_wrapper(in_list, k):
    if not in_list or len(in_list) < k:
        print("Input values are not valid")
        raise ValueError(in_list, k)

    output_set = set()
    path_set = set()
    get_combinations_recursive(output_set, path_set, in_list, k)
    return output_set


"""
=========================================================================
Your own variation on the n-k combination problem. 
Get unique combinations such that no digit overlap within the selected combination.
=========================================================================
"""


def _get_digits(in_number: int) -> set[int]:
    out_set = set()

    while in_number > 0:
        out_set.add(in_number % 10)
        in_number = in_number // 10

    return out_set


def _get_encountered_digits(in_list: list[int]) -> set[int]:
    out_set = set()

    for item in in_list:
        out_set.update(_get_digits(item))

    return out_set


def _is_disjoint_set(in_set_1, in_set_2):
    for i in in_set_1:
        if i in in_set_2:
            return False

    return True


def get_unique_digit_combs_rec(output_set, path_set, in_list, k):
    print("params = outputset: ", output_set, "path_set: ", path_set, in_list, k)

    path_digits = _get_encountered_digits(path_set)

    for i in in_list:
        item_digits = _get_digits(i)
        if i not in path_set and _is_disjoint_set(item_digits, path_digits):
            if k == 1:
                new_set = frozenset(path_set | {i})
                if new_set not in output_set:
                    output_set.add(new_set)
                # we use the '+' instead of append, because we don't want
                # update to the existing set. We want a new set.
            else:
                get_unique_digit_combs_rec(output_set, path_set | {i}, in_list, k - 1)


def get_unique_digits_combinations_wrapper(in_list, k):
    if not in_list or len(in_list) < k:
        print("Input values are not valid")
        raise ValueError(in_list, k)

    output_set = set()
    path_set = set()
    get_unique_digit_combs_rec(output_set, path_set, in_list, k)
    return output_set


if __name__ == "__main__":
    """
    Permutations - Test
    """
    in_list = [1, 2, 3]
    k = 2
    output = get_permutations_wrapper(in_list, k)
    print("1. output = ", output)

    output = get_permutations_wrapper(in_list, 1)
    print("2. output = ", output)

    output = get_permutations_wrapper(in_list, 3)
    print("3. output = ", output)

    try:
        output = get_permutations_wrapper(in_list, 4)
        print("4. output = ", output)
    except Exception as e:
        print(e)

    in_list = [123, 256, 3091, 655]
    k = 4
    output = get_permutations_wrapper(in_list, k)
    print("5. output = ")
    for perm in output:
        print(perm)

    """
    Combinations - Test
    """
    in_list = [1, 2, 3]
    k = 2
    output = get_combinations_wrapper(in_list, k)
    print("1. combination output = ", output)

    output = get_combinations_wrapper(in_list, 3)
    print("2. combination output = ", output)

    output = get_combinations_wrapper(in_list, 1)
    print("3. combination output = ", output)

    output = get_combinations_wrapper([5, 7, 9, 33], 3)
    print("4. combination output = ", output)

    print(_get_digits(9825723897))

    print(_is_disjoint_set({3, 5, 6}, {4, 8, 9}))
    print(_is_disjoint_set({3, 5, 4}, {4, 8, 9}))

    output = get_unique_digits_combinations_wrapper([59, 7, 9, 33], 3)
    print("1. unique combination output = ", output)

    output = get_combinations_wrapper([59, 7, 9, 33], 3)
    print("5. unique combination for same numbers = ", output)
