""" Given the head of a linked list, rotate the list to the right by k places. """
from decimal import HAVE_THREADS
class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
""" head = [1,2,3,4,5] 
Output: [4,5,1,2,3"""


head = ListNode(1)
A = ListNode(2)
B = ListNode(3)
C = ListNode(4)
D = ListNode(5)
head.next = A
A.next = B
B.next = C
C.next = D
D.next = None


class Solution(object):
    def rotateList(self, head, k):
        if head == None:
            return head
        
        #create dummy node
        dummy = ListNode(-1, head)

        #then the pointers
        fast = head
        tail = head

        #we need to determine the length of the linked list
        length = 1
        while tail.next:
            tail=tail.next
            length+=1
        
        #calculate k
        k = k % length
        if k == 0:
            return head
        #then we need to place the fast pointer to the node before k
        for i in range(length-k-1):
            fast=fast.next
        
        #then we need to attach the last node to the front
        tail.next=head
        #then attach dummy.next to the head of that which is fast.next
        dummy.next = fast.next

        #then cut off 
        fast.next = None
        return dummy.next

sol = Solution()
curr = sol.rotateList(head, 4)
while curr:
    print(curr.val)
    curr=curr.next



