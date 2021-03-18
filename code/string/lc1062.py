"""
给定字符串 S，找出最长重复子串的长度。如果不存在重复子串就返回 0。

示例 1：
输入："abcd"
输出：0
解释：没有重复子串。

示例 2：
输入："abbaba"
输出：2
解释：最长的重复子串为 "ab" 和 "ba"，每个出现 2 次。

示例 3：
输入："aabcaabdaab"
输出：3
解释：最长的重复子串为 "aab"，出现 3 次。

示例 4：
输入："aaaaa"
输出：4
解释：最长的重复子串为 "aaaa"，出现 2 次。

提示：
字符串 S 仅包含从 'a' 到 'z' 的小写英文字母。
1 <= S.length <= 1500

"""

class Solution(object):
    def longestRepeatingSubstring(self, S):
        # 获取后缀字符串数组
        suffix_list = []
        for i in range(len(S)):
            suffix_list.append(S[i:])
        # 后缀字符串排序
        suffix_list.sort()
        # 相邻两个后缀字符串最长重复子串
        max_res = 0
        for i in range(1, len(suffix_list)):
            tmp_max = 0
            first_str = suffix_list[i - 1]
            next_str = suffix_list[i]
            if len(first_str) > len(next_str):
                min_index = len(next_str)
            else:
                min_index = len(first_str)
            for n in range(min_index):
                if first_str[n] == next_str[n]:
                    tmp_max += 1
                else:
                    break
            max_res = max(max_res, tmp_max)
        return max_res

s = Solution()
res = s.longestRepeatingSubstring("aabcaabdaab")
print(res)