
def _get_digits(in_num: int) -> [int]:

    dig_list = []

    while in_num > 0:

        digit = in_num % 10
        dig_list.insert(0, digit)
        in_num = in_num // 10

    return dig_list


def _get_product(dig_list, start, end):
    product = 1
    i = start

    while i <= end:
        product = product * dig_list[i]
        i = i + 1

    return product


def _check_colorful_for_width(dig_list: [int], width, product_set: {int}) -> bool:

    # print("product set", product_set)

    start = 0
    end = width - 1

    while end < len(dig_list):
        prod = _get_product(dig_list, start, end)
        if prod in product_set:
            return False
        else:
            product_set.add(prod)
            start = start + 1
            end = end + 1

    return True


def check_colorful(in_number: int) -> bool:

    dig_list = _get_digits(in_number)
    if len(dig_list) == 1:
        return True
    else:
        product_set = set()
        width = 1
        while width <= len(dig_list):
            if _check_colorful_for_width(dig_list, width, product_set):
                width = width + 1
            else:
                return False

        return True


if __name__ == "__main__":

    print(check_colorful(4))
    print(check_colorful(23))
    print(check_colorful(21))
    print(check_colorful(263))
    print(check_colorful(236))
    """
    7642 is a colorful number 4 * 2 will be considered, 42 will not be considered
    """
    print(check_colorful(7642))


