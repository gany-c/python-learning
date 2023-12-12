def get_factorial(input: int) -> int:
    if input < 0:
        return 0
    elif input <= 1:
        return 1
    else:
        return input * get_factorial(input-1)

"""
From Python 3.9 (PEP 585) onwards tuple, list and various other classes are now generic types. 
Using these rather than their typing counterpart is now preferred. 

"""
def get_transpose(input_mat: list[list[int]]) -> list[list[int]]:

    transpose_matrix = []
    print(" Input matrix = ")
    for i, row in enumerate(input_mat):
        for j, cell in enumerate(row):
            print(cell)
            if j > len(transpose_matrix) - 1:
                new_row = []
                transpose_matrix.append(new_row)
            transpose_matrix[j].append(cell)

    return transpose_matrix

# type hints https://stackoverflow.com/questions/39458193/using-list-tuple-etc-from-typing-vs-directly-referring-type-as-list-tuple-etc


if __name__ == "__main__":

    print(get_factorial(5))

    # Test case 1: Factorial of 0 should be 1
    assert get_factorial(0) == 1

    # Test case 2: Factorial of 1 should be 1
    assert get_factorial(1) == 1

    # Test case 3: Factorial of a positive number (e.g., 5)
    assert get_factorial(5) == 120

    # Test case 4: Factorial of a larger positive number (e.g., 10)
    assert get_factorial(10) == 3628800

    # Test case 5: Factorial of a negative number should return 0
    assert get_factorial(-5) == 0

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print(get_transpose(matrix))
