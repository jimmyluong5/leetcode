""" Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples) """

""" Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4] """


class Node():
    def __init__(self, val = 0, children=None):
        self.val = val
        self.children = children

root = Node(1)
A = Node(3)
B = Node(2)
C = Node(4)
D = Node(5)
E = Node(6)

root.children = [A, B, C]
A.children = [D, E]
B.children = []
C.children = []
D.children = []
E.children = []


class Solution():
    def preorder(self, root):
        res = []
        def dfs(node):
            if node == None:
                return 0
            res.append(node.val)
            for child in node.children:
                dfs(child)
        dfs(root)
        return res

sol=Solution()
print(sol.preorder(root))
