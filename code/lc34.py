"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

"""

import sys

class Solution(object):
    def searchRange(self, nums, target):
        # res = [-1, -1]
        # for i in range(len(nums)):
        #     if nums[i] > target:
        #         break
        #     if nums[i] == target:
        #         if res[0] == -1:
        #             res[0] = i
        #         else:
        #             res[1] = i
        # if res[0] != -1 and res[1] == -1:
        #     res[1] = res[0]
        # return res
        res = [-1, -1]
        left = 0
        right = len(nums) - 1
        b = False
        while True:
            if left > right:
                break
            if left == right and nums[left] != target:
                break
            if nums[left] > target or nums[right] < target:
                break
            midIndex = int((left + right) / 2)
            if nums[midIndex] == target:
                b = True
                break
            if nums[midIndex] > target:
                right = midIndex - 1
                continue
            if nums[midIndex] < target:
                left = midIndex + 1
                continue
        if b:
            for i in range(midIndex, -1, -1):
                if nums[i] == target:
                    res[0] = i
                else:
                    break
            for i in range(midIndex, len(nums)):
                if nums[i] == target:
                    res[1] = i
                else:
                    break
        return res

s = Solution()
res = s.searchRange([5, 7, 7, 8, 8, 10], 6)
print(res)