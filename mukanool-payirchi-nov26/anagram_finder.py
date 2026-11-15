from typing import List, Dict


def _create_count_dict(target_str, start, end) -> Dict:
    """
    Lots of index typos here i.e. using the index instead of the
    value at the index

    :param target_str:
    :param start:
    :param end:
    :return:
    """
    output = {}

    i = start
    while i <= end:
        i_char = target_str[i]
        if i_char in output:
            output[i_char] = output[i_char] + 1
        else:
            output[i_char] = 1
        i = i + 1

    return output


def _update_count_dict(sliding_dict, input_str, start, end) -> Dict:

    if end >= len(input_str) - 1:
        return {}

    start_chr = input_str[start]
    sliding_dict[start_chr] = sliding_dict[start_chr] - 1

    if sliding_dict[start_chr] <= 0:
        del sliding_dict[start_chr]

    # Mistake made - index vs index + 1
    end_chr = input_str[end + 1]
    if end_chr in sliding_dict:
        sliding_dict[end_chr] = sliding_dict[end_chr] + 1
    else:
        sliding_dict[end_chr] = 1

    return sliding_dict


def anagram_finder(input_str: str, target_str: str) -> List[str]:
    """
    You're given two strings:
    - s: A longer string to search.
    - p: A shorter pattern.
    Find every substring in s which is an anagram of p
    :param input_str:
    :param target_str:
    :return:
    """

    if not input_str or not target_str:
        return []

    if len(input_str) < len(target_str):
        return []

    output = []

    target_dict = _create_count_dict(target_str, 0, len(target_str) - 1)
    sliding_dict = None

    i = 0
    while i <= len(input_str) - len(target_str):

        if not sliding_dict:
            sliding_dict = _create_count_dict(input_str, i, i + len(target_str) - 1)

        if sliding_dict == target_dict:
            output.append(input_str[i: i + len(target_str)])

        sliding_dict = _update_count_dict(sliding_dict, input_str, i, i + len(target_str) - 1)
        i = i + 1

    return output


if __name__ == "__main__":
    print(anagram_finder("cbaebabacd", "abc"))
    print(anagram_finder("abab", "ab"))
