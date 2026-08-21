""" Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 """
""" Input: ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]

Output: [null, null, null, 1, -1, null, 1, null, -1] """


""" Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
  """



#make node

input = ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]

class node():
    def __init__(self, key = -1, val = -1, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap(object):
    #make a hash function that returns the index
    def hash(self, key):
        index = key % len(self.map)
        return index

    def __init__(self):
        self.map = []
        for i in range(1000):
            self.map.append(node())

    def put(self, key, value):
        #get the index
        index = self.hash(key)
        curr = self.map[index]
        #then compare the key values
        #if the same then we need to override the values
        while curr.next != None:
            if curr.next.key == key:
                curr.next.val = value
                return
            #else move the ptr 
            curr = curr.next

        #else add the node to the dangling pointer
        curr.next = node(key, value)

    def get(self, key):
        index = self.hash(key)
        curr = self.map[index]

        #traverse the nodes
        while curr!=None:
            if curr.key == key:
                return curr.val
            #else move the ptrs
            curr = curr.next
        return -1
        

    def remove(self, key):
        #index
        index = self.hash(key)
        curr = self.map[index]

        while curr.next != None:
            if curr.next.key == key:
                curr.next = curr.next.next
                return 
            #move the ptr
            curr = curr.next



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
sol = MyHashMap()
sol.put(1,1)
sol.put(2,2)
print(sol.get(1))
print(sol.get(3)) 
