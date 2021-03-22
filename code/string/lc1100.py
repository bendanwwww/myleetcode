"""
给你一个字符串 S，找出所有长度为 K 且不含重复字符的子串，请你返回全部满足要求的子串的数目。

示例 1：
输入：S = "havefunonleetcode", K = 5
输出：6
解释：
这里有 6 个满足题意的子串，分别是：'havef','avefu','vefun','efuno','etcod','tcode'。

示例 2：
输入：S = "home", K = 5
输出：0
解释：
注意：K 可能会大于 S 的长度。在这种情况下，就无法找到任何长度为 K 的子串。

提示：
1 <= S.length <= 10^4
S 中的所有字符均为小写英文字母
1 <= K <= 10^4

"""

class Solution(object):
    def numKLenSubstrNoRepeats(self, S, K):
        res = 0
        word_map = {}
        first_index = 0
        index = 0
        while index < len(S):
            if index - first_index == K:
                res += 1
                first_index += 1
            if S[index] in word_map:
                same_index = word_map[S[index]]
                same_index.sort()
                if same_index[len(same_index) - 1] >= first_index:
                    first_index = same_index[len(same_index) - 1] + 1
                word_map[S[index]].append(index)
            else:
                word_map[S[index]] = [index]
            index += 1
        if index - first_index == K:
            res += 1
        return res

s = Solution()
res = s.numKLenSubstrNoRepeats("aaaaaaaa", 2)
print(res)