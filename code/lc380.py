"""
设计一个支持在平均 时间复杂度 O(1) 下，执行以下操作的数据结构。

insert(val)：当元素 val 不存在时，向集合中插入该项。
remove(val)：元素 val 存在时，从集合中移除该项。
getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。
示例 :

// 初始化一个空的集合。
RandomizedSet randomSet = new RandomizedSet();

// 向集合中插入 1 。返回 true 表示 1 被成功地插入。
randomSet.insert(1);

// 返回 false ，表示集合中不存在 2 。
randomSet.remove(2);

// 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
randomSet.insert(2);

// getRandom 应随机返回 1 或 2 。
randomSet.getRandom();

// 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
randomSet.remove(1);

// 2 已在集合中，所以返回 false 。
randomSet.insert(2);

// 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
randomSet.getRandom();

"""

import random

class RandomizedSet(object):

    map = {}
    array = []
    def __init__(self):
        self.map = {}
        self.array = []

    def insert(self, val):
        global array
        global map
        if val in self.map:
            return False
        self.array.append(val)
        self.map[val] = len(self.array) - 1
        return True

    def remove(self, val):
        global array
        global map
        if val in self.map:
            tmp = self.array[len(self.array) - 1]
            n1 = self.map[val]
            n2 = self.map[tmp]
            self.array[n2] = val
            self.array[n1] = tmp
            self.map[tmp] = n1
            self.map.pop(val)
            self.array.remove(val)
            return True
        return False

    def getRandom(self):
        n = random.randint(0, len(self.array) - 1)
        return self.array[n]

s = RandomizedSet()
res1 = s.insert(-1)
res2 = s.remove(-2)
res3 = s.insert(-2)
res4 = s.getRandom()
res5 = s.remove(-1)
res6 = s.insert(-2)
res7 = s.getRandom()
print(res1)
print(res2)
print(res3)
print(res4)
print(res5)
print(res6)
print(res7)