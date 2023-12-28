"""
https://prepinsta.com/atlassian-coding-questions-and-answers/

Given an array representing the heights of towers, the task is to find, for each tower,
the index of the nearest tower that is shorter than it.
The search for a shorter tower can be performed by looking to the left and right sides of each tower.

The following rules apply:

If there are two or more smaller towers at the same distance from the current tower,
choose the tower with the smallest height.
If two towers have the same height, choose the one with the smaller index.
"""
def _backward_pass(in_list: list[int]) -> list[int]:
    out_list = [-1] * len(in_list)

    stack = []

    # iterating from the right end, move left
    for index, height in reversed(list(enumerate(in_list))):
        #print(index, height, stack)

        # if the stack has an index of a tower that is taller,
        while len(stack) > 0 and in_list[stack[-1]] > height:
            # remove the element from the stack
            tower_index = stack.pop()
            # In the output, set that tower's shorter neighbor as this one
            out_list[tower_index] = index

        # push the current index into the stack
        stack.append(index)

    # print("stack = ", stack)
    # for each tower, find shorter neighbors to the left
    return out_list


def _forward_pass(in_list: list[int]) -> list[int]:
    out_list = [-1] * len(in_list)

    stack = []

    for index, height in enumerate(in_list):

        while len(stack) > 0 and in_list[stack[-1]] > height:
            tower_index = stack.pop()
            out_list[tower_index] = index

        stack.append(index)

    # print("stack = ", stack)
    # Analogous to backward: for each tower, find shorter neighbors to the right
    return out_list


def find_nearest_shorter_tower(in_list: list[int]) -> list[int]:
    """
    All that you are doing is merging the 2 indices here

    Don't worry about the spaghetti of if-else. The verbosity is caused by these 2 conditions:
    ACTUAL ALGORITHM IS VERY SIMPLE

    If there are two or more smaller towers at the same distance from the current tower,
    choose the tower with the smallest height.
    If two towers have the same height, choose the one with the smaller index.


    :param in_list:
    :return:
    """
    print("in_list = ", in_list)
    f_indices = _forward_pass(in_list)
    print("forward pass = ", f_indices)

    b_indices = _backward_pass(in_list)
    print("backward pass = ", b_indices)

    out_list = []

    for i in range(0, len(in_list)):
        #print(i)
        if f_indices[i] == b_indices[i]:
            out_list.append(f_indices[i])
        elif f_indices[i] == -1:
            out_list.append(b_indices[i])
        elif b_indices[i] == -1:
            out_list.append(f_indices[i])
        else:
            sep_1 = abs(i - f_indices[i])
            sep_2 = abs(i - b_indices[i])

            # if the shorter towers are equidistant
            if sep_1 == sep_2:
                height_1 = in_list[f_indices[i]]
                height_2 = in_list[b_indices[i]]

                # if the shorter towers are equidistant have the same height
                if height_1 == height_2:
                    if f_indices[i] < b_indices[i]:
                        out_list.append(f_indices[i])
                    else:
                        out_list.append(b_indices[i])

                # choose the shorter of the 2 equidistant towers
                elif height_1 < height_2:
                    out_list.append(f_indices[i])
                else:
                    out_list.append(b_indices[i])
            elif sep_1 < sep_2:
                out_list.append(f_indices[i])
            else:
                out_list.append(b_indices[i])

    return out_list


"""
x = [3, 2, 1]

print(_forward_pass(in_list=x))

y = [1, 2, 3]

print(_backward_pass(in_list=y))
"""

print(find_nearest_shorter_tower([4, 5, 6, 7, 3]))
print("============================")
print(find_nearest_shorter_tower([1, 3, 2]))
print("============================")
print(find_nearest_shorter_tower([4, 8, 3, 5, 3]))
