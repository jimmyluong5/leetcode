""" Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value. """

class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left= left
        self.right = right



class Solution():
    def isSameTree(self, x, y):
        #if the roots are both Null
        if x==None and y == None:
            return True
        if x==None or y==None:
            return False
        if x.val !=y.val:
            return False
        
        #then we return the logical and between going down the left and right subtrees
        return self.isSameTree(x.left, y.left) and self.isSameTree(x.right, y.right)


def print_inorder(root):
    res = []
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        res.append(node.val)
        inorder(node.right)
    inorder(root)
    print(res)


# Example 1: Same trees
# Tree 1:       1          Tree 2:       1
#              / \                      / \
#             2   3                    2   3
p1 = TreeNode(1, TreeNode(2), TreeNode(3))
q1 = TreeNode(1, TreeNode(2), TreeNode(3))

print("--- Test Case 1 ---")
print("Tree p1 (In-order):")
print_inorder(p1)
print("Tree q1 (In-order):")
print_inorder(q1)

sol = Solution()
result1 = sol.isSameTree(p1, q1)
print(f"Are p1 and q1 the same tree? -> {result1}\n")


# Example 2: Different trees
# Tree 3:       1          Tree 4:       1
#              /                          \
#             2                            2
p2 = TreeNode(1, TreeNode(2), None)
q2 = TreeNode(1, None, TreeNode(2))

print("--- Test Case 2 ---")
print("Tree p2 (In-order):")
print_inorder(p2)
print("Tree q2 (In-order):")
print_inorder(q2)

result2 = sol.isSameTree(p2, q2)
print(f"Are p2 and q2 the same tree? -> {result2}")
