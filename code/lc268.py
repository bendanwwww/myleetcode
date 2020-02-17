"""
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

示例 1:
输入: [3,0,1]
输出: 2

示例 2:
输入: [9,6,4,2,3,5,7,0,1]
输出: 8

说明:
你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?

"""

class Solution(object):
    def missingNumber(self, nums):
        nums.append(-1)
        nullIndex = len(nums) - 1
        for i in range(len(nums)):
            while nums[i] != i and nums[i] != -1:
                tmp = nums[nums[i]]
                if tmp == -1:
                    nums[nums[i]] = nums[i]
                    nums[i] = -1
                    nullIndex = i
                else:
                    nums[nums[i]] = nums[i]
                    nums[i] = tmp
        return nullIndex

s = Solution()
res = s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])
print(res)