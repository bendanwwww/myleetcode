"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:
输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1

示例 2:
输入: coins = [2], amount = 3
输出: -1

说明:
你可以认为每种硬币的数量是无限的。

"""

import sys

class Solution(object):
    def coinChange(self, coins, amount):
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            minDp = sys.maxsize
            for c in coins:
                if i - c >= 0:
                    minDp = min(minDp, dp[i - c] + 1)
            dp[i] = minDp
        return -1 if (dp[amount] == sys.maxsize) else dp[amount]

s = Solution()
res = s.coinChange([186, 419, 83, 408], 6249)
print(res)