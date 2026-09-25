""" Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value. """

class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left= left
        self.right = right



class Solution():
    def isSameTree(self, x, y):
        #if the roots are both Null
        if x==None and y == None:
            return True
        if x==None or y==None:
            return False
        if x.val !=y.val:
            return False
        
        #then we return the logical and between going down the left and right subtrees
        return self.isSameTree(x.left, y.left) and self.isSameTree(x.right, y.right)
    
        