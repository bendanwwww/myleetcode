"""
给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。

示例 1:
输入: [[1,1],[2,2],[3,3]]
输出: 3
解释:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4

示例 2:
输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出: 4
解释:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6

"""

class Solution(object):
    def maxPoints(self, points):
        if len(points) < 3:
            return len(points)
        res = 0
        for i in range(len(points)):
            maxNumber = 0
            repeatNumber = 0
            kMap = {}
            for x in range(i + 1, len(points)):
                # 判断点是否重合
                if points[i][0] == points[x][0] and points[i][1] == points[x][1]:
                    repeatNumber+= 1
                    continue
                # 计算斜率
                k = self.countK(points[i], points[x])
                if k in kMap:
                    kMap[k].append(x)
                else:
                    kMap[k] = [x]
                maxNumber = max(maxNumber, len(kMap[k]))
            res = max(res, maxNumber + repeatNumber + 1)
        return res

    def countK(self, p1, p2):
        x = p1[0] - p2[0]
        y = p1[1] - p2[1]
        # 约分 辗转相除法
        if y == 0:
            return '00'
        else:
            while y != 0:
                tmp = x % y
                x = y
                y = tmp
            return str((p1[0] - p2[0]) / x) + '/' + str((p1[1] - p2[1]) / x)

s = Solution()
res = s.maxPoints([[1, 1], [1, 1], [1, 1]])
print(res)