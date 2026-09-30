""" Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level). """


""" Input: root = [1,2,3,4,5,6,7]

Output: [[1],[2,3],[4,5,6,7]] """

from collections import deque

class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    

class Solution():
    def levelOrder(self, root):
        #create the resulting list
        res = []
        if root == None:
            return res
        
        #create the queue.
        queue = collections.deque()

        #append the root
        queue.append(root)

        while queue:
            #create the sublists
            level = []
            #then we loop through each level
            for i in range(len(queue)):
                #then we need to pop the left mode node out the queue then add it to the levels list
                node = queue.popleft()
                level.append(node.val)

                #check the left and right nodes and append them to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            #then we need to combine all the sublists into res
            res.append(level)

        return res
sol=Solution()
print(sol.levelOrder(root))

