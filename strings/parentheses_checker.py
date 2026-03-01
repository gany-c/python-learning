"""
Validate Properly Nested Brackets
Given a string, check if all brackets ('()', '{}', '[]') are properly matched and nested. Return 1 if valid, otherwise return 0.

Example

Input

code_snippet = if (a[0] > b[1]) { doSomething(); }
Output

1
Explanation

All brackets are properly matched: '(' with ')', '[' with ']', and '{' with '}'. No mismatches or improper nesting.

"""


def matches(top_item, c):
    match_map = {'[': ']', '(':')', '{': '}'}
    return match_map[top_item] == c

def areBracketsProperlyMatched(code_snippet):

    if not code_snippet or len(code_snippet) == 0:
        return True

    stack = []

    for c in code_snippet:

        if c in '[{(':
            stack.append(c)
        elif c in ')}]':
            if len(stack) == 0:
                return False

            top_item = stack[-1]
            if matches(top_item, c):
                stack.pop()
            else:
                return False

    return len(stack) == 0


"""
mistakes made:

1. didn't consider inputs like this ']]]', where the stack will be empty while encountering ending braces
2. if not matches(top_item, c) => mismatched braces, if this is encountered you can immediately stop. Even without this the code worked.
"""

# -------------------------
# MAIN METHOD WITH TESTS
# -------------------------
if __name__ == "__main__":

    test_cases = [
        # Valid cases
        ("if (a[0] > b[1]) { doSomething(); }", 1),
        ("()", 1),
        ("[]", 1),
        ("{}", 1),
        ("({[]})", 1),

        # Invalid cases
        ("(]", 0),
        ("([)]", 0),
        ("(((", 0),
        ("]]]", 0),
        ("{[}", 0),
        ("", 1), # Empty string is valid
        ("no brackets here", 1)
    ]

    for i, (input_str, expected) in enumerate(test_cases):
        result = areBracketsProperlyMatched(input_str)
        print(f"Test Case {i+1}: ", end="")
        if result == expected:
            print("PASSED")
        else:
            print(f"FAILED (Expected {expected}, Got {result})")
