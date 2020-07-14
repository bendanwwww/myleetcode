"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例：
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]

"""

class Solution(object):
    def generateParenthesis(self, n):
        dp = []
        dp.append(['()'])
        for i in range(1, n):
            tmp = set([])
            for l in dp[i - 1]:
                # tmp.add('()' + l)
                # tmp.add(l + '()')
                for s in range(0, len(l)):
                    tmp.add(l[:s] + '()' + l[s:])
                tmp.add('('+ l +')')
            dp.append(list(tmp))
        return dp[n - 1]

s = Solution()
res = s.generateParenthesis(4)
print(res)