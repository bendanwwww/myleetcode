"""
给定一个字符串 s ，找出 至多 包含 k 个不同字符的最长子串 T。

示例 1:
输入: s = "eceba", k = 2
输出: 3
解释: 则 T 为 "ece"，所以长度为 3。

示例 2:
输入: s = "aa", k = 1
输出: 2
解释: 则 T 为 "aa"，所以长度为 2。

"""

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        max_res = 0
        left = 0
        right = 0
        s_dict = {}
        while right < len(s):
            if s[right] in s_dict:
                s_dict[s[right]] += 1
            else:
                s_dict[s[right]] = 1
                if len(s_dict) > k:
                    max_res = max(max_res, right - left)
                    while len(s_dict) > k:
                        s_dict[s[left]] -= 1
                        if s_dict[s[left]] == 0:
                            del s_dict[s[left]]
                        left += 1
            right+= 1
        return max(max_res, right - left)

s = Solution()
res = s.lengthOfLongestSubstringKDistinct("ececbccca", 2)
print(res)