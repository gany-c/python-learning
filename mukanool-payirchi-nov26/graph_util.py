# upskill: had to looks this import up
from collections import deque


class GraphNode:
    def __init__(self, val: int):
        self.val = val
        self.connections = []


class GraphWrapper:
    def __init__(self, node: GraphNode, rank: int):
        self.node = node
        self.rank = rank


def find_distance(start: GraphNode, target: GraphNode) -> int:
    """
    Small design philosophy variation to prevent re-processing nodes:

    visited vs queue_added.
    A queue_added node is still processed, but not again added into the queue.
    You were thinking of visited = processed, don't even process it again

    This distinction relevant in the context of a single node having several ancestors,
    especially in the same level.
    
    :param start:
    :param target:
    :return:
    """

    # mistake: queue_added = {}, creates a dict
    queue_added = set()
    queue = deque()

    wrapped_start = GraphWrapper(start, 0)
    queue.append(wrapped_start)
    queue_added.add(start)

    # upskill: correct, but had to verify
    while queue:
        # api mistake => wrapper = queue.pop()
        # pop is lifo, looks like dequeue supports both stack and queue
        wrapper = queue.popleft()

        if wrapper.node == target:
            return wrapper.rank
        else:
            for child in wrapper.node.connections:
                if child not in queue_added:
                    queue.append(GraphWrapper(child, wrapper.rank + 1))
                    # api mistake => queue_added.append(wrapper.node)
                    queue_added.add(child)

    # unable to reach target
    return -1




