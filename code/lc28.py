"""
实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2

示例 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1

说明:
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

"""

class Solution(object):
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                b = self.find(haystack, needle, i)
                if b:
                    return i
        return -1

    def find(self, haystack, needle, index):
        if len(needle) > len(haystack) - index:
            return False
        for s in needle:
            if index >= len(haystack):
                return False
            if s != haystack[index]:
                return False
            index+= 1
        return True

s = Solution()
res = s.strStr("aaa", "aaaa")
print(res)