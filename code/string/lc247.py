"""
中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。
找到所有长度为 n 的中心对称数。

示例 :
输入:  n = 2
输出: ["11","69","88","96"]

"""

class Solution(object):

    one_str = ["0", "1", "8"]
    double_str = ["11", "69", "88", "96"]

    def findStrobogrammatic(self, n):
        if n == 0:
            return []
        if n == 1:
            return self.one_str
        if n == 2:
            return self.double_str
        res_str = []
        res_str.append(self.double_str[0])
        res_str.append(self.double_str[1])
        res_str.append(self.double_str[2])
        res_str.append(self.double_str[3])
        if int(n / 2) > 1:
            res_str.append("00")
        res_str = self.make_str(res_str, int(n / 2) - 1)
        if n % 2 == 1:
            res_str_new = []
            for s in res_str:
                mid = int(len(s) / 2)
                res_str_new.append(s[:mid] + self.one_str[0] + s[mid:])
                res_str_new.append(s[:mid] + self.one_str[1] + s[mid:])
                res_str_new.append(s[:mid] + self.one_str[2] + s[mid:])
            res_str = res_str_new
        return res_str

    def make_str(self, res_str, n):
        if n == 0:
            return res_str
        res_str_new = []
        for s in res_str:
            res_str_new.append(self.double_str[0][0] + s + self.double_str[0][1])
            res_str_new.append(self.double_str[1][0] + s + self.double_str[1][1])
            res_str_new.append(self.double_str[2][0] + s + self.double_str[2][1])
            res_str_new.append(self.double_str[3][0] + s + self.double_str[3][1])
            if n > 1:
                res_str_new.append("0" + s + "0")
        return self.make_str(res_str_new, n - 1)

s = Solution()
res = s.findStrobogrammatic(6)
print(res)