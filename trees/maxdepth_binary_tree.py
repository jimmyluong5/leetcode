""" Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node. """
class TreeNode():
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution():
    def maxDepth(self, root):
        if root==None:
            return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))

from collections import deque

def print_tree(root):
    if not root:
        print([])
        return
    queue = deque([root])
    res = []
    while queue:
        node = queue.popleft()
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)
    while res and res[-1] is None:
        res.pop()
    print(res)

# Test Tree:
#       3
#      / \
#     9  20
#       /  \
#      15   7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print("Tree (Level order):")
print_tree(root)

sol = Solution()
depth = sol.maxDepth(root)
print(f"Maximum Depth: {depth}")
