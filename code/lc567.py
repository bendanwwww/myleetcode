"""
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").

示例2:
输入: s1= "ab" s2 = "eidboaoo"
输出: False

"""

class Solution(object):
    def checkInclusion(self, s1, s2):
        s1_map = {}
        for s in s1:
            if s in s1_map:
                s1_map[s] += 1
            else:
                s1_map[s] = 1
        index = 0
        index_map = {}
        while index < len(s2):
            if self.find(s1_map, index_map):
                return True
            c = s2[index]
            if c not in s1_map:
                index += 1
                index_map = {}
            else:
                if c in index_map:
                    if len(index_map[c]) < s1_map[c]:
                        index_map[c].append(index)
                        index += 1
                    else:
                        index = index_map[c][0] + 1
                        index_map = {}
                else:
                    index_map[c] = [index]
                    index += 1
        return self.find(s1_map, index_map)

    def find(self, s1_map, index_map):
        for k in s1_map:
            if k not in index_map or s1_map[k] != len(index_map[k]):
                return False
        return True

s = Solution()
res = s.checkInclusion('adc', 'dcda')
print(res)