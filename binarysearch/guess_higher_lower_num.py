""" We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked. 

Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1"""
# Dummy guess API implementation for local testing
PICK = 1
def guess(num):
    if num > PICK:
        return -1
    elif num < PICK:
        return 1
    else:
        return 0

class solution():
    def guess(self, n):
        #do binary search
        left = 1
        right = n

        #from the guess api, if -1 then our guess too high so we move right = mid-1
        # 1 our guess is too low, move left = mid+1
        # 0 our guess is correct return mid
         

        while left <=right:
            mid = left +(right-left)//2

            if guess(mid) == -1:
                right = mid-1
            elif guess(mid) ==1:
                left = mid+1
            else:
                return mid
      

sol = solution()
print(sol.guess(10))

print('\n')
print(sol.guess(1))

            
