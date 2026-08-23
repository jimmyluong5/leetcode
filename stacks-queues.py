#stacks and queues

#stacks are made of dynamic arrays
#we only care about whats on the top of the stack what is the last index of the stack

#[1, 2, 3, 5] #we can add to the stack by doing stack.append(x)
#follows LIFO, last in first out think as a stack of pancakes

#pop()
#append()

#append is usually O(1) time 
#pop is O(1)
#isEmpty is O(1)
#peek is O(1) - peek is asking whats on the top of the stack.
#we can determine the top of the stack by doing S[-1]

#we use a doubly linked list for queues because we have a ptr at the start and end of the linked lists.
#queues are the opposite of a queue, like a person in a line, 
# the first one in the line is the first one to leave
#FIFO behaviour

#to add to a queue you must add to the end which is the last index
#to leave the queue you must leave from the front

#enqueue is enter
#dequeue is leaving


#coding stacks

stk = [] #empty stack

stk.append(1)
stk.append(2)
print(stk)

#you can pop out of a stack it will pop the last element you just appended
stk.pop()
print(stk)

stk.append(4)
stk.append(8)

#we can ask whats on the stack by doing stk[-1]

print(stk[-1]) #which is 8

from collections import deque
#queues

q = deque()

print(q)

#we can append 
#add elements on the right side of the q
q.append(1)
q.append(2)
q.append(3)

print(q)

q.popleft() #must be popleft, can do pop right but then its not a queue anymore and a stack
print(q)

#peak on the left
print(q[0])

#peak on the right side
print(q[-1])

#use can put anything in stacks and queues, like strings, tuples, dictionaries like anything.