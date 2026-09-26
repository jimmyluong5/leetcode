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

head = ListNode(1)
A = ListNode(1)
B = ListNode(2) 
head.next = A
A.next = B
B.next = None   



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

    
