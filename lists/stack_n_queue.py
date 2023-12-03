
class ListCircularQueue:

    def __init__(self, size: int):
        self.holder = [None] * size

        # Place to insert the next item, last item inserted is below this
        self.back = 0

        # Place to remove the item from
        self.front = 0

    def __str__(self):
        return f"front = {self.front}, back = {self.back}, holder = {self.holder}"

    def enqueue(self, value: int):

        future_back = (self.back + 1) % len(self.holder)
        if future_back == self.front:
            raise Exception("The queue is full")
        else:
            self.holder[self.back] = value
            self.back = future_back

    def dequeue(self) -> int:

        if self.back == self.front:
            raise Exception("The queue is empty")
        else:
            output = self.holder[self.front]
            self.holder[self.front] = None
            self.front = (self.front + 1) % len(self.holder)
            return output


class ListStack:

    def __init__(self, size: int):
        # initializing an array of Nones of fixed size
        self.holder = [None] * size
        self.top = -1

    def pop(self) -> int:
        if self.top < 0:
            raise ValueError("The stack is empty")
        else:
            output = self.holder[self.top]
            self.holder[self.top] = None
            self.top = self.top - 1
            return output

    def push(self, value: int):
        if self.top >= len(self.holder) - 1:
            raise ValueError("The stack is full")
        else:
            self.top = self.top + 1
            self.holder[self.top] = value


if __name__ == "__main__":

    l_stack = ListStack(5)
    """
    l_stack.push(5)
    print(l_stack.pop())
    try:
        print(l_stack.pop())
    except Exception as e:
        print(e)

    l_stack.push(1)
    l_stack.push(12)
    l_stack.push(33)
    l_stack.push(198)
    l_stack.push(134)

    try:
        print(l_stack.push(205))
    except Exception as e:
        print(e)
    """

    l_q = ListCircularQueue(5)

    try:
        for i in range(5):
            l_q.enqueue(i)
    except Exception as e:
        print(e)

    print(l_q)

    try:
        for i in range(2):
            print(l_q.dequeue())
    except Exception as e:
        print(e)

    print(l_q)

    try:
        for i in range(5, 10):
            l_q.enqueue(i)
    except Exception as e:
        print(e)

    print(l_q)
