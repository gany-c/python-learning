from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._recursive_insert(self.root, value)

    def _recursive_insert(self, current_node, value):
        if value <= current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self._recursive_insert(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self._recursive_insert(current_node.right, value)

    def preorder_traversal(self, node):

        if node is None:
            return
        else:
            print(node.value)
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def inorder_traversal(self, node):

        if node is None:
            return
        else:
            self.inorder_traversal(node.left)
            print(node.value)
            self.inorder_traversal(node.right)

    def print_levels(self):

        if self.root is None:
            return

        node_queue = deque([self.root])
        next_queue = deque()

        while node_queue:

            node = node_queue.popleft()
            print(node.value, end=' ')

            if node.left:
                next_queue.append(node.left)

            if node.right:
                next_queue.append(node.right)

            if len(node_queue) == 0:
                print()
                node_queue = next_queue
                next_queue = deque()


if __name__ == "__main__":

    tree = BinaryTree()
    values = [14, 13, 1, 2, 3, 5, 100]

    for i in values:
        tree.insert(i)

    tree.inorder_traversal(tree.root)
    print("Pre-order")
    tree.preorder_traversal(tree.root)
    print("printing levels")
    tree.print_levels()
