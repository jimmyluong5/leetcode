""" Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

"""

class Solution(object):

    def strStr(self, haystack, needle):
        if len(haystack) == 0 or len(needle) == 0:
            return -1
        
        left= 0
        right=0
        while right < len(haystack):
            if right-left+1 == len(needle):
                if haystack[left:right+1] == needle:
                    return left
                left+=1
            right+=1
        return -1

sol = Solution()
print(sol.strStr("leetcode", "leeto"))

print('\n')
print(sol.strStr("asadsbutsad", "sad"))
