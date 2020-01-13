"""
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
请注意，它是排序后的第k小元素，而不是第k个元素。

示例:

matrix = [
   [1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

返回 13。

说明:
你可以假设 k 的值永远是有效的, 1 ≤ k ≤ n^2 。

"""

class Solution(object):
    def kthSmallest(self, matrix, k):
        if len(matrix) == 1:
            return matrix[0][0]
        left = matrix[0][0]
        right = matrix[len(matrix) - 1][len(matrix) - 1]
        while left != right:
            mid = int((left + right) / 2)
            n = 0
            for i in range(len(matrix)):
                for x in range(len(matrix)):
                    if matrix[i][x] <= mid:
                        n += 1
            if n < k:
                left = mid + 1
            else:
                right = mid
        return right

s = Solution()
matrix = [
   [1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
# matrix = [
#     [1, 2],
#     [12, 100]
# ]
k = 8
res = s.kthSmallest(matrix, k)
print(res)