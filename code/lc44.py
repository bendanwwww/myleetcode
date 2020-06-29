"""
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。

示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。

示例 3:
输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。

示例 4:
输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".

示例 5:
输入:
s = "acdcb"
p = "a*c?b"
输出: false

"""

class Solution(object):
    dp = {}

    def isMatch(self, s, p):
        if len(s) == 0 and len(p) == 0:
            return True
        p2 = ''
        for i in p:
            if i != '*' or len(p2) == 0 or p2[len(p2) - 1] != '*':
                p2+= i
        return self.find(s, p2)

    def find(self, s, p):
        if (s, p) in self.dp:
            return self.dp[(s, p)]
        elif s == p or p == '*':
            self.dp[(s, p)] = True
        elif s == '' or p == '':
            self.dp[(s, p)] = False
        elif s[0] == p[0] or p[0] == '?':
            self.dp[(s, p)] = self.find(s[1:], p[1:])
        elif p[0] == '*':
            self.dp[(s, p)] = self.find(s, p[1:]) or self.find(s[1:], p)
        else:
            self.dp[(s, p)] = False
        return self.dp[(s, p)]

s = Solution()
res = s.isMatch("babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb", "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a")
print(res)