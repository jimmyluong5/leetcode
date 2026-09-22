""" Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5] """
head = [1,2,3,4,5]
left = 2
right = 4

#create the class for the node





class ListNode():
    def __init__(self, val, next = None):
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
    def reverseLL(self, head, left, right):
        #create a dummy node, for all linked list problems
        #dummy node is the strat
        dummy = ListNode(-1, head)
        curr = dummy.next
        leftprev = dummy
        
        #we need to place leftprev at the node before left
        #and in order to do that we need to iterate through the LL
        #left-1 times
        for i in range(left-1):
            leftprev = curr
            curr = curr.next
        
        #now we need to start reversing from left to right
        #the number of iterations is right-left +1 
        prev = None
        #Note that when we reverse it, prev will be the head of the new
        #reversed linked list from left to right, and curr will be at the end past right

        for i in range(right-left+1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr=next

        #curr will sit on the node after right node.

        #the node at left pointer originally needs to point to the last node which is curr      
        leftprev.next.next = curr
        
        #link the left-1 node to the original right node which is now prev
        leftprev.next = prev
        return dummy.next
sol=Solution()
curr = sol.reverseLL(head, left, right)
while curr:
    print(curr.val)
    curr=curr.next
    #should get 1->4->3->2->5

    
