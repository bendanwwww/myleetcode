"""
给定一个字符串列表，你可以将这些字符串连接成一个循环字符串，对于每个字符串，你可以选择是否翻转它。在所有可能的循环字符串中，你需要分割循环字符串（这将使循环字符串变成一个常规的字符串），然后找到字典序最大的字符串。
具体来说，要找到字典序最大的字符串，你需要经历两个阶段：
将所有字符串连接成一个循环字符串，你可以选择是否翻转某些字符串，并按照给定的顺序连接它们。
在循环字符串的某个位置分割它，这将使循环字符串从分割点变成一个常规的字符串。
你的工作是在所有可能的常规字符串中找到字典序最大的一个。

示例:
输入: "abc", "xyz"
输出: "zyxcba"
解释: 你可以得到循环字符串 "-abcxyz-", "-abczyx-", "-cbaxyz-", "-cbazyx-"，
其中 '-' 代表循环状态。
答案字符串来自第四个循环字符串，
你可以从中间字符 'a' 分割开然后得到 "zyxcba"。
 
注意:
输入字符串只包含小写字母。
所有字符串的总长度不会超过 1,000。

"""

class Solution(object):
    def splitLoopedString(self, strs):
        for i in range(len(strs)):
            s_tmp = strs[i][::-1]
            if s_tmp > strs[i]:
                strs[i] = s_tmp

        max_str = ''
        for i in range(len(strs)):
            str_index = strs[i]
            str_index_flip = strs[i][::-1]
            for n in range(len(str_index)):
                tmp_max_1 = str_index[n:] + ''.join(strs[i + 1:]) + ''.join(strs[:i]) + str_index[:n]
                tmp_max_2 = str_index_flip[n:] + ''.join(strs[i + 1:]) + ''.join(strs[:i]) + str_index_flip[:n]
                max_str = max(max_str, tmp_max_1, tmp_max_2)

        return max_str

s = Solution()
res = s.splitLoopedString(['azb', 'a'])
print(res)