"""
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]

示例 2:
输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]

"""

import sys

class Solution(object):
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []
        if len(matrix) == 1:
            return matrix[0]
        res = []
        # 列
        column = 0
        # 行
        row = 0
        # 0: 上 1: 下 2: 左 3: 右
        state = 3
        while len(res) < len(matrix) * len(matrix[0]):
            if state == 0:
                while row >= 0 and matrix[row][column] != sys.maxsize:
                    res.append(matrix[row][column])
                    matrix[row][column] = sys.maxsize
                    row-= 1
                row+= 1
                column+= 1
                state = 3
                continue
            if state == 1:
                while row < len(matrix) and matrix[row][column] != sys.maxsize:
                    res.append(matrix[row][column])
                    matrix[row][column] = sys.maxsize
                    row+= 1
                row -= 1
                column-= 1
                state = 2
                continue
            if state == 2:
                while column >= 0 and matrix[row][column] != sys.maxsize:
                    if matrix[row][column] == sys.maxsize:
                        break
                    res.append(matrix[row][column])
                    matrix[row][column] = sys.maxsize
                    column-= 1
                column += 1
                row-= 1
                state = 0
                continue
            if state == 3:
                while column < len(matrix[0]) and matrix[row][column] != sys.maxsize:
                    res.append(matrix[row][column])
                    matrix[row][column] = sys.maxsize
                    column+= 1
                column -= 1
                row+= 1
                state = 1
                continue
        return res

s = Solution()
res = s.spiralOrder(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
)
print(res)