"""
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：
[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root):
        queue = []
        res = []
        if root is None:
            return []
        queue.append(root)
        res.append([root.val])
        state = 0
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
                if state == 0:
                    for i in range(len(tmpQueue) - 1, -1, -1):
                        tmpRes.append(tmpQueue[i].val)
                    state = 1
                else:
                    for i in range(len(tmpQueue)):
                        tmpRes.append(tmpQueue[i].val)
                    state = 0
                res.append(tmpRes)
            queue = tmpQueue
        return res

s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
res = s.zigzagLevelOrder(root)
print(res)