"""
你需要从一个包括括号和整数的字符串构建一棵二叉树。
输入的字符串代表一棵二叉树。它包括整数和随后的 0 ，1 或 2 对括号。整数代表根的值，一对括号内表示同样结构的子树。
若存在左子结点，则从左子结点开始构建。

示例：
输入："4(2(3)(1))(6(5))"
输出：返回代表下列二叉树的根节点:

       4
     /   \
    2     6
   / \   /
  3   1 5
 

提示：
输入字符串中只包含 '(', ')', '-' 和 '0' ~ '9' 
空树由 "" 而非"()"表示。

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def str2tree(self, s):
        if len(s) == 0:
            return None
        first_index = 0
        while first_index < len(s) and ((ord(s[first_index]) >= ord('0') and ord(s[first_index]) <= ord('9')) or s[first_index] == '-'):
            first_index += 1
        head = TreeNode(s[:first_index])
        if len(s) == first_index:
            return head
        s = s[first_index:]
        i = self.handle_str(s)
        head.left = self.handle_node(s[1:i])
        if i + 1 < len(s):
            head.right = self.handle_node(s[i + 2:len(s) - 1])
        return head

    def handle_node(self, s):
        first_index = 0
        while first_index < len(s) and ((ord(s[first_index]) >= ord('0') and ord(s[first_index]) <= ord('9')) or s[first_index] == '-'):
            first_index += 1
        node = TreeNode(s[:first_index])
        if len(s) == first_index:
            return node
        s = s[first_index:]
        i = self.handle_str(s)
        node.left = self.handle_node(s[1:i])
        if i + 1 < len(s):
            node.right = self.handle_node(s[i + 2:len(s) - 1])
        return node

    def handle_str(self, s):
        stack = []
        i = 0
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                del stack[len(stack) - 1]
            if len(stack) == 0:
                return i
            i += 1
        return i

s = Solution()
res = s.str2tree("123")
print(res)