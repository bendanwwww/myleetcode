"""
归并排序

"""

class Solution(object):
    def sort(self, nums):
        self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, first, end):
        if first == end:
            return
        mid = int((first + end) / 2)
        self.mergeSort(nums, first, mid)
        self.mergeSort(nums, mid + 1, end)

        self.merge(nums, first, mid, end)

    def merge(self, nums, first, mid, end):
        tmp = []
        i = first
        x = mid + 1
        while i <= mid and x <= end:
            if nums[i] < nums[x]:
                tmp.append(nums[i])
                i+= 1
            else:
                tmp.append(nums[x])
                x+= 1
        while i <= mid:
            tmp.append(nums[i])
            i += 1
        while x <= end:
            tmp.append(nums[x])
            x += 1

        n = 0
        for z in range(first, end + 1):
            nums[z] = tmp[n]
            n+= 1

s = Solution()
nums = [1, 9, 5, 3, 7, 8]
s.sort(nums)
print(nums)