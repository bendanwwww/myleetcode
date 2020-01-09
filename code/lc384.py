"""
打乱一个没有重复元素的数组。

示例:
// 以数字集合 1, 2 和 3 初始化数组。
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
solution.shuffle();

// 重设数组到它的初始状态[1,2,3]。
solution.reset();

// 随机返回数组[1,2,3]打乱后的结果。
solution.shuffle();

"""

import copy as cp
import random

class Solution(object):

    numShuffle = []
    numsReset = []

    def __init__(self, nums):
        global numsReset
        global numShuffle
        numsReset = cp.copy(nums)
        numShuffle = cp.copy(nums)

    def reset(self):
        return numsReset

    def shuffle(self):
        nums = cp.copy(numsReset)
        for i in range(len(nums)):
            state = random.randint(i, len(nums) - 1)
            tmp = nums[i]
            nums[i] = nums[state]
            nums[state] = tmp
        return nums

s = Solution([1, 2, 3])
res1 = s.reset()
res2 = s.shuffle()
print(res1)
print(res2)