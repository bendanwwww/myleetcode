"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

"""

class Solution(object):
    def groupAnagrams(self, strs):
        if len(strs) == 0:
            return []
        keyMap = {}
        res = []
        for s in strs:
            l = list(s)
            l.sort()
            tmp = "".join(l)
            if tmp in keyMap:
                tmpList = keyMap[tmp]
                tmpList.append(s)
                keyMap[tmp] = tmpList
            else:
                keyMap[tmp] = [s]

        for k in keyMap:
            res.append(keyMap[k])

        return res

s = Solution()
res = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(res)