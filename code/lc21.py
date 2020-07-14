"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = ListNode()
        headNode = head
        node1 = l1
        node2 = l2
        while True:
            if node1 is None and node2 is None:
                break
            if node1 is None:
                headNode.next = node2
                node2 = node2.next
                headNode = headNode.next
                continue
            if node2 is None:
                headNode.next = node1
                node1 = node1.next
                headNode = headNode.next
                continue
            if node1.val < node2.val:
                headNode.next = node1
                node1 = node1.next
                headNode = headNode.next
            else:
                headNode.next = node2
                node2 = node2.next
                headNode = headNode.next
        return head.next

s = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
res = s.mergeTwoLists(l1, l2)
print(res)
