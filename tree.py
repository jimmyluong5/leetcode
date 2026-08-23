import roman_to_integer
class TreeNode():
    def __init__(self, val, left = None, right = None):
        self.left = left
        self.right = right
        self.val = val

def __str__(self):
    return str(self.val)

#create the nodes
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

print(A)

