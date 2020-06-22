"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""

class Solution(object):
    def permute(self, nums):
        dp = [[] for _ in range(len(nums))]
        dp[0] = [[0]]
        for i in range(1, len(nums)):
            for x in range(0, i + 1):
                for y in dp[i - 1]:
                    tmp = []
                    tmp.append(x)
                    tmpDp = y[:]
                    for z in range(len(tmpDp)):
                        if tmpDp[z] == x:
                            tmpDp[z] = i
                            break
                    tmp+= tmpDp
                    dp[i].append(tmp)

        res = []
        for dp in dp[len(nums) - 1]:
            tmpRes = []
            for i in dp:
                tmpRes.append(nums[i])
            res.append(tmpRes)
        return res

s = Solution()
res = s.permute([5, 2])
print(res)