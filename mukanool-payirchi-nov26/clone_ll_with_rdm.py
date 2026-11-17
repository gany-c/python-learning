class ListNode:

    def __init__(self, in_val):
        self.val: int = in_val
        self.next_ptr: "ListNode|None" = None
        self.random_ptr: "ListNode|None" = None


def clone_list_with_random_ptrs(head: ListNode) -> ListNode:
    # map of linked list nodes to their index positions
    node_to_index_dict = {}
    # array of linked list nodes
    node_list = []

    curr = head
    i = 0

    while curr:
        node_to_index_dict[curr] = i
        node_list.append(curr)
        curr = curr.next_ptr
        i = i + 1

    # for each node, create a mapping of its index to where the random pointer points
    node_index_to_random_index_dict = {}

    for index, node in enumerate(node_list):
        rand_node = node.random_ptr
        if rand_node:
            # Mistake made: used the wrong dict here
            rand_node_index = node_to_index_dict[rand_node]
        else:
            # didn't take care of rand_ptr == None
            rand_node_index = -1

        node_index_to_random_index_dict[index] = rand_node_index

    out_head = None
    out_curr = None
    i = 0
    out_index_to_node_dict = {}

    # first create the linear linked list,
    # also create a mapping of index to nodes
    for index, node in enumerate(node_list):

        cloned_node = ListNode(node.val)
        if not out_head:
            out_head = cloned_node
            out_curr = cloned_node
        else:
            out_curr.next_ptr = cloned_node
            out_curr = cloned_node

        out_index_to_node_dict[i] = cloned_node
        i = i + 1

    out_curr = out_head
    i = 0
    # Set the random pointers
    while out_curr:
        random_index = node_index_to_random_index_dict[i]
        if random_index > -1:
            out_curr.random_ptr = out_index_to_node_dict[random_index]

        out_curr = out_curr.next_ptr
        i = i + 1

    return out_head
