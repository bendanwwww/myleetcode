"""
给定一个正整数 a，找出最小的正整数 b 使得 b 的所有数位相乘恰好等于 a。
如果不存在这样的结果或者结果不是 32 位有符号整数，返回 0。

样例 1
输入：
48
输出：
68
 
样例 2
输入：
15
输出：
35

"""

class Solution(object):
    res = 0

    def smallestFactorization(self, a):
        self.all_num_list = []
        if a < 10:
            return a
        self.find(a, 2, [])
        return self.res

    def find(self, a, n, num_list):
        if a == 1:
            num_list.sort()
            num = int(''.join(num_list))
            if num > 2147483648:
                return
            if self.res == 0:
                self.res = num
            else:
                self.res = min(self.res, num)
            return
        for i in range(n, 10):
            if i > a:
                break
            if a % i == 0:
                tmp_list = num_list[:]
                tmp_list.append(str(i))
                self.find(a / i, i, tmp_list)

s = Solution()
res = s.smallestFactorization(18000000)
print(res)