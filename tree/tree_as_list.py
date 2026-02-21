#!/bin/python3

"""
Height of Binary Search Tree
Given the root of a binary search tree, return the height of the tree. Height is the number of nodes along the longest path from root to leaf.

Example

Input

n = 7
values = [4, 2, 6, 1, 3, 5, 7]
leftChild = [1, 3, 5, -1, -1, -1, -1]
rightChild = [2, 4, 6, -1, -1, -1, -1]
Output

3
Explanation

The tree is perfectly balanced with three levels:
- Level 1: Node 4 (root)
- Level 2: Nodes 2 and 6
- Level 3: Leaves 1, 3, 5, 7 The longest path from root to any leaf has 3 nodes, so the height is 3.

"""



#
# Complete the 'getBinarySearchTreeHeight' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY leftChild
#  3. INTEGER_ARRAY rightChild
#

def getHeight(values, leftChild, rightChild, index):

    left_height = 0
    right_height = 0

    if leftChild[index] >= 0:
        left_height = getHeight(values, leftChild, rightChild, leftChild[index])

    if rightChild[index] >= 0:
        right_height = getHeight(values, leftChild, rightChild, rightChild[index])

    return max(left_height, right_height) + 1

def getBinarySearchTreeHeight(values, leftChild, rightChild):
    # Write your code here
    if not values or not leftChild or not rightChild:
        return 0
    else:
        return getHeight(values, leftChild, rightChild, 0)


if __name__ == '__main__':

    values = [4, 2, 6, 1, 3, 5, 7]
    leftChild = [1, 3, 5, -1, -1, -1, -1]
    rightChild = [2, 4, 6, -1, -1, -1, -1]

    print(getBinarySearchTreeHeight(values, leftChild, rightChild))
