# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def flip_list(self, head):
        return self.flip_list_recursive(head);

    def flip_list_recursive(self, node):
        if node.next == None:
            return node
        new_head = self.flip_list_recursive(node.next)
        node.next.next = node
        node.next = None
        return new_head

s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
res = s.flip_list(head)
print(res)