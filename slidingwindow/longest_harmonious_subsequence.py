""" We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

 

Example 1:

Input: nums = [1,3,2,2,5,2,3,7]

Output: 5

Explanation:

The longest harmonious subsequence is [3,2,2,2,3]. """

nums = [1,3,2,2,5,2,3,7]
class Solution(object):
    
    def findLHS(self, nums):
    #sort first
        nums.sort()
        #make variables
        left = 0 
        right = 0
        lenSequence = 0
        maxLen = 0
        while right < len(nums):
            diff = nums[right]-nums[left]
            if diff == 1:
                lenSequence = right-left+1
                maxLen = max(maxLen, lenSequence)
            if diff > 1:
                left+=1
                lenSequence = right-left+1
            else:
                right+=1
        return maxLen
sol=Solution()
print(sol.findLHS(nums))
