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
    def preorderTraversal(self, root):
        #make two stacks
        res = []
        stk = [root] #initialize it with the root 

        #check edge case
        if root == None:
            return []

        while stk: #while its not empty (not while stk!=None, it'll never hit None)
            #we need to pop the first element each time we iterate in the loop, and set
            #curr to the first element in the call stack to pop
            #then we append it to the resulting array
            curr = stk.pop()
            res.append(curr.val)

            #then we look at the right node first add it to the call stack,
            #then look at the left node and add it to the call stack

            if curr.right:
                stk.append(curr.right)
            
            if curr.left:
                stk.append(curr.left)

            #if you draw it out, it makes a lot of sense, like follow the loop logic, the if statements
            #run once each iteration
        return res
sol = Solution()
print(sol.preorderTraversal(A))



    

