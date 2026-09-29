""" Input: root = [1,2,3,4,5,6,7]

Output: [1,2,4,5,3,6,7] """


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

    def preorderTraversal(self, root):

        res = []
        def preorder(root):
            if root == None:
                return None
            
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        return res
sol=Solution()
print(sol.preorderTraversal(root))
