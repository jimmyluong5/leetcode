""" Given the head of a linked list and an integer val, remove all the nodes of 
the linked list that has Node.val == val, and return the new head. """

#input is [2,1,4,1,2,3]
#output is [1,4,1,3]

class ListNode():
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

head = ListNode(2)
A = ListNode(1)
B = ListNode(4)
C = ListNode(1)
D = ListNode(2)
E = ListNode(3)
val=2

head.next = A
A.next = B
B.next = C
C.next = D
D.next = E
E.next = None



class Solution():
    def removeElements(self, head, val):
        #create the dummy node
        dummy =ListNode(-1, head)
        curr = dummy
        cn = curr.next
        while curr and cn:
            if cn.val == val:
                cn=cn.next
                curr.next = cn
            else:
                curr = curr.next
                cn = cn.next    
        return dummy.next

sol=Solution()
curr = sol.removeElements(head, val)
while curr:
    print(curr.val)
    curr = curr.next
