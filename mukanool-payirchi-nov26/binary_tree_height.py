class TreeNode:
    def __init__(self, val:int):
        self.val = val
        self.left = None
        self.right = None


def find_height(head: TreeNode) -> int:

    if head:
        return 1 + max(find_height(head.left), find_height(head.right))
    else:
        return 0


def insert_bst(head: TreeNode, node: TreeNode):

    if not head:
        return
    else:
        if node.val <= head.val:
            if head.left:
                insert_bst(head.left, node)
            else:
                head.left = node
        else:
            if head.right:
                insert_bst(head.right, node)
            else:
                head.right = node



