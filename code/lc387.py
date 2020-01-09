"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:
s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.

"""

class Solution(object):
    def firstUniqChar(self, s):
        map = {}
        for i in range(len(s)):
            if s[i] in map:
                map[s[i]] = -1
            else:
                map[s[i]] = i
        for i in range(len(s)):
            if map[s[i]] != -1:
                return map[s[i]]
        return -1

s = Solution()
res = s.firstUniqChar("loveleetcode")
print(res)