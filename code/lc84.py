"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。

示例:
输入: [2,1,5,6,2,3]
输出: 10

"""

import sys

class Solution(object):
    def largestRectangleArea(self, heights):
        if len(heights) == 0:
            return 0
        # 此判断投机取巧。。不可取
        if min(heights) == max(heights):
            return heights[0] * len(heights)
        minHeight = sys.maxsize
        minIndex = -1
        for i in range(len(heights)):
            if heights[i] < minHeight:
                minHeight = heights[i]
                minIndex = i
        return max(minHeight * len(heights), self.find(0, minIndex - 1, heights, 0), self.find(minIndex + 1, len(heights) - 1, heights, 1))

    def find(self, first, end, heights, state):
        if first >= end:
            if state == 0:
                return heights[first]
            else:
                return heights[end]
        minHeight = sys.maxsize
        minIndex = -1
        for i in range(first, end + 1, 1):
            if heights[i] < minHeight:
                minHeight = heights[i]
                minIndex = i
        return max(minHeight * (end - first + 1), self.find(first, minIndex - 1, heights, 0), self.find(minIndex + 1, end, heights, 1))

s = Solution()
res = s.largestRectangleArea([0])
print(res)