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


#pre-order traversal DFS

def preorder(root):
    #we need a base case so if the root is None then return
    if root == None:
        return 
    else: #we process the node first then go left then right
        print(root)
        preorder(root.left)
        preorder(root.right)

preorder(A)
# 1 2 4 5 3 10 11
print('\n')
#in order traversal dfs
def inorder(root):
    if root == None:
        return
    else: #we go left first then root then right
        inorder(root.left)
        print(root)
        inorder(root.right)
inorder(A) # left then root then right
# 4 2 5 1 10 3 11
print('\n')

#post order traversal 

def postorder(root):
    if root == None:
        return
    else:
        postorder(root.left)
        postorder(root.right)
        print(root)
postorder(A)
#4 2 5 10 11 3 1
