"""
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:
X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：
X X X X
X X X X
X X X X
X O X X
解释:
被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

"""

class Solution(object):
    def solve(self, board):
        if len(board) == 0:
            return

        indexMap = {}
        queue = []
        # 查找边界的O
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                indexMap['0,' + str(i)] = 1
                queue.append([0, i])
            if board[len(board) - 1][i] == 'O':
                indexMap[str(len(board) - 1) + ',' + str(i)] = 1
                queue.append([len(board) - 1, i])

        for i in range(1 , len(board)):
            if board[i][0] == 'O':
                indexMap[str(i) + ',0'] = 1
                queue.append([i, 0])
            if board[i][len(board[i]) - 1] == 'O':
                indexMap[str(i) + ',' + str(len(board[i]) - 1)] = 1
                queue.append([i, len(board[i]) - 1])

        # 查找与边界O相连的O
        while len(queue) > 0:
            index = queue[0]
            del queue[0]
            # 上
            if index[0] > 0 and board[index[0] - 1][index[1]] == 'O' and str(index[0] - 1) + ',' + str(index[1]) not in indexMap:
                queue.append([index[0] - 1, index[1]])
                indexMap[str(index[0] - 1) + ',' + str(index[1])] = 1
            # 下
            if index[0] < len(board) - 1 and board[index[0] + 1][index[1]] == 'O' and str(index[0] + 1) + ',' + str(index[1]) not in indexMap:
                queue.append([index[0] + 1, index[1]])
                indexMap[str(index[0] + 1) + ',' + str(index[1])] = 1
            # 左
            if index[1] > 0 and board[index[0]][index[1] - 1] == 'O' and str(index[0]) + ',' + str(index[1] - 1) not in indexMap:
                queue.append([index[0], index[1] - 1])
                indexMap[str(index[0]) + ',' + str(index[1] - 1)] = 1
            # 右
            if index[1] < len(board[index[0]]) - 1 and board[index[0]][index[1] + 1] == 'O' and str(index[0]) + ',' + str(index[1] + 1) not in indexMap:
                queue.append([index[0], index[1] + 1])
                indexMap[str(index[0]) + ',' + str(index[1] + 1)] = 1

        for x in range(len(board)):
            for y in range(len(board[x])):
                if str(x) + ',' + str(y) not in indexMap and board[x][y] == 'O':
                    board[x][y] = 'X'

s = Solution()
board = [
            ['X', 'X', 'X', 'X'],
            ['X', 'O', 'O', 'X'],
            ['X', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'X']
        ]
s.solve(board)
print(board)