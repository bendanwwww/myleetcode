"""
你有一个十进制数字，请按照此规则将它变成「十六进制魔术数字」：首先将它变成字母大写的十六进制字符串，然后将所有的数字 0 变成字母 O ，将数字 1  变成字母 I 。
如果一个数字在转换后只包含 {"A", "B", "C", "D", "E", "F", "I", "O"} ，那么我们就认为这个转换是有效的。
给你一个字符串 num ，它表示一个十进制数 N，如果它的十六进制魔术数字转换是有效的，请返回转换后的结果，否则返回 "ERROR" 。

示例 1：
输入：num = "257"
输出："IOI"
解释：257 的十六进制表示是 101 。

示例 2：
输入：num = "3"
输出："ERROR"

"""

class Solution(object):
    def toHexspeak(self, num):
        dict_digits = [
                        '0', '1', '2', '3', '4', '5', '6', '7', 
                        '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'
                        ]
        dict_valid = ['A', 'B', 'C', 'D', 'E', 'F', 'I', 'O']
        res = ""
        num_tmp = int(num)
        while num_tmp != 0:
            add_str = dict_digits[num_tmp % 16]
            if add_str == '0':
                add_str = 'O'
            if add_str == '1':
                add_str = 'I'
            if add_str not in dict_valid:
                return "ERROR"
            res = add_str + res
            num_tmp = int(num_tmp / 16)
        return res

s = Solution()
res = s.toHexspeak("3")
print(res)