"""680. Valid Palindrome II
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false """
s = "abca"
s1 = "abaabaabbabbabaaba"
s2="abc"

class Solution():
    def validpalindrome(self, s):
        #create helper function
        def is_pal(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left+=1
                right-=1
            return True
    

        left = 0
        right = len(s)-1
        while left < right:
            if s[left]!=s[right]:
                #delete the left character and determine if right subarray is palindrome
                if is_pal(left+1, right) == True:
                    return True
                elif is_pal(left, right-1):
                    return true
                else: 
                    return False
            #move the pointers
            left+=1
            right-=1
        return True
sol = Solution()
print(sol.validpalindrome(s))
print("\n")
print(sol.validpalindrome(s1))
print("\n")
print(sol.validpalindrome(s2))
