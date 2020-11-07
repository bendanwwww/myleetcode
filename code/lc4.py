"""
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。
进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？

示例 1：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2

示例 2：
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

示例 3：
输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000

示例 4：
输入：nums1 = [], nums2 = [1]
输出：1.00000

示例 5：
输入：nums1 = [2], nums2 = []
输出：2.00000

提示：
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        size = len(nums1) + len(nums2)
        if size % 2 == 0:
            mid = int((size - 1) / 2)
            if len(nums1) == 0:
                return (nums2[mid] + nums2[mid + 1]) / 2.0
            if len(nums2) == 0:
                return (nums1[mid] + nums1[mid + 1]) / 2.0
        else:
            mid = int(size / 2)
            if len(nums1) == 0:
                return nums2[mid]
            if len(nums2) == 0:
                return nums1[mid]

        index_1 = 0
        index_2 = 0
        while index_1 + index_2 < mid:
            if index_1 == len(nums1):
                index_2+= 1
                continue
            if index_2 == len(nums2):
                index_1+= 1
                continue
            if nums1[index_1] < nums2[index_2]:
                index_1+= 1
            else:
                index_2+= 1

        if size % 2 == 0:
            if index_1 == len(nums1):
                return (nums2[index_2] + nums2[index_2 + 1]) / 2.0
            if index_2 == len(nums2):
                return (nums1[index_1] + nums1[index_1 + 1]) / 2.0
            tmp = min(nums1[index_1], nums2[index_2])
            if nums1[index_1] < nums2[index_2]:
                if index_1 + 1 == len(nums1):
                    return (tmp + nums2[index_2]) / 2.0
                else:
                    return (tmp + min(nums1[index_1 + 1], nums2[index_2])) / 2.0
            else:
                if index_2 + 1 == len(nums2):
                    return (tmp + nums1[index_1]) / 2.0
                else:
                    return (tmp + min(nums1[index_1], nums2[index_2 + 1])) / 2.0

        else:
            if index_1 == len(nums1):
                return nums2[index_2]
            if index_2 == len(nums2):
                return nums1[index_1]
            return min(nums1[index_1], nums2[index_2])

    def findMedianSortedArrays_2(self, nums1, nums2):
        size = len(nums1) + len(nums2)
        if size % 2 == 0:
            return (self.find(nums1, nums2, int(size / 2)) + self.find(nums1, nums2, int(size / 2) + 1)) / 2.0
        else:
            return self.find(nums1, nums2, int(size / 2) + 1)

    def find(self, nums1, nums2, k):
        index_1 = 0
        index_2 = 0
        while k > 1:
            if index_1 >= len(nums1):
                return nums2[index_2 + k - 1]
            if index_2 >= len(nums2):
                return nums1[index_1 + k - 1]
            i = int(k / 2) - 1
            index_1_end = min(index_1 + i, len(nums1) - 1)
            index_2_end = min(index_2 + i, len(nums2) - 1)
            if nums1[index_1_end] <= nums2[index_2_end]:
                k = k - (index_1_end - index_1 + 1)
                index_1 = index_1_end + 1
            else:
                k = k - (index_2_end - index_2 + 1)
                index_2 = index_2_end + 1
        if index_1 >= len(nums1):
            return nums2[index_2]
        if index_2 >= len(nums2):
            return nums1[index_1]
        return min(nums1[index_1], nums2[index_2])


s = Solution()
res = s.findMedianSortedArrays_2([2, 3, 4], [1])
print(res)