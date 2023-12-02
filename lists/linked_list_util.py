class ListNode:

    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node

    def set_next(self, next_node):
        self.next_node = next_node

    def get_next(self):
        return self.next_node

    def __str__(self):
        return str(self.value)


class ListUtil:

    @staticmethod
    def create_list(in_array):

        if in_array is None:
            raise ValueError("Invalid input array")

        head = ListNode(None, None)
        end = head

        for val in in_array:
            node = ListNode(val, None)
            end.set_next(node)
            end = node

        return head

    @staticmethod
    def display_list(head: ListNode):

        if head is None:
            raise ValueError("Invalid Head")

        temp = head.get_next()

        while temp is not None:
            # Python, printing in same line.
            print(temp.value, end=", ")
            temp = temp.get_next()

        print()

    @staticmethod
    def add_to_list(head: ListNode, val: int):

        if head is None:
            raise ValueError("invalid head node")

        temp = head

        while temp.get_next() is not None:
            temp = temp.get_next()

        new_node = ListNode(val, None)
        temp.set_next(new_node)


    @staticmethod
    def delete_from_list(head: ListNode, val: int):

        if head is None:
            raise ValueError("invalid head node")

        prev = head
        temp = prev.get_next()

        if temp is None:
            # print("List is empty")
            return

        while temp is not None and temp.value != val:
            temp = temp.get_next()
            prev = prev.get_next()

        if temp is None:
            print("Value not found, nothing to delete")
        else:
            prev.set_next(temp.get_next())
            print("Deleted node", temp.value)


    @staticmethod
    def insert_into_sorted_list(head: ListNode, insert_node: ListNode):

        if head is None:
            raise ValueError("Invalid head provided")

        prev = head
        temp = prev.get_next()

        # print(f"new_node = {insert_node}")

        while temp is not None and temp.value <= insert_node.value:
            temp = temp.get_next()
            prev = prev.get_next()

        prev.set_next(insert_node)
        insert_node.set_next(temp)


    @staticmethod
    def sort_linked_list(head: ListNode):

        if head is None or head.get_next() is None:
            return head

        sorted_head = ListNode(None, None)
        temp = head.get_next()

        while temp is not None:
            # saving the future node
            look_ahead = temp.get_next()
            # print("Look ahead node = ", look_ahead)

            # inserting into sorted list
            ListUtil.insert_into_sorted_list(sorted_head, temp)

            # set temp to future_node
            temp = look_ahead

        head.set_next(sorted_head.get_next())


if __name__ == "__main__":
    list_head = ListUtil.create_list([1, 2, 3, 4, 5, 6])
    # ListUtil.display_list(list_head)

    ListUtil.add_to_list(list_head, 22)
    ListUtil.display_list(list_head)

    ListUtil.delete_from_list(list_head, 100)
    ListUtil.delete_from_list(list_head, 3)

    ListUtil.display_list(list_head)

    print("======== Testing the sorted numbers ========")

    second_list = ListUtil.create_list([34, 345, 730, 46, 23, 4658, 5, 7, 9, 2, 1])
    print(" The random list = ")
    ListUtil.display_list(second_list)
    print(" Sorting the list")
    ListUtil.sort_linked_list(second_list)
    print(" The sorted list = ")
    ListUtil.display_list(second_list)
