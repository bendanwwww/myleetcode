"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:
给定有序数组: [-10,-3,0,5,9],
一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
      0
     / \
   -3   9
   /   /
 -10  5

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        mid = int(len(nums) / 2)
        root = TreeNode(nums[mid])
        self.put(root, nums, 0, mid - 1, mid + 1, len(nums) - 1)
        return root

    def put(self, node, nums, left1, left2, right1, right2):
        if left1 <= left2:
            leftMid = int((left1 + left2) / 2)
            node.left = TreeNode(nums[leftMid])
            self.put(node.left, nums, left1, leftMid - 1, leftMid + 1, left2)
        if right1 <= right2:
            rightMid = int((right1 + right2) / 2)
            node.right = TreeNode(nums[rightMid])
            self.put(node.right, nums, right1, rightMid - 1, rightMid + 1, right2)

s = Solution()
res = s.sortedArrayToBST([-10, -3, 0, 5, 9])
print(res)