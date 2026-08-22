""" You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,5]

Output: [1,1,2,3,4,5]
Example 2:

Input: list1 = [], list2 = [1,2]

Output: [1,2] """

# create node class
class node():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # String representation for printing the linked list
    def __repr__(self):
        vals = []
        curr = self
        while curr:
            vals.append(str(curr.val))
            curr = curr.next
        return "[" + ", ".join(vals) + "]"

# Helper function to build a linked list from a Python list
def build_linked_list(arr):
    if not arr:
        return None
    dummy = node()
    curr = dummy
    for val in arr:
        curr.next = node(val)
        curr = curr.next
    return dummy.next

class Solution():
    def merge(self, list1, list2):
        # list1 and list2 are head nodes of linked lists
        p1 = list1
        p2 = list2

        # create dummy node
        dummy = node()
        curr = dummy # automatically has value 0 and next None
        
        # compare node values and link nodes
        while p1 and p2:
            if p1.val < p2.val:
                curr.next = p1
                p1 = p1.next
            else: # p2.val <= p1.val
                curr.next = p2
                p2 = p2.next
            curr = curr.next
        
        # link remaining elements if any
        if p1 is None:
            curr.next = p2
        else:
            curr.next = p1

        return dummy.next


# Build input linked lists from Python arrays
list1 = build_linked_list([1, 2, 4])
list2 = build_linked_list([1, 3, 5])

sol = Solution()
print(sol.merge(list1, list2))


