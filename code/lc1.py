"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

"""

class Solution(object):
    def twoSum(self, nums, target):
        res = []
        dictMap = {}
        for i in range(len(nums)):
            if nums[i] in dictMap:
                dictMap[nums[i]].append(i)
            else:
                dictMap[nums[i]] = [i]

        for i in range(len(nums)):
            if target - nums[i] in dictMap:
                if target - nums[i] != nums[i]:
                    return [dictMap[nums[i]][0], dictMap[target - nums[i]][0]]
                elif len(dictMap[target - nums[i]]) == 2:
                    return dictMap[target - nums[i]]
        return res

s = Solution()
res = s.twoSum([3, 2, 4], 6)
print(res)