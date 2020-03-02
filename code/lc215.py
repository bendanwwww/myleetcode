"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

说明:
你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

"""

class Solution(object):

    res = 0

    def findKthLargest(self, nums, k):
        if len(nums) == 1:
            return nums[0]
        self.localFind(nums, k, 0, len(nums) - 1)
        return self.res

    def localFind(self, nums, k, f, l):
        if f >= l:
            return
        middle = nums[f]
        i = f
        j = l
        b = 0
        while i < j:
            if b == 0:
                if nums[j] >= middle:
                    j -= 1
                else:
                    nums[i] = nums[j]
                    b = 1
            else:
                if nums[i] <= middle:
                    i += 1
                else:
                    nums[j] = nums[i]
                    b = 0
        nums[i] = middle
        if len(nums) - i == k:
            self.res = nums[i]
            return
        if len(nums) - i < k:
            self.localFind(nums, k, f, i)
        if len(nums) - i > k:
            self.localFind(nums, k, i + 1, l)
        self.res = nums[len(nums) - k]

s = Solution()
res = s.findKthLargest([99, 99], 1)
print(res)
