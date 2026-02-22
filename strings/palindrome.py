"""#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'isAlphabeticPalindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code as parameter.
#
Check Palindrome by Filtering Non-Letters
Given a string containing letters, digits, and symbols, determine if it reads the same forwards and backwards when considering only alphabetic characters (case-insensitive).

Example

Input

code = A1b2B!a
Output

1

"""


def isAlphabeticPalindrome(code):
    # Write your code here
    if code is None:
        return False

    filtered = ''
    reverse_fltr = ''

    for c in code.lower():
        if not c.isalpha():
            continue

        filtered = filtered + c
        reverse_fltr = c + reverse_fltr

    return filtered == reverse_fltr


if __name__ == '__main__':
    code = input()

    result = isAlphabeticPalindrome(code)

    print(int(result))
