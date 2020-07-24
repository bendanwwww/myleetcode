"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""

class Solution(object):
    def threeSum(self, nums):
        res = []
        if len(nums) == 0:
            return res
        nums.sort()

        for f in range(len(nums)):
            if nums[f] > 0:
                break
            if f > 0 and nums[f] == nums[f - 1]:
                continue

            t = len(nums) - 1
            for s in range(f + 1, len(nums)):
                if s > f + 1 and nums[s] == nums[s - 1]:
                    continue
                sum = nums[f] + nums[s]
                while s < t and sum + nums[t] > 0:
                    t-= 1
                if s == t:
                    break
                if sum + nums[t] == 0:
                    res.append([nums[f], nums[s], nums[t]])
        return res


s = Solution()
res = s.threeSum([0, 0, 0, 0])
print(res)