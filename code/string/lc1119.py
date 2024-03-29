"""
给你一个字符串 S，请你删去其中的所有元音字母（'a', 'e', 'i', 'o', 'u'），并返回这个新字符串。

示例 1：
输入："leetcodeisacommunityforcoders"
输出："ltcdscmmntyfrcdrs"

示例 2：
输入："aeiou"
输出：""

提示：
S 仅由小写英文字母组成。
1 <= S.length <= 1000

"""

class Solution(object):
    def removeVowels(self, s):
        res = ""
        dict_word = ['a', 'e', 'i', 'o', 'u']
        for i in range(len(s)):
            if s[i] not in dict_word:
                res += s[i]
        return res

s = Solution()
res = s.removeVowels("leetcodeisacommunityforcoders")
print(res)