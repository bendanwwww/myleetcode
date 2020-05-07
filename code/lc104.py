"""
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，
    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        queue = []
        maxDepth = 0
        if root is None:
            return 0
        queue.append([root, 1])
        while len(queue) > 0:
            node = queue[0][0]
            depth = queue[0][1]
            maxDepth = max(depth, maxDepth)
            del queue[0]
            if node.left is not None:
                queue.append([node.left, depth + 1])
            if node.right is not None:
                queue.append([node.right, depth + 1])
        return maxDepth

s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
res = s.maxDepth(root)
print(res)