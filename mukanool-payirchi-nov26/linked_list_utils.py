class ListNode:
    def __init__(self, inp: int):
        self.val = inp
        self.next = None


def detect_loops(head: ListNode) -> bool:

    if not head:
        return False

    runner = head
    walker = head

    while runner:

        runner = runner.next
        if not runner:
            return False
        else:
            if runner == walker:
                return True

        # exact same block
        runner = runner.next
        if not runner:
            return False
        else:
            if runner == walker:
                return True

        # walker steps once for every 2 steps of the runner
        walker = walker.next


def insert_at_pos(head: ListNode, insert_node: ListNode, position: int) -> ListNode:
    """
    Mistake made: Got confused between syncing the pointer incrementation and index incrementation.
    Write down the parameter description and examples and then start coding



    :param head: Head of the list, it can be none i.e. an empty list
    :param insert_node: this will always be a valid node
    :param position: this will be index of the node after insertion, index starts at 0, canot be negative
    :return: new head.
    """

    # new head if we insert at position 0
    if position == 0:
        insert_node.next = head
        head = insert_node
        return head
    else:
        # if the list is empty, we can only insert at position 0
        if not head:
            raise ValueError("We can only insert at position 0 in an empty list")
        else:
            curr = head

            i = 0
            pred_index = position - 1

            while curr and i < pred_index:
                curr = curr.next
                i = i + 1
            # while we exit, i will be at pred_index - if the list didn't run out
            # so, if the requested position is 1, pred_index will 0. So, no increment is necessary
            # we insert after node 0 and before old node1

            if curr:
                insert_node.next = curr.next
                curr.next = insert_node
                return head
            else:
                raise ValueError("Number of nodes in the list is not enough")



