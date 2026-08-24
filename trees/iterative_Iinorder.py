class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(8)
E = TreeNode(14)
F = TreeNode(19)
G = TreeNode(25)

A.left = B
A.right = C

B.left = D
B.right = E

C.left = F
C.right = G


# Constructing example tree:
    #       1
    #      / \
    #     2    3
    #    / \  / \
    #   8 14 19 25 


class Solution():
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #iterative approach to inorder traversal
        #make the resulting array
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                #if the curr pointer is not null then we append the node t19o the call stack
                stack.append(curr)
                #then move the ptr to the left
                curr = curr.left
            #if it is null then we must set the curr ptr to whichever node we want to remove
            curr = stack.pop()
            #then we need to add the value to the resulting array
            res.append(curr.val)
            #then move the ptr to the right
            curr = curr.right
        return res
sol = Solution()
print(sol.inorderTraversal(A))