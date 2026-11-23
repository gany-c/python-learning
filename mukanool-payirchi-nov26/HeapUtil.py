
class MinHeap:
    """
    A min heap is a binary tree where each node has a lower value than either of its children.
    It is implemented as an array, where if a node is at i, the children are at 2i + 1 and 2i + 2
    """
    def __init__(self, size):
        self.store = []
        self.size = size
        # crucial mistake - last index will be at 0 in an empty queue
        self.last_index = -1

    def _correct_down(self, index):

        left_index = 2 * index + 1
        if left_index > self.last_index:
            return

        if self.store[left_index] < self.store[index]:
            temp = self.store[left_index]
            self.store[left_index] = self.store[index]
            self.store[index] = temp
            self._correct_down(left_index)

        right_index = 2 * index + 2
        if right_index <= self.last_index:
            if self.store[right_index] < self.store[index]:
                temp = self.store[right_index]
                self.store[right_index] = self.store[index]
                self.store[index] = temp
                self._correct_down(right_index)

    def dequeue(self) -> int:
        """
        We return the lowest element, i.e. the top most element
        1. save the top most element
        2. replace it by the last element, update last index
        3. correct the heap property from top to the new end
        4. return the saved output
        :return:
        """

        # same mistake here - last_index should be at -1 while empty, not 0
        if not self.store or self.last_index == -1:
            return None

        output: int = self.store[0]
        self.store[0] = self.store[self.last_index]
        # mistake made, pop is necessary, otherwise the older elements are retained
        self.store.pop()
        self.last_index = self.last_index - 1
        self._correct_down(0)
        return output

    def _bubble_up(self):

        i = self.last_index
        while i > 0:
            parent = (i - 1)//2
            if self.store[parent] > self.store[i]:
                # mistake: bugs in swapping
                temp = self.store[parent]
                self.store[parent] = self.store[i]
                self.store[i] = temp
            i = i - 1
            # mistake: forgot this step

    def enqueue(self, elem: int):
        """
        1. Add a node to the end of the array
        2. update the last elem index
        3. Bubble up the heap property
        :param elem:
        :return:
        """

        if self.last_index >= self.size - 1:
            return

        self.store.append(elem)
        self.last_index = self.last_index + 1
        self._bubble_up()
        print(self.store)


if __name__ == "__main__":

    heap = MinHeap(5)
    heap.enqueue(3)
    heap.enqueue(2)
    print(heap.dequeue())
    print(heap.dequeue())
    print(heap.dequeue())
    heap.enqueue(33)
    heap.enqueue(44)
    heap.enqueue(51)
    heap.enqueue(19)
    # at this point the heap is not necessarily in ascending order
    print(heap.dequeue())
    print(heap.dequeue())
    print(heap.dequeue())
    print(heap.dequeue())
    # but the dequeue order will be ascending

