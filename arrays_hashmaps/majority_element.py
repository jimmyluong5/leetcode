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

nums = [2, 2, 1, 1, 1, 2, 2]
#if the last element was a 9, the algorithm wouldn't work.

class Solution:
    def majorityElement(self, nums):
        #create hashmap
        map = {}
        n = len(nums)
        #for hashmaps you should always increase the freq first
        #because if the number already exists in the hashmap then 
        #the loop is actually the 2nd iteration
        for num in nums:
            if num in map:
                #increase the frequency
                map[num]+=1

                #check for condition
                if map[num] > n//2:
                    return num
            else:
                #add it to the hashmap
                map[num] = 1
        return num
       
       
sol = Solution()

print(sol.majorityElement(nums))

            