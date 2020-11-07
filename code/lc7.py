"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21

注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

"""

class Solution(object):
    def reverse(self, x):
        # x_str = str(x)
        # if len(x_str) < 2:
        #     return x
        # tmp_state = ''
        # if x_str[0] == '-':
        #     tmp_state = '-'
        #     x_str = x_str[1:]
        # res = ''
        # for i in range(len(x_str) - 1, -1, -1):
        #     res+= x_str[i]
        # res = tmp_state + res
        # if int(res) > 2**31 - 1 or int(res) < -2**31:
        #     return 0
        # return int(res)
        res = 0
        tmp_state = False
        if x < 0:
            tmp_state = True
            x = -x
        while x != 0:
            pop = x % 10
            if x < 10 and res > int(2**31 / 10) or (res == int(2**31 / 10) and ((tmp_state and pop > 2**31 % 10) or (not tmp_state and pop > (2**31 - 1) % 10))):
                return 0
            res = res * 10 + pop
            x = int(x / 10)
        if tmp_state:
            res = -res
        return res

s = Solution()
res = s.reverse(900000)
print(res)
