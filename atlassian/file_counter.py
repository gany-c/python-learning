"""
The total size of all files stored; and

The top N collections (by file size) where N can be a user-defined value

file1.txt (size: 100)
file2.txt (size: 200) in collection "collection1"
file3.txt (size: 200) in collection "collection1"
file4.txt (size: 300) in collection "collection2"
file5.txt (size: 10)
"""

class CustomFile:

    def __init__(self, name, size, collection=None):
        self.name = name
        self.size = size
        self.collection = collection

    def __repr__(self):
        return f"{self.name}, {self.size}, {self.collection};"


list_files = []


def get_total_size(in_list: list[CustomFile]) -> int:

    if not in_list:
        raise ValueError("Invalid input list")

    sum = 0

    for c_file in in_list:

        if not c_file:
            continue
        else:
            sum += c_file.size

    return sum


def _get_col_dict(in_list: list[CustomFile]):

    col_dict = {}

    for cust_file in in_list:
        if not cust_file.collection:
            continue

        if cust_file.collection in col_dict:
            col_dict[cust_file.collection] += cust_file.size
        else:
            col_dict[cust_file.collection] = cust_file.size

    return col_dict


def _custom_comp(col_score_tuple):
    print("In custom comp: ", col_score_tuple)
    return -1 * col_score_tuple[1]


def get_top_k_collections(in_list: list[CustomFile], k: int) -> list[str]:
    """
    1. get dict of collection to size
    2. convert dict to list of col_name - size
    3. sort this descending order
    4. return top k of this list
    :param in_list:
    :param k: user define value
    :return:
    """

    if k == 0:
        return []

    col_dict = _get_col_dict(in_list)
    collection_size_list = list(col_dict.items())
    sorted_list = sorted(collection_size_list, key=_custom_comp)

    out_list = []

    for score_tuple in sorted_list:
        out_list.append(score_tuple[0])
        k = k - 1

    return out_list


def get_report(in_list: list[CustomFile], k: int) -> dict:
    """
    Actual steps

    :param in_list:
    :param k:
    :return:
    """

    out_dict = {}
    total_size = get_total_size(in_list)

    out_dict["total_size"] = total_size
    if k > 0:
        out_dict["top_k "] = get_top_k_collections(in_list, k)

    return out_dict


if __name__ == "__main__":

    list_files = [CustomFile("file1.txt", 100), CustomFile("file2.txt", 200, "collection1"),
                  CustomFile("file3.txt", 200, "collection1"),
                  CustomFile("file4.txt", 300, "collection2"),
                  CustomFile("file5.txt", 10)]

    """
    Intermediate steps
    
    print(list_files)
    print(get_total_size(list_files))
    temp_dict = _get_col_dict(list_files)
    temp_list = list(temp_dict.items())
    print(sorted(temp_list, key=_custom_comp))    
    """



