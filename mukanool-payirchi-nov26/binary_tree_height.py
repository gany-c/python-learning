class TreeNode:
    def __init__(self, val:int):
        self._val = val
        self.left = None
        self.right = None


def find_height(head: TreeNode) -> int:

    if head:
        return 1 + max(find_height(head.left), find_height(head.right))
    else:
        return 0



