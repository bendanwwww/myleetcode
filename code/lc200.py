"""
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

示例 1:
输入:
11110
11010
11000
00000
输出: 1

示例 2:
输入:
11000
11000
00100
00011
输出: 3

"""

class Solution(object):
    def numIslands(self, grid):
        if len(grid) == 0:
            return 0
        res = 0
        isFind = [([False] * len(grid[0])) for i in range(len(grid))]
        for i in range(len(grid)):
            for x in range(len(grid[i])):
                if not isFind[i][x] and grid[i][x] == '1':
                    self.find(grid, isFind, i, x)
                    res+= 1
        return res

    def find(self, grid, isFind, i, x):
        queue = []
        queue.append([i, x])
        while len(queue) > 0:
            i = queue[0][0]
            x = queue[0][1]
            del queue[0]
            isFind[i][x] = True
            if i - 1 >= 0 and not isFind[i - 1][x] and grid[i - 1][x] == '1':
                queue.append([i - 1, x])
            if x - 1 >= 0 and not isFind[i][x - 1] and grid[i][x - 1] == '1':
                queue.append([i, x - 1])
            if i + 1 < len(grid) and not isFind[i + 1][x] and grid[i + 1][x] == '1':
                queue.append([i + 1, x])
            if x + 1 < len(grid[i]) and not isFind[i][x + 1] and grid[i][x + 1] == '1':
                queue.append([i, x + 1])

s = Solution()
res = s.numIslands([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]])
print(res)