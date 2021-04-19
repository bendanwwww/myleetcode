

class Solution(object):
    res = 0

    def smallestFactorization(self, a):
        self.all_num_list = []
        if a < 10:
            return a
        # for i in range(2, 9):
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
                # break

s = Solution()
res = s.smallestFactorization(18000000)
print(res)