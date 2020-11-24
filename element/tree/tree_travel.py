class Tree_node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def travel_tree(self, tree_node, res_list):
        if tree_node == None:
            return
        self.travel_tree(tree_node.left, res_list)
        self.travel_tree(tree_node.right, res_list)
        res_list.append(tree_node.val)
        return res_list

    res_list = []
    def find_node_route(self, tree_node, find_node, list):
        if tree_node == None:
            return
        list.append(tree_node.val)
        if tree_node == find_node:
            self.res_list = list
            return
        self.find_node_route(tree_node.left, find_node, list[:])
        self.find_node_route(tree_node.right, find_node, list[:])
        return

s = Solution()
tree_node = Tree_node(5)
tree_node.left = Tree_node(3)
tree_node.right = Tree_node(8)
tree_node.left.left = Tree_node(1)
tree_node.left.right = Tree_node(4)
tree_node.right.left = Tree_node(7)
res = s.travel_tree(tree_node, [])
s.find_node_route(tree_node, tree_node.right.left, [])
print(res)
print(s.res_list)