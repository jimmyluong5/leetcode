""" Given the head of a sorted linked list, 
delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.
Input: head = [1,1,2]
Output: [1,2]
"""

class ListNode():
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = next
#input: [1,1,2]
#output: [1,2]
head = ListNode(1)
A = ListNode(1)
B = ListNode(2) 
head.next = A
A.next = B
B.next = None   

#input [1,1,2,3,3]
#output [1,2,3]
head1 = ListNode(1)
A = ListNode(1)
B = ListNode(1)
C = ListNode(2)
D = ListNode(3)
E = ListNode(3)

head1.next = A
A.next = B
B.next = C
C.next = D
D.next = E
E.next = None


class Solution():
    def removeDuplicate(self, head):
        #create the dummy node
        dummy = ListNode(-1, head)
        #create the ptrs
        left=head
        right = left
        while left:
            while right is not None and left.val == right.val:
                right =right.next
            left.next=right
            left=left.next
        return dummy.next
sol = Solution()
curr = sol.removeDuplicate(head)
while curr:
    print(curr.val)
    curr=curr.next
print('\n')

curr1=sol.removeDuplicate(head1)
while curr1:
    print(curr1.val)
    curr1=curr1.next

