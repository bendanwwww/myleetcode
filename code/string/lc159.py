"""
给定一个字符串 s ，找出 至多 包含两个不同字符的最长子串 t ，并返回该子串的长度。

示例 1:
输入: "eceba"
输出: 3
解释: t 是 "ece"，长度为3。

示例 2:
输入: "ccaabbb"
输出: 5
解释: t 是 "aabbb"，长度为5。

"""

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        char_set = []
        index = 0
        max_num = 0
        tmp_max = 0
        i = 0
        while i < len(s):
            if s[i] in char_set:
                tmp_max += 1
                i += 1
                continue
            if len(char_set) < 2:
                char_set.append(s[i])
                tmp_max += 1
                if len(char_set) == 2:
                    index = i
                i += 1
            else:
                max_num = max(max_num, tmp_max)
                tmp_max = 0
                char_set = []
                i = index
        return max(max_num, tmp_max)

s = Solution()
res = s.lengthOfLongestSubstringTwoDistinct("aabbddd")
print(res)