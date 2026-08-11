
""" Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first. """


""" 
Input: 
nums = [3,4,5,6], target = 7

Output: [0,1] """

""" Input: nums = [4,5,6], target = 10

Output: [0,2] """
nums = [1, 2, 3, 4, 5, 6, 7]
target = 4
class Solution(object):
    def twoSum(self, nums, target):

        #use a hashmap
        map = {}

        #iterate over the nums array and indices
        for i, n in enumerate(nums):
            #check if the difference between the target and the current number is in the map
            diff = target - n

            #if it is in the map then just return a list of the indices
            if diff in map:
                return [map[diff], i]
            else:
                #its not in the map and we can add it to the hashmap
                map[n] = i
    #not in the array entirely
    print('Not possible')
#create a nod eof SOlution before calling twoSum
sol = Solution()
print(sol.twoSum(nums, 8))        


