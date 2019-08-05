# -*- coding: utf-8 -*-

'''Details of Requirement'''
"""
/**
 * 1.Apply a Array(support dynamic expansion)
 * 2.Apply a Linked List
 * 3.Test(Basic Algorithm)
 *  3.1.Three Sum
 *  3.2.Majority Element
 *  3.3.Missing Positive
 *  3.4.Linked List Cycle I
 *  3.5.Merge k Sorted Lists
 */
"""

# Array(support dynamic expansion)
## 1.Merge Two arrays into One
## 2.Ordered arrays with fixed size & Dynamic ADMS(Addition, Deletion, Modification, Search)
## 3.Hash Thought & Test
Class t1_array(list):
    '''define'''
    def __init__(self,*args,size=None,fixed=False):
        # fixed or not
        if not isinstance(fixed, bool) and fixed:
            raise TypeError("Fixed size must be bool")
        self._fixed = fixed
        
        # data
        if args:
            self._data = [i for i in args]          # list stored
            if self._fixed:
                if not size:
                    raise IOError("While array length is fixed, size not be none")
                else:
                    if not isinstance(size, int):
                        raise TypeError("List length must be integer")
                    self._size = size
                    self.is_empty = False
                    none_data = [None] * (self._size - len(self._data))
                    self._data += none_data
        else:
            if size:
                if not isinstance(size, int):
                    raise TypeError("List length must be integer")
                self._size = size
                self.is_empty = False
                self._data = [None] * self._size
            else:
                self._size = 0
                self.is_empty = True
                self._data = []
                
                
    def __str__(self):
        str_res = """
        Array: {array}
            empty: {empty}
            length: {length}
        """.format(array=self._data, empty=self.is_empty, length=self._size)
        return str_res
    
    
    def insert(self, index, value):
        """
        if the array is empty, the data will be still insert, and index is 0
        :param index: insert index, must be integer
        :param value: insert data
        :return:
        """
        if not isinstance(index, int):
            raise TypeError("Index must be integer")
        if self.is_empty:
            if self._fixed:
                self._data = [None] + self._data[1:]
            else:
                self._data = [value]
                self.is_empty = False
                self._size += 1
        else:
            if not self._size > index:
                raise IndexError("Index be not more than array length")
            else:
                if self._fixed:
                    self._data = self._data[:index] + [value] + self._data[index: -1]
                else:
                    self._data = self._data[:index] + [value] + self._data[index:]
                    self._size += 1
                    
                    
    def append(self, value, sorted=False):
        if self._fixed:
            raise IOError("The array length is fixed, you need to use insert")
        else:
            if isinstance(value, list):
                if not sorted:
                    self._data += value
                else:
                    self._data += value
                    self._data.sort()
                self._size += len(value)
                self.is_empty = False
            else:
                if self.is_empty:
                    self._data = [value]
                    self.is_empty = False
                    self._size += 1
                else:
                    self._data += [value]
                    self._size += 1
                    
                    
    def delete(self, index):
        """
        :param index:
        :return:
        """
        if not isinstance(index, int):
            raise TypeError("Index must be integer")
        if self.is_empty:
            raise IOError("The array is empty")
        else:
            if self._size < index - 1:
                raise IndexError("Index be not more than array length")
            else:
                self._data = self._data[:index] + self._data[index + 1:]
                if self._fixed:
                    self._data += [None]
                else:
                    self._size -= 1

    def pop(self, index=None):
        """

        :param index:
        :return:
        """
        if index:
            if not isinstance(index, int):
                raise TypeError("Index must be integer")
            if self.is_empty:
                raise IOError("The array is empty")
            else:
                if not self._size > index:
                    raise IndexError("Index be not more than array length")
                else:
                    self._data = self._data[:index] + self._data[index + 1:]
                    if self._fixed:
                        self._data += [None]
                    else:
                        self._size -= 1
        else:
            if self.is_empty:
                raise IOError("The array is empty")
            else:
                if self._size == 1:
                    if self._fixed:
                        self._data = [None]
                    else:
                        self._data = []
                        self._size = 0
                        self.is_empty = True
                else:
                    self._data = self._data[1:]
                    if self._fixed:
                        self._data += [None]
                    else:
                        self._size -= 1
                        
                        
    def update(self, index, value):
        if not isinstance(index, int):
            raise TypeError("Index must be integer")
        if self.is_empty:
            raise IOError("The array is empty")
        else:
            if not self._size > index:
                raise IndexError("Index be not more than array length")
            else:
                self._data = self._data[:index] + [value] + self._data[index + 1:]
                
                
# Linked List
## 1.Single, Circle, Two-Way(support AD)
## 2.Single Linked List Reversal
## 3.Merge two Linked List into one
## 4.Search the MID node of Linked List
    Class t1_linked_list():
        def __init__(self, nodes, *args):
            pass
        
        
        def append(self):
            pass
        
        def delete(self):
            pass
        
        def reverse(self):
            pass
        
        def mid(self):
            pass

