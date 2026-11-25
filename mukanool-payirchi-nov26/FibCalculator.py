class FibCalculator:

    def __init__(self):
        self._memo_map = {}

    def get_fibonacci_number(self, in_number):
        if in_number < 0:
            return None
        elif in_number == 0:
            return 0
        elif in_number == 1:
            return 1
        elif in_number in self._memo_map:
            return self._memo_map[in_number]
        else:
            result = self.get_fibonacci_number(in_number - 1) + self.get_fibonacci_number(in_number - 2)
            self._memo_map[in_number] = result
            return result


if __name__ == "__main__":
    calc = FibCalculator()
    print(calc.get_fibonacci_number(6))
    print(calc.get_fibonacci_number(3))
    print(calc.get_fibonacci_number(4))
    print(calc.get_fibonacci_number(10))
    print(calc.get_fibonacci_number(100))

