# -*- coding: utf-8 -*-
"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]

"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, _sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        def inorder_traverse(node, path, __sum):
            assert isinstance(path, list)
            if node is None or node.val is None:
                return
            path.append(node.val)
            if node.val == __sum and node.left == node.right == None:
                res.append(path)
                return
            if node.left:
                inorder_traverse(node.left, path, __sum - node.val)
            if node.right:
                inorder_traverse(node.right, path, __sum - node.val)
        inorder_traverse(root, [], _sum)
        return res