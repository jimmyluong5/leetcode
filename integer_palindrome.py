#leetcode 7

""" Given an integer x, return true if x is a palindrome, and false otherwise."""
""" Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left. """

""" Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, 
it becomes 121-. Therefore it is not a palindrome.
"""
x = 121
class Solution():
    def isPalindrome(self, x):

    #we know that negative numbers cannot be palindromes so we check for that
        if x<0:
            return False
        
        #now we convert the integer to a string
        s = str(x)

        #then we use the two pointer approach
        l = 0
        r = len(s)-1

        while (l<r):
            #if the characters are not equal to each other return False
            if (s[l] != s[r]):
                print('This number:', x, 'is not a palindrome')
                return False
            
            #else just move both ptrs towards each other
            l +=1
            r -=1
        
        #after the loop has finished we return True and its a palindrome
        print('This number:', x, 'is a palindrome')
        return True

sol = Solution()
print(sol.isPalindrome(121))

print('\n')

print(sol.isPalindrome(100))
#testing 