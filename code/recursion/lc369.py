"""
用一个 非空 单链表来表示一个非负整数，然后将这个整数加一。
你可以假设这个整数除了 0 本身，没有任何前导的 0。
这个整数的各个数位按照 高位在链表头部、低位在链表尾部 的顺序排列。

示例:
输入: [1,2,3]
输出: [1,2,4]

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def to_string(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next

class Solution(object):
    def plusOne(self, head):
        self.plus(head)
        if head.val == 0:
            head_new = ListNode(1)
            head_new.next = head
            head = head_new
        return head

    def plus(self, node):
        if node == None:
            return True
        if self.plus(node.next):
            node.val += 1
            if node.val == 10:
                node.val = 0
                return True
            else:
                return False

s = Solution()
head = ListNode(9)
head.next = ListNode(9)
head.next.next = ListNode(9)
res = s.plusOne(head)
res.to_string()
