"""
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:
输入: [10,9,2,5,3,7,101,18]
输出: 4

解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

说明:
可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。

进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

"""

class Solution(object):
    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        dp[len(nums) - 1] = 1
        max = 1
        for i in range(len(nums) - 2, -1, -1):
            for x in range(i + 1, len(nums)):
                if nums[x] > nums[i]:
                    tmp = dp[x] + 1
                    if tmp > dp[i]:
                        dp[i] = tmp
            if dp[i] > max:
                max = dp[i]
        return max

s = Solution()
res = s.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6])
print(res)