from typing import List
def reverse_words(s: str) -> str:
    print(s)
    print(len(s))

    if len(s) < 2:
        return s

    out_sentence = ""
    word_start = 0
    word_end = 0

    while word_start < len(s):

        while word_start < len(s) and s[word_start] == " ":
            word_start = word_start + 1

        if word_start >= len(s):
            break

        print("word_start = ", word_start)
        word_end = word_start
        print("1. word_end = ", word_end)
        while  word_end < len(s) and s[word_end] != " ":
            word_end = word_end + 1

        print("2. word_end = ", word_end)
        word = s[word_start: word_end]
        print("Word = ", word)

        word_start = word_end

        out_sentence = word + " " + out_sentence
        print(out_sentence)
        print("=======================")

    return out_sentence

def _find_longest_string_in_array(input: List[str]) -> str:

    max_len = 0
    max_str = ''

    for token in input:
        if len(token) > max_len:
            max_len = len(token)
            max_str = token

    return max_str


def _find_strings_with_unique_chars(input: str) -> List[str]:
    out = []
    temp_map = {}
    word_start = 0
    word_end = 1

    temp_map[input[word_start]] = 0

    while word_start < len(input) and word_end < len(input):
        if input[word_end] in temp_map:
            out.append(input[word_start: word_end])
            repeated_char = input[word_end]
            # print(repeated_char)
            repeated_char_pos = temp_map[repeated_char]
            # print(repeated_char_pos)
            word_start = temp_map[repeated_char] + 1
            word_end = word_end + 1

            #: clean map
            temp_map = {}
            temp = word_start
            while temp < word_end:
                temp_map[input[temp]] = temp
                temp = temp + 1

        else:
            temp_map[input[word_end]] = word_end
            word_end = word_end + 1

    if word_start < word_end:
        out.append(input[word_start: word_end])

    return out

def find_longest_unique_substring(s: str) -> str:
    subs = _find_strings_with_unique_chars(s)
    return _find_longest_string_in_array(subs)

if __name__ == "__main__":
    """
    # Works well, commented to avoid clutter in testing
    out_sentence = reverse_words("The quick brown fox jumped over the lazy dog")
    print("output  = ", out_sentence)

    out_sentence = reverse_words("They always need to have things explained.")
    print("output  = ", out_sentence)

    out_sentence = reverse_words("        They always need to have things explained.        ")
    print("output  = ", out_sentence)


    test_arr = ['aa', 'swagger', 'intellij', 'indeed.com']
    print(_find_longest_string_in_array(test_arr))

    # print(_find_strings_with_unique_chars("abcded"))
    # print(_find_strings_with_unique_chars("aaaaded"))
    print(_find_strings_with_unique_chars("aaaa"))
    """
    print(find_longest_unique_substring("abcdedzyxwvutsaaaa"))
