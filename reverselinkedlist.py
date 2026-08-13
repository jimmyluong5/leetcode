class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev


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

# 2. Traverse and print original list
print("Original list:")
curr = head
while curr:
    print(curr.val)
    curr = curr.next

# 3. Reverse using Solution class
solution = Solution()
head = solution.reverseList(head)

# 4. Traverse and print reversed list
print("Reversed list:")
curr = head
while curr:
    print(curr.val)
    curr = curr.next
