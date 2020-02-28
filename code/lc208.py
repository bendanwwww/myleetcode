"""
实现一个 Trie (前缀树)，包含 insert, search 和 startsWith 这三个操作。

示例:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true

说明:
你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。

"""

class Node(object):

    def __init__(self, val, end):
        self.val = val
        self.next = []
        self.end = end

class Trie(object):

    head = None

    def __init__(self):
        self.head = Node(None, False)

    def insert(self, word):
        nodes = self.head.next
        lastNode = self.head
        # 查找共同的前缀
        index = 0
        for s in word:
            b = False
            for t in nodes:
                if t.val == s:
                    nodes = t.next
                    index+= 1
                    lastNode = t
                    b = True
                    break
            if not b:
                break
        if index == len(word):
            lastNode.end = True
        else:
            tmpNodes = lastNode.next
            for i in range(index, len(word)):
                n = None
                if i == len(word) - 1:
                    n = Node(word[i], True)
                else:
                    n = Node(word[i], False)
                tmpNodes.append(n)
                tmpNodes = n.next

    def search(self, word):
        nodes = self.head.next
        lastNode = self.head
        index = 0
        b = False
        for s in word:
            for t in nodes:
                if t.val == s:
                    nodes = t.next
                    index+= 1
                    lastNode = t
                    b = True
                    break
            if not b:
                break
        if index < len(word) or not lastNode.end:
            return False
        else:
            return True


    def startsWith(self, prefix):
        nodes = self.head.next
        lastNode = self.head
        index = 0
        b = False
        for s in prefix:
            for t in nodes:
                if t.val == s:
                    nodes = t.next
                    index+= 1
                    lastNode = t
                    b = True
                    break
            if not b:
                break
        if index < len(prefix):
            return False
        else:
            return True



# Your Trie object will be instantiated and called as such:
s = Trie()
s.insert('apple')
#s.insert('app')
res1 = s.search('app')
res2 = s.startsWith('app')
print(res1)
print(res2)
