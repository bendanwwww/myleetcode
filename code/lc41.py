"""
给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。

示例 1:
输入: [1,2,0]
输出: 3

示例 2:
输入: [3,4,-1,1]
输出: 2

示例 3:
输入: [7,8,9,11,12]
输出: 1

"""

class Solution(object):
    def firstMissingPositive(self, nums):
        res = 1
        findMap = {}
        for i in nums:
            findMap[i] = 1
            while res in findMap:
                res+= 1
            if i + 1 > 0 and i + 1 not in findMap:
                res = min(i + 1, res)
        return res

s = Solution()
res = s.firstMissingPositive([3, 4, -1, 1])
print(res)