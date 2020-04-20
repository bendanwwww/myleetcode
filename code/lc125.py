"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:
输入: "race a car"
输出: false

"""

class Solution(object):
    def isPalindrome(self, s):
        if len(s) == 0:
            return True
        first = 0
        last = len(s) - 1
        while first < last:
            if s[first] == ' ' or (s[first].lower() < 'a' or s[first].lower() > 'z') and (s[first] < '0' or s[first] > '9'):
                first+= 1
                continue
            if s[last] == ' ' or (s[last].lower() < 'a' or s[last].lower() > 'z') and (s[last] < '0' or s[last] > '9'):
                last-= 1
                continue
            if s[first] != s[last] and s[first].lower() != s[last] and s[first] != s[last].lower():
                return False
            first += 1
            last -= 1
        return True

s = Solution()
res = s.isPalindrome("0P")
print(res)