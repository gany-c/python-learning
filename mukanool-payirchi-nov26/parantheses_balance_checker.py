
start_set = {'(', '[', '{'}
end_mapping = {
    ')': '(',
    '}': '{',
    ']': '['
}


def check_balanced_brackets(in_str: str) -> bool:

    stack = []

    for c in in_str:
        if c in start_set:
            stack.append(c)
        elif c in end_mapping:
            if len(stack) == 0 or stack[-1] != end_mapping[c]:
                return False
            else:
                stack.pop()

    return len(stack) == 0


if __name__ == "__main__":
    print(check_balanced_brackets("))[]"))
    print(check_balanced_brackets("(())[]"))
    print(check_balanced_brackets(""))
    print(check_balanced_brackets("abc"))
    print(check_balanced_brackets("ab{c}"))
    print(check_balanced_brackets("ab{c}{"))
    print(check_balanced_brackets("{"))
