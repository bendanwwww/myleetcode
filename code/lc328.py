"""
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

示例 1:
输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL

示例 2:
输入: 2->1->3->5->6->4->7->NULL
输出: 2->3->6->7->1->5->4->NULL

说明:
应当保持奇数节点和偶数节点的相对顺序。
链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        if head is None:
            return head
        tmpNode = head
        tmpLast = head
        tmpTail = None
        lastHead = None
        lastTail = None
        n = 0;
        while tmpNode is not None:
            if n % 2 == 1:
                if lastHead is None:
                    lastHead = ListNode(tmpNode.val)
                    lastTail = lastHead
                else:
                    lastTail.next = ListNode(tmpNode.val)
                    lastTail = lastTail.next
                tmpLast.next = tmpNode.next
            n+= 1
            if tmpNode.next is None:
                if n % 2 == 0:
                    tmpTail = tmpLast
                else:
                    tmpTail = tmpNode
            tmpLast = tmpNode
            tmpNode = tmpNode.next
        tmpTail.next = lastHead
        return head

s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)
res = s.oddEvenList(head)
print(res)