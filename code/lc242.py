"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false

说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

"""

class Solution(object):
    def isAnagram(self, s, t):
        dict1 = {}
        dict2 = {}

        for c in s:
           if c in dict1:
               dict1[c]+= 1
           else:
               dict1[c] = 1

        for c in t:
            if c in dict2:
               dict2[c] += 1
            else:
               dict2[c] = 1

        if len(s) != len(t):
            return False

        for c in s:
            if c not in dict2 or dict1[c] != dict2[c]:
                return False

        return True

s = Solution()
res = s.isAnagram("a", "ab")
print(res)