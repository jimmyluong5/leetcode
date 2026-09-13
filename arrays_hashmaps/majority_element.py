""" Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

for hashmap problems always increase the frequency first because 
its actually the 2nd iteration of going in the loop if the number
exists already in the hashmap
 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2 """

nums=[5,5,1,1,1,5,5]

class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        map = {}

        #edge case
        if n == 1:
            return nums[0]
        for num in nums:
            if num in map:
                if map[num] == n//2: #majority element guaranteed to exist so this must be true.
                    return num
                else:
                    #increase the frequency
                    map[num] +=1
            else:
                map[num] = 1
        return num
                    
       
       
sol = Solution()

print(sol.majorityElement(nums))

            