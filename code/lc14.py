"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        res = ''
        if len(strs) == 0:
            return res
        index = 0
        same = ''
        while True:
            for s in strs:
                if index >= len(s):
                    return res
                if same == '':
                    same = s[index]
                else:
                    if same != s[index]:
                        return res
            res+= s[index]
            index+= 1
            same = ''
        # return res

s = Solution()
res = s.longestCommonPrefix(["flower", "flow", "flight"])
print(res)
