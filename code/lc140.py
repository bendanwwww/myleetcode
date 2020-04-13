"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

说明：
分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

示例 1：
输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
  "cats and dog",
  "cat sand dog"
]

示例 2：
输入:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
输出:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
解释: 注意你可以重复使用字典中的单词。

示例 3：
输入:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
输出:
[]

"""

class Solution(object):

    res = []

    def wordBreak(self, s, wordDict):
        self.res = []
        wordMap = {}
        for w in wordDict:
            wordMap[w] = w

        word = ''
        for i in range(len(s)):
            word+= s[i]
            if word in wordMap:
                self.find(s[i + 1:], wordMap, word)
        return self.res

    def find(self, s, wordMap, str):
        if len(s) == 0:
            self.res.append(str)
            return
        word = ''
        for i in range(len(s)):
            word+= s[i]
            if word in wordMap:
                wordCopy = str[:]
                wordCopy+= ' ' + word
                self.find(s[i + 1:], wordMap, wordCopy)

s = Solution()
w = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
print(s.wordBreak(w, wordDict))
