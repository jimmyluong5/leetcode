""" Input: root = [1,2,3,4,5,6,7]

Output: [4,2,5,1,6,3,7] """

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
A = TreeNode(2)
B = TreeNode(3)

C = TreeNode(4)
D = TreeNode(5)
E = TreeNode(6)
F = TreeNode(7)

root.left = A
root.right = B

A.left = C
A.right = D

B.left = E
B.right = F







class Solution():
    def inorderTraversal(self, root):
        res = []
        def inorder(root):
            if root == None:
                return None
            
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return res

sol = Solution()
print(sol.inorderTraversal(root))
