""" Remove Nth Node From End of List
Medium
Topics
Company Tags
Hints
Given the head of a linked list and an integer n, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4], n = 2

Output: [1,2,4]
Example 2:

Input: head = [5], n = 1

Output: []
Example 3:

Input: head = [1,2], n = 2

Output: [2] """

class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    

#create the linked lists
def create_linked_list(arr):
    dummy = ListNode()
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr=curr.next
    return dummy.next


class Solution():
    def removeNthFromEnd(self, head, n):
        #we need to create a dummy node for LL to take care of the edge cases
        #where we need to do anything with the head node.
        dummy = ListNode(0, head)
        #set the left pointer to dummy
        left = dummy
        right = head

        #move the right pointer n steps ahead of left
        for i in range(n):
            right=right.next
        
        #then we need to move both pointers
        while right:
            right=right.next
            left=left.next
        left.next=left.next.next
        return dummy.next
sol = Solution()
head = create_linked_list([1,2,3,4])
curr = sol.removeNthFromEnd(head, 2)
while curr:
    print(curr.val)
    curr=curr.next
    #should get 1,2,4


