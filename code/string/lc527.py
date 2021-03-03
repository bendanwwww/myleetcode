"""
给定一个由n个不重复非空字符串组成的数组，你需要按照以下规则为每个单词生成最小的缩写。

初始缩写由起始字母+省略字母的数量+结尾字母组成。
若存在冲突，亦即多于一个单词有同样的缩写，则使用更长的前缀代替首字母，直到从单词到缩写的映射唯一。换而言之，最终的缩写必须只能映射到一个单词。
若缩写并不比原单词更短，则保留原样。

示例:
输入: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
输出: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]

注意:
n和每个单词的长度均不超过 400。
每个单词的长度大于 1。
单词只由英文小写字母组成。
返回的答案需要和原数组保持同一顺序。

"""

class Solution(object):
    def wordsAbbreviation(self, dict):
        res = []
        index = 1
        same_list = set(dict)
        same_dict = {}
        for i in range(len(dict)):
            res.append(dict[i])
            same_dict[dict[i]] = [i]
        while len(same_list) > 0:
            same_list_tmp = set()
            same_dict_tmp = {}
            for s in same_list:
                for i in same_dict[s]:
                    tmp = dict[i]
                    s_append = tmp[:index] + str(len(tmp) - index - 1) + tmp[-1:]
                    if len(s_append) >= len(tmp):
                        s_append = tmp
                    res[i] = s_append
                    if s_append in same_dict_tmp:
                        same_dict_tmp[s_append].append(i)
                        same_list_tmp.add(s_append)
                    else:
                        same_dict_tmp[s_append] = [i]
            same_list = same_list_tmp
            same_dict = same_dict_tmp
            index += 1
        return res

s = Solution()
res = s.wordsAbbreviation(["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"])
print(res)