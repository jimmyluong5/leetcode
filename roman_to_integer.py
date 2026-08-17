""" Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 """


s1 = ['III']
s2 = ['IV'] #4
s3 = ['MCMXCIV'] #1994
class solution():
    def romantoint(self, s):

        #create a hashmap of the translations of the roman characters to integers
        map = {
            'I': 1, 
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        #after that there are 6 cases where we need to check for the subtractive cases
        #IV, IX, XL, XC, CD, CM
        #this means that if a smaller value comes before a larger value we subtract the smaller value from the larger value
        
        # 4, 9, 40, 90, 400, 900

        s = s.replace('IV', 'IIII') #4
        s = s.replace('IX', 'VIIII') #9
        s = s.replace('XL', 'XXXX') #40
        s = s.replace('XC', 'LXXXX') #90
        s = s.replace('CD', 'CCCC') #400
        s = s.replace('CM', 'DCCCC') #900

        #loop through the string and just convert the roman numerals in the string to integer and 
        #just add to the number
        num = 0
        for char in s:
            num += map[char]
        return num

sol=solution()

print(sol.romantoint(s1)) 
print(sol.romantoint(s2)) 
print(sol.romantoint(s3)) 
