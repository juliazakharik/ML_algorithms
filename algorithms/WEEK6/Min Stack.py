"""
155. Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

"""

class Node:
    def __init__(self, val, next_=None):
        self.val = val
        self.next_ = next_
        
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None
        self.min_ = None
        self.flag = False
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.min_ == None:
            self.min_ = x
        self.head = Node(x, self.head)
        if x < self.min_:
            self.min_ = x
        

    def pop(self):
        """
        :rtype: None
        """
        self.flag = True
        self.head = self.head.next_
        

    def top(self):
        """
        :rtype: int
        """
        return self.head.val
        

    def getMin(self):
        """
        :rtype: int
        """
        if not self.flag:
            return self.min_
        current = self.head
        min_ = self.head.val
        while current:
            if current.val < min_:
                min_ = current.val
            current = current.next_
        return min_
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()




class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = []
        self.min_ = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.min_ == None:
            self.min_ = x
        self.head.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        self.head = self.head[:-1]
        

    def top(self):
        """
        :rtype: int
        """
        return self.head[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.head)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()