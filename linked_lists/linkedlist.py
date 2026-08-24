#singly linked list

class singlylinkedlist:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

head = singlylinkedlist(1) #head node with a value of 1 contained in the node.

#make the next nodes
node1 = singlylinkedlist(5)
node2 = singlylinkedlist(10)
node3 = singlylinkedlist(15)

#connect the nodes together
head.next = node1
node1.next = node2
node2.next = node3
#node3.next = None not needed

print(head.data) #prints the value contained in the head node

#traverse the list we use a for loop - O(n)
#have a ptr to the head node and just move curr until it reaches None
curr = head
while curr != None:
    print(curr.data)
    curr = curr.next

def print_linkedlist():
    curr = head
    
    while curr != None:
        print(curr.data)
        curr = curr.next

#function to search for the node value
def search(head, target):
    curr = head
    while curr != None:
        if curr.data == target:
            return True
        #move the ptr over to the next node
        curr = curr.next
    return False

print(search(head, 80))
print(search(head, 10))


#function to delete a desired node

def delete_node(head, target):
    #edge cases
    if head is None:
        return None #this is when the linked list is empty, so nothing to delete

    if head.data == target: #this is if the head node is the target to delete
        return head.next
    
    prev = head
    curr = head.next

    while curr != None:
        #need to check if our target is the current node
        if curr.data == target:
            #get access to the node ahead of the one we want to delete
            prev.next = curr.next
            curr = None
            #then we want to make the ptr point to None
      
        else: #move the ptrs
            prev = curr
            curr = curr.next
    return head

print(delete_node(head, 10)) #removed node.

#then we can print all the nodes again
print_linkedlist()
print('\n')


delete_node(head, 1)
print_linkedlist()
print('\n')

delete_node(head,15)
print_linkedlist()

print('\n')
delete_node(head,5)
print_linkedlist()










