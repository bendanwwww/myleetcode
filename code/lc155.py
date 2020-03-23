"""
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。

示例:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

"""

class MinStack(object):

    data = []
    helper = []

    def __init__(self):
        self.data = []
        self.helper = []

    def push(self, x):
        self.data.append(x)
        if len(self.helper) == 0 or self.helper[len(self.helper) - 1] >= x:
            self.helper.append(x)


    def pop(self):
        if self.data[len(self.data) - 1] == self.helper[len(self.helper) - 1]:
            del self.helper[len(self.helper) - 1]
        del self.data[len(self.data) - 1]


    def top(self):
        return self.data[len(self.data) - 1]


    def getMin(self):
        return self.helper[len(self.helper) - 1]



# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(3)
#obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.getMin())
