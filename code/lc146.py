"""
运用你所掌握的数据结构，设计和实现一个LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

进阶:
你是否可以在 O(1) 时间复杂度内完成这两种操作？

示例:
LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得密钥 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得密钥 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4

"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.last = None

class LRUCache(object):

    dataMap = {}
    dataNode = {}
    listHead = None
    listTail = None
    size = 0
    capacity = 0

    def __init__(self, capacity):
        self.dataMap = {}
        self.dataNode = {}
        self.listHead = None
        self.listTail = None
        self.size = 0
        self.capacity = capacity

    def get(self, key):
        if key in self.dataMap:
            self.arrangement(key)
            return self.dataMap[key]
        else:
            return -1

    def put(self, key, value):
        if self.size == 0:
            node = ListNode(key)
            self.listHead = node
            self.listTail = node
            self.dataMap[key] = value
            self.dataNode[key] = node
            self.size+= 1
            return
        if key in self.dataMap:
            self.dataMap[key] = value
            self.arrangement(key)
            return
        node = ListNode(key)
        self.listTail.next = node
        node.last = self.listTail
        self.listTail = node
        self.dataMap[key] = value
        self.dataNode[key] = node
        if self.size == self.capacity:
            del self.dataMap[self.listHead.val]
            del self.dataNode[self.listHead.val]
            self.listHead = self.listHead.next
            self.listHead.last = None
        else:
            self.size += 1

    def arrangement(self, key):
        node = self.dataNode[key]
        if node == self.listTail:
            return
        if self.size == 1:
            return
        if node == self.listHead:
            self.listTail.next = node
            self.listHead = node.next
            node.last = self.listTail
            node.next = None
            self.listTail = node
        else:
            lastNode = node.last
            nextNode = node.next
            lastNode.next = nextNode
            nextNode.last = lastNode
            self.listTail.next = node
            node.last = self.listTail
            node.next = None
            self.listTail = node

#[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
cache = LRUCache(10)
cache.put(10, 13)
cache.put(3, 17)
cache.put(6, 11)
cache.put(10, 5)
cache.put(9, 10)
print(cache.get(13))
cache.put(2, 19)
print(cache.get(2))
print(cache.get(3))
cache.put(5, 25)
print(cache.get(8))
cache.put(9, 22)
cache.put(5, 5)
cache.put(1, 30)
print(cache.get(11))
cache.put(9, 12)
print(cache.get(7))
print(cache.get(5))
print(cache.get(8))
print(cache.get(9))
cache.put(4, 30)
cache.put(9, 3)
print(cache.get(9))
print(cache.get(10))
print(cache.get(10))
cache.put(6, 14)
cache.put(3, 1)
print(cache.get(3))
cache.put(10, 11)
print(cache.get(8))
cache.put(2, 14)
print(cache.get(1))
print(cache.get(5))
print(cache.get(4))
cache.put(11, 4)
cache.put(12, 24)
cache.put(5, 18)
print(cache.get(13))
cache.put(7, 23)
print(cache.get(8))
print(cache.get(12))
cache.put(3, 27)
cache.put(2, 12)
