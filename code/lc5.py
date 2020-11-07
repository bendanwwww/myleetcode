"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"

"""

class Solution(object):
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s
        res = s[0]
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            if i < len(s) - 1:
                dp[i][i + 1] = s[i] == s[i + 1]
                dp[i + 1][i] = s[i] == s[i + 1]
                if dp[i][i + 1]:
                    res = s[i:i + 2]

        for i in range(2, len(s)):
            for x in range(len(s) - i):
                dp[x][x + i] = (dp[x + 1][x + i - 1] and s[x] == s[x + i])
                dp[x + i][x] = (dp[x + 1][x + i - 1] and s[x] == s[x + i])
                if dp[x][x + i]:
                    res = s[x:x + i + 1]
        return res

s = Solution()
res = s.longestPalindrome('babad')
print(res)

