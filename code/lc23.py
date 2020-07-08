"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:
输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import sys

class Solution(object):
    def mergeKLists(self, lists):
        head = None
        lastNode = None
        nodePoints = []
        for i in range(len(lists)):
            nodePoints.append(lists[i])

        while True:
            min = sys.maxsize
            index = 0
            noneNum = 0
            for x in range(len(nodePoints)):
                if nodePoints[x] is None:
                    noneNum+= 1
                    continue
                if nodePoints[x].val < min:
                    min = nodePoints[x].val
                    index = x
            if noneNum < len(nodePoints):
                if head is None:
                    head = nodePoints[index]
                    lastNode = nodePoints[index]
                else:
                    lastNode.next = nodePoints[index]
                    lastNode = lastNode.next
                nodePoints[index] = nodePoints[index].next
            else:
                break
        return head

s = Solution()
head1 = ListNode(1)
head1.next = ListNode(4)
head1.next.next = ListNode(5)
head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)
head3 = ListNode(2)
head3.next = ListNode(6)
lists = [head1, head2, head3]
res = s.mergeKLists(lists)
print(res)