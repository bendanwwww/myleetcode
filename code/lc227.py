"""
实现一个基本的计算器来计算一个简单的字符串表达式的值。
字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

示例 1:
输入: "3 + 2 * 2"
输出: 7

示例 2:
输入: "3 / 2"
输出: 1

示例 3:
输入: "3 + 5 / 2"
输出: 5

说明：
你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。

"""

class Solution(object):
    def calculate(self, s):
        # 预处理
        nums = []
        tmp = 0

        for c in s:
            if c == ' ':
                continue
            if c.isnumeric():
                tmp = tmp * 10 + int(c)
            else:
                nums.append(tmp)
                nums.append(c)
                tmp = 0
        nums.append(tmp)

        stack = []
        for c in nums:
            # 若栈顶元素为乘除, 先运算这部分
            if len(stack) > 0 and (stack[len(stack) - 1] == '/' or stack[len(stack) - 1] == '*'):
                symbol = stack.pop()
                num = stack.pop()
                if symbol == '/':
                    stack.append(int(int(num) / int(c)))
                else:
                    stack.append(int(num) * int(c))
            else:
                stack.append(c)

        res = 0
        symbol = ''
        for c in stack:
            if c == '+' or c == '-':
                symbol = c
            else:
                if symbol == '':
                    res = int(c)
                else:
                    if symbol == '+':
                        res = res + int(c)
                    else:
                        res = res - int(c)

        return res

s = Solution()
res = s.calculate("2*3+2")
print(res)
