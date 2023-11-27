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
                get_permutations_recursive(output_list, path_list + [i], in_list, k-1)


def get_permutations_wrapper(in_list, k):

    if not in_list or len(in_list) < k:
        print("Input values are not valid")
        raise ValueError(in_list, k)

    output_list = []
    path_list = []
    get_permutations_recursive(output_list, path_list, in_list, k)
    return output_list


if __name__ == "__main__":
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
