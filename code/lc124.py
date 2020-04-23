"""
给定一个非空二叉树，返回其最大路径和。
本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:
输入: [1,2,3]
       1
      / \
     2   3
输出: 6

示例 2:
输入: [-10,9,20,null,null,15,7]
   -10
   / \
  9  20
    /  \
   15   7
输出: 42

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys

class Solution(object):

    max = -sys.maxsize

    def maxPathSum(self, root):
        if root is None:
            return 0
        self.dfs(root)
        return self.max

    def dfs(self, node):
        if node is None:
            return 0
        maxLeft = max(0, self.dfs(node.left))
        maxRight = max(0, self.dfs(node.right))
        self.max = max(self.max, node.val + maxLeft + maxRight)
        return max(node.val + maxLeft, node.val + maxRight)

s = Solution()
root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.right.left.left = TreeNode(1)
root.right.left.right = TreeNode(-5)
res = s.maxPathSum(root)
print(res)