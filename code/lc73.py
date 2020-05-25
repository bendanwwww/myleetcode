"""
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:
输入:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

示例 2:
输入:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

进阶:
一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个常数空间的解决方案吗？

"""

import sys

class Solution(object):
    def setZeroes(self, matrix):
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if matrix[x][y] == sys.maxsize:
                    continue
                if matrix[x][y] == 0:
                    for i in range(len(matrix[x])):
                        if matrix[x][i] != 0:
                            matrix[x][i] = sys.maxsize
                    for i in range(len(matrix)):
                        if matrix[i][y] != 0:
                            matrix[i][y] = sys.maxsize

        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if matrix[x][y] == sys.maxsize:
                    matrix[x][y] = 0

s = Solution()
matrix = [[1, 1, 1],
          [0, 1, 2]]
# [[0,1,1],[0,0,0]]
s.setZeroes(matrix)
print(matrix)