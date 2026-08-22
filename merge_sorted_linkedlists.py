""" You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.

Example 1:



Input: list1 = [1,2,4], list2 = [1,3,5]

Output: [1,1,2,3,4,5]
Example 2:

Input: list1 = [], list2 = [1,2]

Output: [1,2] """

#create node class
class node():
    def __init__(self, val = -1, next = None):
        self.val = val
        self.next = next

#list1 and list2 are the heads of list1 and list2
list1= [1, 2, 4]
list2= [1, 3, 5]
class Solution:
    def merge(self, list1, list2):
        #create dummy node and pointers

        p1 = list1
        p2 = list2

        #create dummy node
        dummy = node() #automatically has the value of -1 and next of None
        
        #create curr ptr which helps us link values together
        while p1 and p2:
            if p1.val < p2.val:
                curr.next = p1
                p1 = p1.next
                curr = curr.next

            else: #p2.val<=p1.val
                curr.next = p2
                p2=p2.next
                curr = curr.next
        
        #one of the pointers hit null, based on drawing it out, curr will behind the ptr that hit null

        if p1 == None:
            curr.next = p2
            return dummy.next
    
        if p2 ==None:
            curr.next = p1
            return dummy.next


sol = Solution
print(sol.merge(list1, list2))

