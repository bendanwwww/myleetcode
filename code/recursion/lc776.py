

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def splitBST(self, root, V):
      return self.find(root, V)

    def find(self, node, V):
      if root == None:
        return [[None], [None]]
      

s = Solution()
head = TreeNode(4)
head.left = TreeNode(2)
head.right = TreeNode(6)
head.left.left = TreeNode(1)
head.left.right = TreeNode(3)
head.right.left = TreeNode(5)
head.right.right = TreeNode(7)
s.splitBST(head, 2)