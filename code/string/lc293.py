"""
你和朋友玩一个叫做「翻转游戏」的游戏，游戏规则：给定一个只有 + 和 - 的字符串。你和朋友轮流将 连续 的两个 "++" 反转成 "--"。 当一方无法进行有效的翻转时便意味着游戏结束，则另一方获胜。
请你写出一个函数，来计算出第一次翻转后，字符串所有的可能状态。

示例：
输入: s = "++++"
输出:
[
  "--++",
  "+--+",
  "++--"
]
注意：如果不存在可能的有效操作，请返回一个空列表 []。

"""

class Solution(object):
    def generatePossibleNextMoves(self, s):
        res = []
        for i in range(0, len(s) - 1):
            if s[i] == '+' and s[i + 1] == '+':
                data = s[:i] + "--"
                if i < len(s) - 1:
                    data += s[i + 2:]
                res.append(data)
        return res

s = Solution()
res = s.generatePossibleNextMoves("++++")
print(res)