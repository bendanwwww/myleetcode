"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:
输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true

示例 3:
输入: "(]"
输出: false

示例 4:
输入: "([)]"
输出: false

示例 5:
输入: "{[]}"
输出: true

"""

class Solution(object):
    def isValid(self, s):
        stack = []
        if len(s) % 2 != 0:
            return False
        for i in range(len(s)):
            if s[i] in ['(', '[', '{']:
                stack.append(s[i])
            else:
                if len(stack) > len(s) - i:
                    return False
                if len(stack) == 0:
                    return False
                stackLast = stack.pop()
                if s[i] == ')' and stackLast != '(' or s[i] == ']' and stackLast != '[' or s[i] == '}' and stackLast != '{':
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

s = Solution()
res = s.isValid(']')
print(res)