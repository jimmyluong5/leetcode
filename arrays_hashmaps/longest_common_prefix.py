""" You are given an array of strings strs. Return the longest common prefix of all the strings.

If there is no longest common prefix, return an empty string "".

Example 1:

Input: strs = ["bat","bag","bank","band"]

Output: "ba"
Example 2:

Input: strs = ["dance","dag","danger","damage"]

Output: "da"
Example 3:

Input: strs = ["neet","feet"]

Output: "" """
strs1 = ["dance","dag","danger","damage"]
strs2 = ['bat', 'bag', 'bank', 'band'] 


class solution():
    def longest_prefix(self, strs):

        #initialize a result string
        result = ""

        #then we need to loop over the first string because all successive strings will contain prefixes
        #if the first string contains the prefix
        for i in range(len(strs[0])):

            #then we need to see if the characters match
            #so create the string s and compare the characters

            for s in strs:
                #we need to return the result if our index is outside the string we made 
                #or if the characters don't match
                if i == len(s) or s[i] != strs[0][i]:
                    #then we need to return the result
                    return result
            
            #if the characters match
            #add the character to the result
            result += strs[0][i]
        
        #return the result
        return result
    
sol = solution()

print(sol.longest_prefix(strs1)) 
print(sol.longest_prefix(strs2))