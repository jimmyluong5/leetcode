""" You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3] """

class ListNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# 1. Create nodes and link them
head = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(4)
node4 = ListNode(5)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4




class Solution():
#make helper function for the reverse LL shit
    def reverse(self, head):
        curr = head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr=next
        return prev
    def reorderList(self, head):

        
        
        #we need to find the middle pointer
        #and depending on the position of the middle pointer we change what we reverse
        #we always want the first half to be the largest list
        fast = head
        slow = head
        prev = None
        while fast and fast.next:
            fast=fast.next.next
            prev = slow
            slow=slow.next
        
        if fast == None:
            #this is the even case
            #this is where prev.next is the middle pointer
            #assign a temp pointer
            temp = prev.next #this is the of the 2nd linked list

            #cut the link
            prev.next = None
            #reverse the 2nd half of the linked list
            p2 = self.reverse(temp)

        else:
            #fast is not none and slow is our middle, but we need a temp pointer for the head of the 2nd ll
            #this is the odd case
            temp = slow.next
            
            slow.next = None
            p2 = self.reverse(temp)

        
        #now we need to just merge
        dummy = head
        curr = head
        p1 = head
        while p1 and p2:
            p1 = p1.next
            curr.next = p2

            curr = curr.next
            p2=p2.next

            curr.next = p1
            curr=curr.next
        return dummy
sol=Solution()

curr = sol.reorderList(head)
while curr:
    print(curr.val)
    curr=curr.next
    
    #should get 1 5 2 4 3 