"""
Stack, Queue, Recursion
"""
from abstractcollection import AbstractCollection    # Abstract Class
from array_linked_list import Node

'''Stack'''
# 1.realize a sequence  Stack with 'array'
# 2.realize a chain Stack with 'linked list'
# *3.realize a forward and backward function of browser

# Abstract Class
class AbstractStack(AbstractCollection):
    """An abstract stack implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        AbstractCollection.__init__(self, sourceCollection)
        
        
# Linked Stack
class t2_linked_stack(AbstractStack):
    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = None
        AbstractStack.__init__(self, sourceCollection)

    # Accessor methods
    def __iter__(self):
        def visitNodes(node):
            """Adds items to tempList from tail to head."""
            if not node is None:
                visitNodes(node.next)
                tempList.append(node.data)
                
        tempList = list()                
        visitNodes(self._items)
        return iter(tempList)

    def peek(self):
        if self.isEmpty():
            raise KeyError("The stack is empty.")
        return self._items.data

    # Mutator methods
    def clear(self):
        self._size = 0
        self._items = None

    def push(self, item):
        self._items = Node(item, self._items)
        self._size += 1

    def pop(self):
        if self.isEmpty():
            raise KeyError("The stack is empty.")
        data = self._items.data
        self._items = self._items.next
        self._size -= 1
        return data

    # Mutator methods
    def add(self, item):
        self.push(item)
    
    
'''Queue'''
# 1.realize a sequence Queue with 'array'
# 2.realize a chain Queue with 'linked list'
# 3.realize a circle Queue
class t2_queue(AbstractCollection):
    """A link-based queue implementation."""
    # Constructor
    def __init__(self, sourceCollection = None):
        self._front = self._rear = None
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __iter__(self):
        pass
    
    def peek(self):
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        return self._front.data

    # Mutator methods
    def clear(self):
        pass
    
    def add(self, item):
        newNode = Node(item, None)
        if self.isEmpty():
            self._front = newNode
        else:
            self._rear.next = newNode
        self._rear = newNode
        self._size += 1

    def pop(self):
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        oldItem = self._front.data
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -= 1
        return oldItem
    
    
'''Recursion'''
# 1.realize Fibonacci sequence
# 2.realize Factorial
# 3.realize full permutation of a set of data
class t2_recursion:
    def fibonacciSeq(self, epoch=5):
        if epoch==1 or epoch==2:
            return 1
        return self.fibonacciSeq(epoch-1)+self.fibonacciSeq(epoch-2)
    
    def factorial(self, n=5):
        if n==1:
            return 1
        return n*self.factorial(n-1)
    
    def fullPermutation(self, params, select):
        return self.factorial(params)/self.factorial(params-select)
    
    
if __name__ == '__main__':
    testRe = t2_recursion()
    assert testRe.fibonacciSeq(9)==34, 'fibonacci sequence is not true'
    assert testRe.factorial(5)==120, 'factorial is not true'
    assert testRe.fullPermutation(5,3)==60, 'fullPermutation is not true%d'%testRe.fullPermutation(5,3)
    print('ALL Recursion functions are right')
