"""
给定两个字符串 s 和 t，判断他们的编辑距离是否为 1。
注意：
满足编辑距离等于 1 有三种可能的情形：
往 s 中插入一个字符得到 t
从 s 中删除一个字符得到 t
在 s 中替换一个字符得到 t

示例 1：
输入: s = "ab", t = "acb"
输出: true
解释: 可以将 'c' 插入字符串 s 来得到 t。

示例 2:
输入: s = "cab", t = "ad"
输出: false
解释: 无法通过 1 步操作使 s 变为 t。

示例 3:
输入: s = "1203", t = "1213"
输出: true
解释: 可以将字符串 s 中的 '0' 替换为 '1' 来得到 t。

"""

class Solution(object):
    def isOneEditDistance(self, s, t):
        if s == t:
            return False

        if len(s) == len(t):
            not_same_num = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    not_same_num += 1
                if not_same_num > 1:
                    return False
            return True

        if abs(len(s) - len(t)) == 1:
            not_same_num = 0
            s_index = 0
            t_index = 0
            while s_index < len(s):
                if t_index == len(t) or s[s_index] != t[t_index]:
                    if len(s) > len(t):
                        s_index += 1
                    else:
                        t_index += 1
                    not_same_num += 1
                else:
                    s_index += 1
                    t_index += 1
                if not_same_num > 1:
                    return False
            return True

        return False

s = Solution()
res = s.isOneEditDistance("a", "")
print(res)