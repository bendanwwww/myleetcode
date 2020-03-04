"""
编写一个算法来判断一个数是不是“快乐数”。
一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

示例: 
输入: 19
输出: true
解释:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

"""

class Solution(object):
    def isHappy(self, n):
        slow = self.find(n)
        fast = self.find(slow)
        while slow != fast:
            slow = self.find(slow)
            fast = self.find(self.find(fast))
        if slow == 1:
            return True
        else:
            return False


    def find(self, n):
        sum = 0
        for i in str(n):
            sum+= int(i) * int(i)
        return sum

s = Solution()
res = s.isHappy(2)
print(res)