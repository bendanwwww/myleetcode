"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3
 
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
   3    3

进阶：
你可以运用递归和迭代两种方法解决这个问题吗？

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        queue = []
        res = True
        if root is None:
            return True
        queue.append(root)
        while len(queue) > 0:
            compare = []
            tmpQueue = []
            while len(queue) > 0:
                node = queue[0]
                del queue[0]
                if node.left is not None:
                    tmpQueue.append(node.left)
                    compare.append(node.left.val)
                else:
                    compare.append("None")
                if node.right is not None:
                    tmpQueue.append(node.right)
                    compare.append(node.right.val)
                else:
                    compare.append("None")
            if len(compare) > 0:
                index1 = 0
                index2 = len(compare) - 1
                while index1 < index2:
                    if compare[index1] != compare[index2]:
                        return False
                    index1+= 1
                    index2-= 1
            queue = tmpQueue
        return res

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
res = s.isSymmetric(root)
print(res)