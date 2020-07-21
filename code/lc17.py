"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

示例:
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

"""

class Solution(object):
    def letterCombinations(self, digits):
        dictMap = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'],
                   4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'],
                   7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
        dp = []
        if len(digits) == 0:
            return []
        for i in range(len(digits)):
            tmp = dictMap[int(digits[i])]
            if i == 0:
                dp.append(tmp)
            else:
                dpTmp = []
                lastDp = dp[i - 1]
                for s in tmp:
                    for d in lastDp:
                        dpTmp.append(d + s)
                dp.append(dpTmp)
        return dp[len(digits) - 1]

s = Solution()
res = s.letterCombinations("23")
print(res)
