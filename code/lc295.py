"""
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，
[2,3,4] 的中位数是 3
[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：
void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。

示例：
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2

进阶:
如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？

"""

import heapq

class MedianFinder(object):

    numMaxHeap = []
    numMinHeap = []
    count = 0

    def __init__(self):
        self.numMaxHeap = []
        self.numMinHeap = []
        self.count = 0

    def addNum(self, num):
        self.count+= 1
        heapq.heappush(self.numMaxHeap, -num)
        heapq.heappush(self.numMinHeap, -heapq.heappop(self.numMaxHeap))
        if self.count % 2 == 1:
            heapq.heappush(self.numMaxHeap, -heapq.heappop(self.numMinHeap))

    def findMedian(self):
        if self.count == 0:
            return 0.0
        if self.count % 2 == 0:
            return (-self.numMaxHeap[0] + self.numMinHeap[0]) / 2.0
        else:
            return -self.numMaxHeap[0]

s = MedianFinder()
s.addNum(1)
s.addNum(2)
print(s.findMedian())
s.addNum(3)
print(s.findMedian())