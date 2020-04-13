"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
说明：
拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。

示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        wordMap = {}
        for w in wordDict:
            wordMap[w] = w
        #return self.DFS(s, wordMap)
        return self.BFS(s, wordMap)

    # 深度优先遍历
    def DFS(self, s, wordMap):
        word = s
        index = 0
        wordStack = []
        while len(word) > 0:
            tmp = word[0:index]
            b = False
            for i in range(index, len(word)):
                tmp+= word[i]
                if tmp in wordMap:
                    wordStack.append([word, i + 1])
                    word = word[i + 1:]
                    b = True
                    if len(word) == 0:
                        return True
                    break
            if not b:
                if len(wordStack) == 0:
                    return False
                word = wordStack[len(wordStack) - 1][0]
                index = wordStack[len(wordStack) - 1][1]
                del wordStack[len(wordStack) - 1]

    # 宽度优先遍历
    def BFS(self, s, wordMap):
        wordQueue = [s]
        while len(wordQueue) > 0:
            tmpWord = wordQueue[0]
            del wordQueue[0]
            word = ''
            for i in range(len(tmpWord)):
                word+= tmpWord[i]
                if word in wordMap:
                    if i == len(tmpWord) - 1:
                        return True
                    wordQueue.append(tmpWord[i + 1:])
        return False

s = Solution()
words = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
print(s.wordBreak(words, wordDict))
