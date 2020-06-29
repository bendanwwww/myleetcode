"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

"""

class Solution(object):
    def trap(self, height):
        res = 0
        if len(height) == 0:
            return 0
        findMap = {}
        last = height[0]
        lastIndex = 0
        tmp = 0
        for i in range(1, len(height)):
            if height[i] >= last:
                findMap[(lastIndex, i)] = 1
                last = height[i]
                lastIndex = i
                res+= tmp
                tmp = 0
            else:
                tmp+= last - height[i]

        last = height[len(height) - 1]
        lastIndex = len(height) - 1
        tmp = 0
        for i in range(len(height) - 2, -1, -1):
            if height[i] >= last:
                if (i, lastIndex) not in findMap:
                    res+= tmp
                last = height[i]
                lastIndex = i
                tmp = 0
            else:
                tmp+= last - height[i]
        return res

s = Solution()
res = s.trap([2, 0, 2])
print(res)
