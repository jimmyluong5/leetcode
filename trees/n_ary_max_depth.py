""" Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples). """


class Node():
    def __init__(self, val = 0, children = None):
        self.val = val
        self.children = children

""" Input: root = [1,null,3,2,4,null,5,6]
Output: 3 """

root = Node(1)
A=Node(3)
B=Node(2)
C=Node(4)
D=Node(5)
E=Node(6)

root.children = [A,B,C]
A.children = [D,E]
B.children = []
C.children = []
D.children = []
E.children = []



class Solution():
    def maxDepth(self, root):
        #base case
        if root == None:
            return 0
        maxHeight = 0
        for child in root.children:
            maxHeight = max(maxHeight, self.maxDepth(child))
        return 1+maxHeight
sol=Solution()
print(sol.maxDepth(root))
