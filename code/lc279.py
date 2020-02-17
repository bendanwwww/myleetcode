"""
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:
输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.

示例 2:
输入: n = 13
输出: 2
解释: 13 = 4 + 9.

"""

import sys

class Solution(object):
    def numSquares(self, n):
        dp = [sys.maxsize] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            for x in range(1, int(i ** 0.5) + 1):
                dp[i] = min(dp[i], (dp[i - x * x] + 1))
        return dp[n]

s = Solution()
res = s.numSquares(13)
print(res)