if __name__ == "__main__":

    a = 99999999999999
    print(a)
    a_sq = a * a
    print(a_sq)
    print(len(str(a_sq)))

    a_list = [a_sq, 17 * a_sq, 43 * a]
    a_sum = sum(a_list)
    print(a_sum)

