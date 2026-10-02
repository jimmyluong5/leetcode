""" Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type. """

s = "()[]{}"
s1 = "([{}])"
#Output: true for both.
class Solution(object):
    def isValid(self, string):
        #check if odd
        if len(string)%2 !=0:
            return False

        #create stack
        stack = []

        #loop through array
        for char in string:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                #check if stack is empty
                if stack == []:
                    return False

                #then we need to check the closed brackets with the top of the stack
                if char == ']' and stack[-1] == '[':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                elif char == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    #mismatch brackets
                    return False
        return len(stack) == 0
sol = Solution()
print(sol.isValid(s))

print('\n')
print(sol.isValid(s1))




                