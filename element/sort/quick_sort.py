"""
快速排序

"""

class Solution(object):
    def sort(self, nums):
        self.localSort(nums, 0, len(nums) - 1)

    def localSort(self, nums, f, l):
        if f >= l:
            return
        middle = nums[f]
        i = f
        j = l
        b = 0
        while i < j:
            if b == 0:
                if nums[j] >= middle:
                    j-= 1
                else:
                    nums[i] = nums[j]
                    b = 1
            else:
                if nums[i] <= middle:
                    i+= 1
                else:
                    nums[j] = nums[i]
                    b = 0
        nums[i] = middle
        self.localSort(nums, f, i)
        self.localSort(nums, i + 1, l)

s = Solution()
nums = [30, 40, 60, 10, 20, 50, 0]
s.sort(nums)
print(nums)