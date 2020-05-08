"""
给定一个二叉树，返回它的中序 遍历。

示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3
输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        res = []
        if root is None:
            return []
        stack = []
        stack.append([root, True])
        while len(stack) > 0:
            if stack[-1][0].left is not None and stack[-1][1]:
                stack[-1][1] = False
                stack.append([stack[-1][0].left, True])
            else:
                tmpNode = stack[-1][0]
                stack.pop()
                res.append(tmpNode.val)
                if tmpNode.right is not None:
                    stack.append([tmpNode.right, True])
        return res

s = Solution()
# [10,5,15,null,null,6,20]
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)
res = s.inorderTraversal(root)
print(res)