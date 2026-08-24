""" Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2 """

nums = [2, 2, 1, 1, 1, 1, 2, 3]
n = len(nums)
class Solution:
    def majorityElement(self, nums):
        #create hashmap
        map = {}

        #loop through the nums array
        for num in nums:
            if num in map:
                if map[num] == n//2:
                    return num
                else:
                    #increase the frequency
                    map[num] +=1
            else:
                #add the number to the hashmap
                map[num] = 1
        return num
sol = Solution()

print(sol.majorityElement(nums))

            