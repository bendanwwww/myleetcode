"""
根据逆波兰表示法，求表达式的值。
有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

说明：
整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

示例 1：
输入: ["2", "1", "+", "3", "*"]
输出: 9
解释: ((2 + 1) * 3) = 9

示例 2：
输入: ["4", "13", "5", "/", "+"]
输出: 6
解释: (4 + (13 / 5)) = 6

示例 3：
输入: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
输出: 22
解释:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

"""

import operator

class Solution(object):
    def evalRPN(self, tokens):
        if len(tokens) == 1:
            return int(tokens[0])

        ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        stack = []
        stack.append(int(tokens[0]))
        stack.append(int(tokens[1]))
        index = 1
        while index < len(tokens) - 1:
            index+= 1
            if self.is_int(tokens[index]):
                stack.append(int(tokens[index]))
            else:
                a = stack[len(stack) - 1]
                b = stack[len(stack) - 2]
                del stack[-1]
                del stack[-1]
                stack.append(int(ops[tokens[index]](int(b), int(a))))
        return stack[0]

    def is_int(self, str):
        try:
            int(str)
            return True
        except ValueError:
            return False

s = Solution()
res = s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
print(res)
