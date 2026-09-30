""" Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, 
each group of children is separated by the null value (See examples) """

""" Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]] """

import collections
class Node():
    def __init__(self, val = 0, children = None):
        self.val = val
        self.children = children


#create the tree
root = Node(1)
A = Node(3)
B = Node(2)
C = Node(4)
D = Node(5)
E = Node(6)

root.children = [A, B, C]
A.children = [D,E]
B.children = []
C.children = []
D.children = []
E.children = []

class Solution():
    def levelOrder(self, root):
        res = []
        if root == None:
            return res
        
        #create the queue
        queue = collections.deque()

        #append the root to the queue
        queue.append(root)

        #loop through the queue while its not empty
        while queue:
            #create the sublist for each level
            level = []

            #loop through each level of the tree
            for i in range(len(queue)):
                #pop the left most node and add it to the sublist
                node = queue.popleft()
                #add it to the sublist
                level.append(node.val)

                #then we need to loop thorugh all the children 
                for child in node.children:
                    #add the children to the queue
                    queue.append(child)
            #we need to combine the sublists
            res.append(level)
        return res
sol = Solution()
print(sol.levelOrder(root))
