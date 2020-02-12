"""
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:
输入: [1,3,4,2,2]
输出: 2

示例 2:
输入: [3,1,3,4,2]
输出: 3

说明：
1.不能更改原数组（假设数组是只读的）。
2.只能使用额外的 O(1) 的空间。
3.时间复杂度小于 O(n2) 。
4.数组中只有一个重复的数字，但它可能不止重复出现一次。

"""

class Solution(object):
    def findDuplicate(self, nums):
        # 此方法改变了原数组
        # index = 0
        # while index < len(nums):
        #     while nums[index] - 1 != index:
        #         if nums[index] == nums[nums[index] - 1]:
        #             return nums[index]
        #         tmp = nums[nums[index] - 1]
        #         nums[nums[index] - 1] = nums[index]
        #         nums[index] = tmp
        #     index+= 1
        # return 0

        # 快慢指针
        fastIndex = nums[nums[0]]
        slowIndex = nums[0]
        while fastIndex != slowIndex:
            fastIndex = nums[nums[fastIndex]]
            slowIndex = nums[slowIndex]

        index1 = 0
        index2 = fastIndex
        while index1 != index2:
            index1 = nums[index1]
            index2 = nums[index2]

        return index1

s = Solution()
res = s.findDuplicate([1, 2, 4, 2, 2])
print(res)