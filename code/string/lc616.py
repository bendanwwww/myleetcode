"""
给一个字符串 s 和一个字符串列表 dict ，你需要将在字符串列表中出现过的 s 的子串添加加粗闭合标签 <b> 和 </b> 。如果两个子串有重叠部分，你需要把它们一起用一个闭合标签包围起来。同理，如果两个子字符串连续被加粗，那么你也需要把它们合起来用一个加粗标签包围。

样例 1：
输入：
s = "abcxyz123"
dict = ["abc","123"]
输出：
"<b>abc</b>xyz<b>123</b>"
 

样例 2：
输入：
s = "aaabbcc"
dict = ["aaa","aab","bc"]
输出：
"<b>aaabbc</b>c"

"""

class Solution(object):
    def addBoldTag(self, s, dict):
        dict_b = set()
        for d in dict:
            i = 0
            while i < len(s):
                if len(s) - i < len(d):
                    break
                str_tmp = s[i:i + len(d)]
                if str_tmp == d:
                    for n in range(i, i + len(d)):
                        dict_b.add(n)
                i += 1
        dict_b = list(dict_b)
        dict_b.sort()
        res = ""
        last_index = -1
        if len(dict_b) != 0:
            for b in dict_b:
                if b - 1 != last_index:
                    if res != "":
                        res += "</b>"
                    res += s[last_index + 1:b] + "<b>"
                if res == "":
                    res += "<b>"
                res += s[b]
                last_index = b
            res += "</b>"
            if dict_b[len(dict_b) - 1] < len(s) - 1:
                res += s[dict_b[len(dict_b) - 1] + 1:]
        else:
            res = s
        return res

s = Solution()
res = s.addBoldTag("abcxyz123", ["abc", "123"])
print(res)