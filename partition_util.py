def _explore_subset_sums(path: list[int], current_sum: int, start: int, input_list: list[int], target: int) -> list[int]:

    # print(f" path = {path}")
    if (current_sum + input_list[start]) == target:
        # print("debug 1")
        return path + [input_list[start]]
    elif start == len(input_list) - 1:
        # print("debug 2")
        return None
    else:
        # if the current item fits into the list, with more room, explore a solution with it
        if current_sum + input_list[start] < target:
            # print(f"debug 3 path = {path}")
            # print(f"debug 3 start = {start}")
            # print(f"debug 3 input_list[start] = {input_list[start]}")

            return _explore_subset_sums(path + [input_list[start]],
                                        current_sum + input_list[start],
                                        start + 1,
                                        input_list,
                                        target)

        # regardless of smaller or larger, explore a solution without the current item
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

    if target < 0 or len(input_list) <= 0:
        return []

    path = []
    current_sum = 0
    start = 0

    return _explore_subset_sums(path, current_sum, start, input_list, target)


if __name__ == "__main__":

    tgt = 10
    in_list = [1, 2, 3, 4, 5, 6]
    print(f" sum set = {get_subset_sum(tgt, in_list)}")

    in_list = [200, 4, 5, 6, 1, 2, 3]
    print(f" sum set = {get_subset_sum(tgt, in_list)}")

    tgt = 192
    print(f" sum set = {get_subset_sum(tgt, in_list)}")
