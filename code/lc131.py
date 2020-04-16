"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案。

示例:
输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]

"""

class Solution(object):
    def partition(self, s):
        if len(s) == 0:
            return []
        if len(s) == 1:
            return [[s]]

        res = []
        tmp = []
        for i in s:
            tmp.append(i)
        queue = []
        queue.append([tmp, 0])
        while len(queue) > 0:
            strArray = queue[0][0]
            res.append(strArray)
            index = queue[0][1]
            del queue[0]
            if index >= len(strArray) - 1:
                continue

            for i in range(index, len(strArray)):
                word = strArray[i]
                for z in range(i + 1, len(strArray)):
                    word+= strArray[z]
                    if self.help(word):
                        newArray = []
                        if i > 0:
                            newArray = strArray[:i]
                        newArray.append(word)
                        x = len(newArray)
                        for y in range(z + 1, len(strArray)):
                            newArray.append(strArray[y])
                        queue.append([newArray, x])
        return res

    def help(self, s):
        f = 0
        e = len(s) - 1
        while f < e:
            if s[f] != s[e]:
                return False
            f+= 1
            e-= 1
        return True

s = Solution()
res = s.partition("dcc")
print(res)