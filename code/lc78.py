"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。

示例:
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""

class Solution(object):
    def subsets(self, nums):
        res = []
        for i in range(2 ** len(nums), 2 ** (len(nums) + 1)):
            binStr = bin(i)[3:]
            tmpRes = []
            for ci in range(len(binStr)):
                if binStr[ci] == '1':
                    tmpRes.append(nums[ci])
            res.append(tmpRes)
        return res

s = Solution()
res = s.subsets([1, 2, 3])
print(res)