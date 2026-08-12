""" Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9) """

""" Input: s = "Was it a car or a cat I saw?"

Output: true """
s = 'Lebron@James !!!!! @@'
s1 = 'race @car!'
class Solution:
    def isPalindrome(self, s):
        #we use the two pointer approach again but non-alpha characters don't count and 
        #we must be aware of the uppercase and lowercase letters

        #first we turn the string lowercase
        s = s.lower()

        #then we remove all the spaces and non-alpha characters
        s = ''.join(char for char in s if char.isalnum()) #this reads 
        #we do a for loop in the string using the iterating variable char, 
        #then we check if char is alphanumeric and if it is we add it to the string
        #so s at the end should only be alphanumeric

        #now we can do the two pointer approach

        left = 0
        right = len(s)-1

        while left < right:
            
            if (s[left] != s[right]):
                return False
            
            left +=1
            right -=1
        return True

sol = Solution()
print(sol.isPalindrome(s))
print(sol.isPalindrome(s1))






        