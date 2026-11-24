
def insertion_sort(in_list: [int]) -> [int]:
    output = []

    for outer_val in in_list:

        if len(output) == 0:
            output.append(outer_val)
        else:
            inserted: bool = False
            for j, val in enumerate(output):
                if val > outer_val:
                    output.insert(j, outer_val)
                    inserted = True
                    # missed it - bugs are always there, write test cases
                    break
            # missed this too - insertion at the very end
            if not inserted:
                output.append(outer_val)

    return output


if __name__ == "__main__":
    print(insertion_sort([9, 55, 7, 0]))
    print(insertion_sort([]))
    print(insertion_sort([2]))
    print(insertion_sort([99, 55, 7, 0]))
    print(insertion_sort([9, 9, 9]))
    print(insertion_sort([9, 99, 999]))

