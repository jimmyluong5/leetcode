
""" Input: root = [1,2,3,4,5,6,7]

Output: [4,5,2,6,7,3,1] """

class TreeNode():
    def __init__ (self, val = 0, left = None, right = None):
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
    def postorderTraversal(self, root):

        res = []
        def postorder(root):
            if root == None:
                return None
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)
        postorder(root)
        return res

sol=Solution()
print(sol.postorderTraversal(root))        