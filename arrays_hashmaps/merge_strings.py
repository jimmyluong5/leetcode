""" Merge Strings Alternately
Easy
Topics
Company Tags
You are given two strings, word1 and word2. Construct a new string by merging them in alternating order, starting with word1 — take one character from word1, then one from word2, and repeat this process.

If one string is longer than the other, append the remaining characters from the longer string to the end of the merged result.

Return the final merged string.

Example 1:

Input: word1 = "abc", word2 = "xyz"

Output: "axbycz"
Example 2:

Input: word1 = "ab", word2 = "abbxxc"

Output: "aabbbxxc" """

word1= "abc"
word2= "xyz"
class Solution():
    def mergeStrings(self, word1: str, word2: str):
        #initialize the pointers at the start of each string
        p1 = 0
        p2 = 0
        p = 0

        #calculate the sizes of the strings
        n1 = len(word1)
        n2 = len(word2)

        #result string
        res =" " * (n1+n2)

        #turn res into a list
        res = list(res)

        while p1 < n1 and p2 < n2:
            #just attach each character of each string to the result and move the ptrs
            res[p] = word1[p1]
            p1+=1
            p+=1

            res[p] = word2[p2]
            p2+=1
            p+=1
        
        #if p1 == n1, string1 is smaller than string 2

        if p1 == n1 and p2<n2:
            while p2<n2:
                res[p] = word2[p2]
                p2+=1
                p+=1
        
        #string 2 is smaller so p2 ==n2
        if p2==n2 and p1<n1:
            while p1<n1:
                res[p] = word1[p1]
                p1+=1
                p+=1
        
        #turn res back from a list to a string
        res ="".join(res)
        return res
sol = Solution()
print(sol.mergeStrings(word1,word2))



#you can do it without the if statements
class solution1:
    def mergestrings(self, word1, word2):
        #determine the lengths of the strings
        n = len(word1)
        m = len(word2)

        #create the result string
        res = " " * (m+n)

        #turn string into array
        res = list(res)

        #initialize ptrs
        i, j, k  = 0, 0, 0
        while i < n and j < m:
            #just append the characters one by one and move the k ptr
            res[k] = word1[i]
            k+=1
            i+=1

            res[k] = word2[j]
            k+=1
            j+=1
        
        #if one of the strings hit the length
        while i == n and j < m:
            res[k] = word2[j]
            k+=1
            j+=1
        while j == m  and i < n:
            res[k]= word1[i]
            k+=1
            i+=1
        
        #turn the result back into string
        res = "".join(res)
        return res
print("\n")

sol2 = solution1()
print(sol2.mergestrings(word1, word2))