# -*- coding: utf-8 -*-
"""
https://github.com/zexuchen93/Data-Structure/blob/master/Array%20and%20list.ipynb
"""

import ctypes
'''dynamic array'''
class DynamicArray:
    def _init_(self):
        # creat an empty array
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
        
    def _len_(self):
        # return number of elements stored in the array
        return self._n
    
    def _getitem_(self, k):
        # return elements at index k
        if k >= 0 and k < self._n:
            return self._A[k]
        
    def append(self, obj):
        # add object to end of the array
        if self._n == self._capacity: # not enough room
            self._resize(2*self._capacity)
            self._A[self._n] = obj
        self._n += 1
        
    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c
        
    def delete(self, obj):
        # if the object is already in the array, it will be removed.
        # otherwise, this function is a no-op
        if obj in self._A:
            self._n -= 1
        idx = self.findIndex(obj)
        for i in range(idx, self._n):
            self.A[i] = self._A[i-1]
            
    def findIndex(self, obj):
        for i in range(self._n):
            if self._A[i] == obj:
                return i
        return None
        
    def insert(self, idx, obj):
        for i in range(idx, self._n):
            self._A[i] = self._A[i+1]
        self._A[k] = obj
        
    
    def _make_array(self, c):
        return (c*ctypes.py_object)()

'''linked list (3 class)'''
class ListNode(object):
    def _int_(self, value):
        self.next = None
        self.val = value
        
class LinkedList(object):
    def _init_(self):
        self.head = None
        
    def print_all_nodes(self, head):
        cur = head
        while cur:
            print cur.val
            cur = cur.next
            
    def search_by_index(self, head, index):
        if not head or index < 0:
            return None
        for i in range(index):
            head = head.next
            if not head:
                return None
        return head
    
    def search_by_value(self, head, val):
        if not head:
            return None
        while head:
            if head.val == val:
                return head
            else:
                if head.next:
                    head = head.next
                else:
                    return None
                
    def add_to_index(self, head, index, value):
        if index == 0:
            new_head = ListNode(value)
            new_head.next = head
            return new_head
        else:
            pre_node = self.search_by_index(index-1)
            if pre_node is None:
                return None
            cur = pre_node.next
            pre_node.next = ListNode(value)
            pre_node.next.next = cur
            return head
        
   # version 2
   def add_to_index(self, head, index, value):
        dummy_node = ListNode(0)
        dummy_node.next = head
        pre_node = self.search_by_index(head, index-1)
        if pre_node is None:
            return 
        cur = pre_node.next
        pre_node.next = ListNode(value)
        pre_node.next.next = cur
        return dummy_node.next
    
class DoublyListNode(object):
    def _init_(self, value):
        self.val = value
        self.prev = None
        self.next = None
        
    def search_by_index(self, head, index):
        if not head or index<0:
            return None
        for i in range(index):
            head = head.next
            if not head:
                return None
        return head
    
    def search_by_val(self, head, val):
        dummy_node = ListNode(0)
        dummy_node.next = head
        while head:
            if head.val == val:
                return head
            head = head.next
        return None
    
    def remove_by_index(self, head, index):
        dummy_node = ListNode(0)
        dummy_node.next = head
        head.prev = dummy_node
        remove_node = self.search_by_index(head, index)
        if remove_node is None:
            return dummy_node.next
        if remove_node.prev is not None:
            remove_node.prev.next = remove_node.next
        if remove_node.next is not None:
            remove_node.next.prev = remove+node.prev
        dummy_node.next.prev = None
        return dummy_node.next
    
    
'''function'''
# reverse a linked list
def reverse(self, node):
    previous_node = None
    while node is not None:
        next_node = node.next
        node.next = previous_node
        previous_node = node
        node = next_node
    return previous_node


# merge two sorted linked lists
def merge(self, l1,l2):
    cur = dummy_node = ListNode(0)
    
    while l1 and l2:
        if l1.val < l2.val:
            dummy_node.next = l1
            l1 = l1.next
        else:
            dummy_node.next = l2
            l2 = l2.next
        dummy_node = dummy_node.next
    if l1:
        dummy_node.next = l1
    if l2:
        dummy_node.next = l2
    return cur.next


# the median of linked list
def median(self, head):
    slow, fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow