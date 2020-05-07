"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：
[
  [3],
  [9,20],
  [15,7]
]

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        queue = []
        res = []
        if root is None:
            return []
        queue.append(root)
        res.append([root.val])
        while len(queue) > 0:
            tmpQueue = []
            while len(queue) > 0:
                node = queue[0]
                del queue[0]
                if node.left is not None:
                    tmpQueue.append(node.left)
                if node.right is not None:
                    tmpQueue.append(node.right)
            if len(tmpQueue) > 0:
                tmpRes = []
                for i in range(len(tmpQueue)):
                    tmpRes.append(tmpQueue[i].val)
                res.append(tmpRes)
            queue = tmpQueue
        return res

s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
res = s.levelOrder(root)
print(res)