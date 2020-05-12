"""
一条包含字母 A-Z 的消息通过以下方式进行了编码：
'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:
输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。

示例 2:
输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

"""

class Solution(object):
    def numDecodings(self, s):
        if len(s) == 0 or s[0] == '0':
            return 0
        if len(s) == 1:
            if s == '0':
                return 0
            else:
                return 1
        dp = [0] * len(s)
        dp[0] = 1
        if int(s[0]) > 2 and s[1] == '0':
            return 0
        if (int(s[0]) < 2 and int(s[1]) > 0) or (int(s[0]) == 2 and int(s[1]) <= 6 and int(s[1]) > 0):
            dp[1] = 2
        else:
            dp[1] = 1
        for i in range(2, len(s)):
            if s[i] == '0' and (int(s[i - 1]) > 2 or int(s[i - 1]) == 0):
                return 0
            if int(s[i - 1]) < 2 or (int(s[i - 1]) == 2 and int(s[i]) <= 6):
                if int(s[i]) > 0 and int(s[i - 1]) > 0:
                    dp[i] = dp[i - 1] + dp[i - 2]
                else:
                    dp[i] = dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[len(s) - 1]

s = Solution()
res = s.numDecodings("20")
print(res)
