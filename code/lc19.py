"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.

说明：
给定的 n 保证是有效的。

进阶：
你能尝试使用一趟扫描实现吗？

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        tmpNode = ListNode(0)
        tmpNode.next = head
        node1 = tmpNode
        node2 = tmpNode
        for i in range(0, n + 1):
            node1 = node1.next
        while node1 is not None:
            node1 = node1.next
            node2 = node2.next
        node2.next = node2.next.next
        return tmpNode.next

s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
res = s.removeNthFromEnd(head, 2)
print(res)