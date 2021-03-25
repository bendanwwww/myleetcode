"""
给出一个字符串 s 和一个整数 k，请你帮忙判断这个字符串是不是一个「K 回文」。
所谓「K 回文」：如果可以通过从字符串中删去最多 k 个字符将其转换为回文，那么这个字符串就是一个「K 回文」。

示例：
输入：s = "abcdeca", k = 2
输出：true
解释：删除字符 “b” 和 “e”。

"""

class Solution(object):
    def isValidPalindrome(self, s, k):
        s_len = len(s)
        dp = [[0 for i in range(s_len)] for j in range(s_len)]
        for i in range(1, s_len):
            first_index = 0
            while first_index < s_len - i:
                last_index = first_index + i
                if s[first_index] == s[last_index]:
                    dp[first_index][last_index] = dp[first_index + 1][last_index - 1]
                else:
                    dp[first_index][last_index] = min(dp[first_index + 1][last_index], dp[first_index][last_index - 1]) + 1
                first_index += 1
        return dp[0][s_len - 1] <= k

s = Solution()
res = s.isValidPalindrome("bacabaaa", 2)
print(res)