
class MyStack:
    def __init__(self, capacity: int):
        self._size = capacity
        self._store = []

    def push(self, elem: int):
        if len(self._store) >= self._size:
            raise MemoryError("Stack Full")
        else:
            self._store.append(elem)

    def pop(self) -> int:
        if len(self._store) <= 0:
            raise MemoryError("Stack Empty")
        else:
            return self._store.pop()

    def peek(self) -> int:
        if len(self._store) <= 0:
            raise MemoryError("Stack Empty")
        else:
            return self._store[-1]

    # mistake made: tried using len on the
    # custom object
    def get_size(self) -> int:
        return len(self._store)


class MyQueue:
    def __init__(self, capacity: int):
        # even in the worst case the capacity is honored
        # if the insert order is undisturbed by retrieval
        # the queue can store twice as much
        self._size = capacity
        self._insert_stack = MyStack(capacity)
        self._retrieve_stack = MyStack(capacity)

    def _transfer(self):

        if self._retrieve_stack.get_size() > 0:
            raise ValueError("Cannot transfer")
        else:
            while self._insert_stack.get_size() > 0:
                self._retrieve_stack.push(self._insert_stack.pop())

    def enqueue(self, elem: int):

        if self._insert_stack.get_size() < self._size:
            self._insert_stack.push(elem)
        else:
            if self._retrieve_stack.get_size() == 0:
                self._transfer()
                self._insert_stack.push(elem)
            else:
                print("Cannot insert")

    def dequeue(self) -> int:

        if self._retrieve_stack.get_size() > 0:
            return self._retrieve_stack.pop()
        else:
            if self._insert_stack.get_size() > 0:
                self._transfer()
                return self._retrieve_stack.pop()
            else:
                return None


if __name__ == "__main__":
    queue_1 = MyQueue(5)
    queue_1.enqueue(2)
    queue_1.enqueue(5)
    print(queue_1.dequeue())
    print(queue_1.dequeue())
    print(queue_1.dequeue())
    queue_1.enqueue(20)
    queue_1.enqueue(30)
    queue_1.enqueue(40)
    queue_1.enqueue(50)
    queue_1.enqueue(60)
    queue_1.enqueue(25)
    queue_1.enqueue(35)
    queue_1.enqueue(45)
    queue_1.enqueue(55)
    queue_1.enqueue(65)

    for i in range(0, 10):
        print(queue_1.dequeue())
