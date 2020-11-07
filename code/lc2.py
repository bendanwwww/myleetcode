"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        index_1 = 1
        index_2 = 1
        head_1 = l1
        head_2 = l2
        first = 0
        second = 0
        while head_1 is not None:
            first = first + head_1.val * index_1
            head_1 = head_1.next
            index_1 = index_1 * 10
        while head_2 is not None:
            second = second + head_2.val * index_2
            head_2 = head_2.next
            index_2 = index_2 * 10
        res = first + second
        index_res = max(index_1, index_2)
        if res < index_res:
            index_res = index_res / 10
        next_res = int(res / index_res)
        next_node = ListNode(next_res)
        res = res - next_res * index_res
        while index_res > 1:
            index_res = index_res / 10
            tmp_res = int(res / index_res)
            tmp_node = ListNode(tmp_res)
            tmp_node.next = next_node
            next_node = tmp_node
            res = res - tmp_res * index_res
        return next_node

s = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
res = s.addTwoNumbers(l1, l2)
print(res)