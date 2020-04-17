"""
给定一个未排序的整数数组，找出最长连续序列的长度。
要求算法的时间复杂度为 O(n)。

示例:
输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

"""

class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0
        res = []
        numMap = {}
        numListMap = {}
        for i in nums:
            numMap[i] = 0
        for i in nums:
            if numMap[i] == 1:
                continue
            tmpList = [i]
            numMap[i] = 1
            x = i + 1
            while x in numMap:
                if x in numListMap:
                    tmpList = tmpList + numListMap[x]
                    del numListMap[x]
                    break
                tmpList.append(x)
                numMap[x] = 1
                x+= 1
            numListMap[i] = tmpList
            if len(tmpList) > len(res):
                res = tmpList
        return len(res)

s = Solution()
res = s.longestConsecutive([100, 4, 200, 1, 3, 2])
print(res)
