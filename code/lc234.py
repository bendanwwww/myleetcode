"""
请判断一个链表是否为回文链表。

示例 1:
输入: 1->2
输出: false

示例 2:
输入: 1->2->2->1
输出: true

进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    # first = None
    # res = True
    #
    # def isPalindrome(self, head):
    #     self.first = head
    #     self.find(head)
    #     return self.res
    #
    # def find(self, node):
    #     if node is None:
    #         return
    #     self.find(node.next)
    #     if self.first.val != node.val:
    #         self.res = False
    #     else:
    #         self.first = self.first.next

    def isPalindrome(self, head):
        if head is None:
            return True
        # 快慢指针寻找中间节点
        slow = head
        fast = head
        slowlast = head
        while fast is not None:
            slowlast = slow
            slow = slow.next
            if fast.next is None or fast.next.next is None:
                break
            else:
                fast = fast.next.next
        # 翻转链表
        slowlast.next = None
        last = None
        while slow is not None:
            tmp = slow.next
            slow.next = last
            last = slow
            slow = tmp
        slow = last
        # 比较两个链表
        res = True
        first = head
        firstLast = head
        last = slow
        while last is not None:
            if last.val != first.val:
                res = False
                break
            firstLast = first
            first = first.next
            last = last.next

        # 恢复链表
        if first is None:
            first = firstLast
        last = None
        while slow is not None:
            tmp = slow.next
            slow.next = last
            last = slow
            slow = tmp
        slow = last
        first.next = slow
        return res

s = Solution()
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(1)
head.next.next.next = ListNode(1)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(2)
# head.next.next.next.next = ListNode(1)
res = s.isPalindrome(head)
print(res)
