#this is textbook dfs
import collections
class ListNode():
    def __init__(self, val = 0, left=None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def bfs(self, root):
        #create the result
        res = []
        if root == None:
            return res
            