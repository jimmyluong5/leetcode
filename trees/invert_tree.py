""" 226. Invert Binary Tree
Solved
Easy
Topics
premium lock icon
Companies
Given the root of a binary tree, invert the tree, and return its root. """

class TreeNode():
    def __init__(self, val = 0, left= None, right=None):
        self.val = val
        self.left=left
        self.right=right

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)
G = TreeNode(11)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G



class Solution():
    def invertTree(self, root):
        #base case
        if root == None:
            return None
        
        #swap the right and left child then recursively do that
        temp=root.left
        root.left=root.right
        root.right=temp
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

from collections import deque

def print_tree(root):
    if not root:
        print([])
        return
    queue = deque([root])
    res = []
    while queue:
        node = queue.popleft()
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)
    while res and res[-1] is None:
        res.pop()
    print(res)

print("Before inversion:")
print_tree(A)

sol = Solution()
inverted_root = sol.invertTree(A)

print("After inversion:")
print_tree(inverted_root)
