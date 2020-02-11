"""
根据百度百科，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在1970年发明的细胞自动机。

给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞具有一个初始状态 live（1）即为活细胞， 或 dead（0）即为死细胞。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
根据当前状态，写一个函数来计算面板上细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。

示例:

输入:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
输出:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

进阶:
你可以使用原地算法解决本题吗？请注意，面板上所有格子需要同时被更新：你不能先更新某些格子，然后使用它们的更新后的值再更新其他格子。
本题中，我们使用二维数组来表示面板。原则上，面板是无限的，但当活细胞侵占了面板边界时会造成问题。你将如何解决这些问题？

"""

class Solution(object):

    live = 0

    def gameOfLife(self, board):
        if len(board) == 0:
            return board

        # 1 -> 0 = -1
        # 0 -> 1 = 2
        # board[i - 1][x - 1]
        # board[i - 1][x]
        # board[i - 1][x + 1]
        # board[i][x - 1]
        # board[i][x + 1]
        # board[i + 1][x - 1]
        # board[i + 1][x]
        # board[i + 1][x + 1]
        for i in range(len(board)):
            for x in range(len(board[i])):
                self.live = 0
                if i - 1 >= 0:
                    if x - 1 >= 0:
                        self.liveOrDead(board[i - 1][x - 1])
                    if x + 1 < len(board[i]):
                        self.liveOrDead(board[i - 1][x + 1])
                    self.liveOrDead(board[i - 1][x])
                if x - 1 >= 0:
                    self.liveOrDead(board[i][x - 1])
                if x + 1 < len(board[i]):
                    self.liveOrDead(board[i][x + 1])
                if i + 1 < len(board):
                    if x - 1 >= 0:
                        self.liveOrDead(board[i + 1][x - 1])
                    if x + 1 < len(board[i]):
                        self.liveOrDead(board[i + 1][x + 1])
                    self.liveOrDead(board[i + 1][x])

                if board[i][x] == 1:
                    if self.live < 2 or self.live > 3:
                        board[i][x] = -1
                if board[i][x] == 0:
                    if self.live == 3:
                        board[i][x] = 2

        for i in range(len(board)):
            for x in range(len(board[i])):
                if board[i][x] == -1:
                    board[i][x] = 0
                if board[i][x] == 2:
                    board[i][x] = 1

    def liveOrDead(self, state):
            if state == 1 or state == -1:
                self.live+= 1

s = Solution()
board = [
            [1]
         ]
s.gameOfLife(board)
print(board)