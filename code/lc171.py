"""
给定一个Excel表格中的列名称，返回其相应的列序号。
例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

示例 1:
输入: "A"
输出: 1

示例 2:
输入: "AB"
输出: 28

示例 3:
输入: "ZY"
输出: 701

"""

class Solution(object):
    def titleToNumber(self, s):
        res = 0
        index = len(s)
        for t in s:
            res+= (int(ord(t)) - 64) * (26 ** (index - 1))
            index-= 1
        return res

s = Solution()
res = s.titleToNumber("AA")
print(res)