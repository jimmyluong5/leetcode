#create the linked list definition

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

head = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1 #this makes it a cycle - 

#create the solution class
class Solution():
    def hasCycle(self, head):
        
        #we need to have a fast and slow ptr
        slow = head
        fast = head
        while fast and fast.next != None:
            #move the slow ptr 1 spot
            #move the fast ptr 2 spots

            slow = slow.next
            fast = fast.next

            #if the fast and the slow ptrs are on the same spot or have the same memory address
            #return True
            if slow == fast:
                return True
        return False


sol = Solution()
print(sol.hasCycle(head))
