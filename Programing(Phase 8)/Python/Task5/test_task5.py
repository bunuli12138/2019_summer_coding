# -*- coding: utf-8 -*-

'''Invert Binary Tree'''
def invertTree(root):
    if root != None:
        node = root
        node.left, node.right = invertTree(node.right), invertTree(node.left)
    else:
        return None

    return node

'''Maximum Depth of Binary Tree'''
def maxDepth(root):
    if root is None: 
        return 0 
    else: 
        left_height = maxDepth(root.left) 
        right_height = maxDepth(root.right) 
        return max(left_height, right_height) + 1 

'''Validate Binary Search Tree'''


'''Path Sum'''
def hasPathSum(root, sum):
    if not root:
        return False

    sum -= root.val
    if not root.left and not root.right:  # if reach a leaf
        return sum == 0
    return hasPathSum(root.left, sum) or hasPathSum(root.right, sum)