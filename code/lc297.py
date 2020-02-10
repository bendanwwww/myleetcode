"""
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

示例: 
你可以将以下二叉树：
    1
   / \
  2   3
     / \
    4   5
序列化为 "[1,2,3,null,null,4,5]"

提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        resArray = []
        queue = []
        queue.append(root)
        while len(queue) > 0:
            node = queue[0]
            del queue[0]
            if node is None:
                resArray.append('null')
            else:
                resArray.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        while len(resArray) > 0:
            n = len(resArray) - 1
            if resArray[n] is not 'null':
                break
            else:
                del resArray[n]
        return '[' + ','.join(map(lambda x: str(x), resArray)) + ']'

    def deserialize(self, data):
        if data is None or data == '[]':
            return None
        index = 0
        nodeArray = data.replace('[', '').replace(']', '').split(',')
        root = TreeNode(nodeArray[index])
        queue = []
        queue.append(root)
        while len(queue) > 0:
            node = queue[0]
            del queue[0]
            if index + 1 >= len(nodeArray) or nodeArray[index + 1] == 'null':
                node.left = None
            else:
                node.left = TreeNode(nodeArray[index + 1])
            if index + 2 >= len(nodeArray) or nodeArray[index + 2] == 'null':
                node.right = None
            else:
                node.right = TreeNode(nodeArray[index + 2])
            index+= 2
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return root

    # def deserialize(self, data):
    #     if data is None or data == '[]':
    #         return None
    #     nodeArray = data.replace('[', '').replace(']', '').split(',')
    #     root = TreeNode(nodeArray[0])
    #     self.deserializeRoot(root, nodeArray, 0)
    #     return root
    #
    # def deserializeRoot(self, node, array, n):
    #     nodeLeft = 2 * n + 1
    #     nodeRight = 2 * n + 2
    #     if nodeLeft < len(array) and array[nodeLeft] != 'null':
    #         node.left = TreeNode(array[nodeLeft])
    #         self.deserializeRoot(node.left, array, nodeLeft)
    #     else:
    #         node.left = None
    #
    #     if nodeRight < len(array) and array[nodeRight] != 'null':
    #         node.right = TreeNode(array[nodeRight])
    #         self.deserializeRoot(node.right, array, nodeRight)
    #     else:
    #         node.right = None


s = Codec()

root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
root.right.left.left = TreeNode(3)
root.right.left.right = TreeNode(1)

res1 = s.serialize(root)
res2 = s.deserialize(res1)
print(res1)
print(res2)