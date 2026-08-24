""" Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 """
 

"""Input: s = "anagram", t = "nagaram"

Output: true """

s = 'anagram'
t = 'anagram'
class Solution():
    def anagram(self, s, t):
        #check the lengths
        if len(s) != len(t):
            return False
        
        #build the hashmaps
        map1 = {}
        map2 = {}

        for char in s:
            if char in map1:
                map1[char] += 1
            else:
                map1[char] = 1
        
           
        for char in t:
            if char in map2:
                map2[char] +=1
            else:
                map2[char] = 1
    
        return map1==map2 #if true returns True, else False
sol = Solution()
print(sol.anagram(s,t))