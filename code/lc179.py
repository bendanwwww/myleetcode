"""
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:
输入: [10,2]
输出: 210

示例 2:
输入: [3,30,34,5,9]
输出: 9534330

说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。

"""

class Solution(object):
    def largestNumber(self, nums):
        res = ''
        for i in range(len(nums)):
            for x in range(i + 1, len(nums)):
                if self.compare(str(nums[i]), str(nums[x])):
                    tmp = nums[i]
                    nums[i] = nums[x]
                    nums[x] = tmp
        if nums[len(nums) - 1] == 0:
            return "0"
        for i in range(len(nums) - 1, -1, -1):
            res+= str(nums[i])
        return res

    def compare(self, a, b):
        if int(a + b) > int(b + a):
            return True
        else:
            return False

s = Solution()
res = s.largestNumber([12, 121])
print(res)