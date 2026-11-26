from typing import List
import string


def designer_pdf_viewer(h: List[int], word: str) -> int:
    """
    mistake made - gave sum of heights instead of Max height x width
    :param h:
    :param word:
    :return:
    """

    char_to_pos_dict = {}
    for i, c in enumerate(string.ascii_lowercase):
        char_to_pos_dict[c] = i

    pos_to_height_dict = {}
    for pos, height in enumerate(h):
        pos_to_height_dict[pos] = height

    h_max = 0
    for c in word:
        height = pos_to_height_dict[char_to_pos_dict[c]]
        if height > h_max:
            h_max = height

    return h_max * len(word)
