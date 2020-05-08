"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。
假设一个二叉搜索树具有如下特征：
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

示例 1:
输入:
    2
   / \
  1   3
输出: true

示例 2:
输入:
    10
   / \
  5   15
     / \
    6   20
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    mid = []

    def isValidBST(self, root):
        self.mid = []
        if root is None:
            return True
        self.find(root)
        for i in range(1, len(self.mid)):
            if self.mid[i] <= self.mid[i - 1]:
                return False
        return True

    def find(self, node):
        if node is None:
            return
        self.find(node.left)
        self.mid.append(node.val)
        self.find(node.right)

s = Solution()
# [10,5,15,null,null,6,20]
root = TreeNode(0)
# root.left = TreeNode(5)
# root.right = TreeNode(15)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(20)
res = s.isValidBST(root)
print(res)