"""
给定一个无序的数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。

示例 1:
输入: nums = [1, 5, 1, 1, 6, 4]
输出: 一个可能的答案是 [1, 4, 1, 5, 1, 6]

示例 2:
输入: nums = [1, 3, 2, 2, 3, 1]
输出: 一个可能的答案是 [2, 3, 1, 3, 1, 2]

说明:
你可以假设所有输入都会得到有效的结果。

进阶:
你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？

"""

import heapq
import numpy as np

class Solution(object):
    def wiggleSort(self, nums):
        # heap find mid-number
        #midNumber = 0
        # numsHeap = []
        # heapSize = int((len(nums) + 1) / 2)
        # for i in range(heapSize):
        #     heapq.heappush(numsHeap, nums[i])
        # for i in range(heapSize, len(nums)):
        #     if heapq.nsmallest(1, numsHeap)[0] < nums[i]:
        #         heapq.heappop(numsHeap)
        #         heapq.heappush(numsHeap, nums[i])
        # midNumber = heapq.nsmallest(1, numsHeap)[0]

        midNumber = np.median(nums)
        # three-way-partition
        i = 0
        j = 0
        n = len(nums) - 1
        while j <= n:
            if nums[j] < midNumber:
                nums[i], nums[j] = nums[j], nums[i]
                i = i + 1
                j = j + 1
            elif nums[j] > midNumber:
                nums[j], nums[n] = nums[n], nums[j]
                n = n - 1
            else:
                j = j + 1
        # insert new nums
        midN = int((len(nums) + 1) / 2)
        first = nums[:midN]
        last = nums[midN:]
        for i in range(len(first)):
            nums[2 * i] = first[len(first) - 1 - i]
        for i in range(len(last)):
            nums[2 * i + 1] = last[len(last) - 1 - i]

s = Solution()
nums = [1, 3, 2, 2, 3, 1]
s.wiggleSort(nums)
print(nums)