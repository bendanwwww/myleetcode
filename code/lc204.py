"""
统计所有小于非负整数 n 的质数的数量。

示例:
输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""

class Solution(object):
    def countPrimes(self, n):
        primes = [True] * n
        res = 0
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for x in range(i * i, n, i):
                    if primes[x]:
                        primes[x] = False
                        res += 1
        return 0 if (n - res - 2) < 0 else n - res - 2

s = Solution()
res = s.countPrimes(13)
print(res)