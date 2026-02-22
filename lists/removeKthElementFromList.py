"""
One-Pass Removal of k-th Node from End
Given the head of a singly linked list and an integer k, remove the k-th node from the end in one traversal and return the new head. If k is invalid, return the original list.

Example

Input

head = [5, 6, 7, 8]
k = 3
Output

[6, 7, 8]
Explanation

The list has 4 nodes.
The k-th node from the end with k=3 is the 4th node from the end (value 5), which is the head. Removing it yields [6,7,8].
Input Format

The first line contains an integer n denoting the length of linked list.
The next n lines contains elements of the linked list.
The last line contains k.
Example

4
5
6
7
8
3
here 4 is the length of the linked list, followed by the elements of the list and value of k.

Constraints

0 <= number of nodes in head <= 1000
-10^9 <= value of each node <= 10^9
0 <= k <= 10^9
Output Format

Return the head of the modified linked list after removal.
Sample Input 0

1
5
1
Sample Output 0

5
"""

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')

        node = node.next

        if node:
            print(sep, end='')


def removeKthNodeFromEnd(head, k):
    # Write your code here

    # lol, K starts at 0
    k = k + 1

    if head is None:
        return head

    scout = head
    i = 1
    while scout.next is not None and i < k:
        scout = scout.next
        i = i + 1

    # insufficient elements in the list
    if i < k:
        return head

    # the list comprises of exactly K elements
    if scout.next is None:
        head = head.next
        return head

    # what follows prev will be deleted
    prev = head
    scout = scout.next

    # move scout to the last element, prev follows at a distance
    while scout.next is not None:
        scout = scout.next
        prev = prev.next

    # delete the node following prev
    tobedeleted = prev.next
    prev.next = tobedeleted.next

    return head


