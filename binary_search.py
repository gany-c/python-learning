# Type in your Binary Search code here
from math import floor


def binary_search(input, target):
    #print(f"Binary Search is starting {input}, {target}")

    if input is None or len(input) == 0:
        print("Invalid input array")
        return -1

    start = 0
    end = len(input) -1

    while start <= end:
        mid = floor((start + end)/2)

        if input[mid] == target:
            return mid
        elif input[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    print("Target not found")
    return -1


if __name__ == "__main__":
    print(binary_search([1, 2, 3, 4, 5], 4))
    print(binary_search([6, 22, 51, 73, 189, 673, 1000, 2000], 4))
    print(binary_search([6, 22, 51, 73, 189, 673, 1000, 2000], 150))
    print(binary_search([6, 22, 51, 73, 189, 673, 1000, 2000], 6))
    print(binary_search([1, 3, 5, 7, 9], 9))
    input = [i for i in range(100000)]
    target = 55555
    print(len(input))
    print(binary_search(input, target))


