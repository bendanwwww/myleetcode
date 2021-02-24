"""
给定一个字符串，逐个翻转字符串中的每个单词。

示例：
输入: ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
输出: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

注意：
单词的定义是不包含空格的一系列字符
输入字符串中不会包含前置或尾随的空格
单词与单词之间永远是以单个空格隔开的

进阶：使用 O(1) 额外空间复杂度的原地解法。

"""

class Solution(object):
    def reverseWords(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
            left += 1
            right -= 1
        first = 0
        for i in range(len(s)):
            if s[i] == " " or i == len(s) - 1:
                l = first
                if i == len(s) - 1:
                    r = i
                else:
                    r = i - 1
                while l < r:
                    tmp = s[l]
                    s[l] = s[r]
                    s[r] = tmp
                    l += 1
                    r -= 1
                first = i + 1

s = Solution()
ss = ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
s.reverseWords(ss)
print(ss)