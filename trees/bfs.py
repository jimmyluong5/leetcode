import collections

class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
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

C.left = None
C.right = None
D.left = None
D.right = None

B.left = E
B.right = F

E.left = None
E.right = None

class Solution():
    def bfs(self, root):
        #create the result
        res = []
        if root == None:
            return res

        #create the queue
        queue = collections.deque()

        #import the root
        queue.append(root)

        #then we need to iterate through the queue while its not empty
        while queue:
            #then just pop the left of the queue and add it to the result
            node = queue.popleft()

            #print the value or add it to the result, or do something here at the node.
            #print(node.val)
            res.append(node.val)

            #check the left
            if node.left:
                #add to the queue
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        #then after we just return res
        return res
sol = Solution()
print(sol.bfs(root))
