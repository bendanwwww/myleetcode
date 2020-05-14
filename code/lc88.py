"""
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

说明:
初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
 

示例:
输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
输出: [1,2,2,3,5,6]

"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        tmp1 = nums1[:]
        index1 = 0
        indexTmp = 0
        index2 = 0
        while indexTmp < m or index2 < n:
            if indexTmp == m:
                nums1[index1] = nums2[index2]
                index2+= 1
                index1+= 1
                continue
            if index2 == n:
                nums1[index1] = tmp1[indexTmp]
                indexTmp+= 1
                index1+= 1
                continue
            if nums2[index2] <= tmp1[indexTmp]:
                nums1[index1] = nums2[index2]
                index2+= 1
            else:
                nums1[index1] = tmp1[indexTmp]
                indexTmp+= 1
            index1+= 1

s = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
s.merge(nums1, 3, nums2, 3)
print(nums1)