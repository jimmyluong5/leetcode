class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

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


def inorder(root):
    if root is None:
        return
    else:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

print("Tree Before Invert (Inorder Traversal):")
inorder(A)

class Solution(object):
    def invertTree(self, root):
        # Swap left and right children, then recursively invert subtrees
        if root is None:
            return None
        else:
            temp = root.left
            root.left = root.right
            root.right = temp

            #recurse down the left and right
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

sol = Solution()
sol.invertTree(A)

print("\nTree After Invert (Inorder Traversal):")
inorder(A)
