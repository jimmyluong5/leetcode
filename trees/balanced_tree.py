""" Given a binary tree, return true if it is height-balanced and false otherwise.

A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1. """

""" Input: root = [3,9,20,null,null,15,7]
Output: true """

class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(3)
A = TreeNode(9)
B = TreeNode(20)
C = TreeNode(15)
D = TreeNode(7)

root.left = A
root.right = B

A.left = None
A.right = None

B.left = C
B.right = D

C.left = None
C.right = None

D.left = None
D.right = None


class Solution():
    def isBalanced(self, root):
        #base case
        if root == None:
            return True

        #res
        self.res = True

        #helper dfs
        def dfs(curr):
            if curr == None:
                return 0

            leftHeight = dfs(curr.left)
            rightHeight = dfs(curr.right)
            if (abs(leftHeight-rightHeight) > 1):
                self.res = False
            
            return 1+max(leftHeight,rightHeight)
        
        dfs(root)
        return self.res

sol=Solution()
print(sol.isBalanced(root))