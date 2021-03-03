"""
给一个 非空 字符串 s 和一个单词缩写 abbr ，判断这个缩写是否可以是给定单词的缩写。
字符串 "word" 的所有有效缩写为：
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
注意单词 "word" 的所有有效缩写仅包含以上这些。任何其他的字符串都不是 "word" 的有效缩写。
注意:
假设字符串 s 仅包含小写字母且 abbr 只包含小写字母和数字。

示例 1:
给定 s = "internationalization", abbr = "i12iz4n":
函数返回 true.
         

示例 2:
给定 s = "apple", abbr = "a2e":
函数返回 false.

"""

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        word_index = 0
        add = ''
        for i in abbr:
            if ord(i) >= ord('0') and ord(i) <= ord('9'):
                if add == '0':
                    return False
                add += i
            else:
                if add != '':
                    if add == '0':
                        return False
                    word_index += int(add)
                if word_index >= len(word) or i != word[word_index]:
                    return False
                add = ''
                word_index += 1
        if add != '':
            word_index += int(add)
        return word_index == len(word)


s = Solution()
res = s.validWordAbbreviation("a", "01")
print(res)
