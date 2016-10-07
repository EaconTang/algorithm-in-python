# -*- coding: utf-8 -*-
"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
from DataStruct.BinTreeNode import BinTreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1


if __name__ == '__main__':
    a = BinTreeNode('A')
    b = BinTreeNode('B')
    c = BinTreeNode('C')
    d = BinTreeNode('D')
    a.left = b
    b.left = c
    # c.left = d
    print Solution().maxDepth(a)