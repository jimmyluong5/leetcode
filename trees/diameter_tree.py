""" The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.

The length of a path between two nodes in a binary tree is the number of edges between the nodes. Note that the path can not include the same node twice.

Given the root of a binary tree root, return the diameter of the tree. """



class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right






class Solution():
    def diameterOfBinaryTree(self, root):
        #create global variable
        self.max_diameter = 0
        
        #create the dfs function
        def dfs(curr):
            if curr == None:
                return 0
            #get the left and right heights
            leftHeight = dfs(curr.left)
            rightHeight = dfs(curr.right)

            #determine the diameter
            diameter = leftHeight + rightHeight

            #determine the max diameter
            self.max_diameter = max(self.max_diameter, diameter)

            return 1+max(leftHeight, rightHeight)

        dfs(root)
        return self.max_diameter

sol=Solution()


