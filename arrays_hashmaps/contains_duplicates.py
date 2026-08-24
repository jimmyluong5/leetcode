""" Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

  """

""" Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3. """

nums1 = [1, 2, 3, 4]
nums2 = [1, 1, 2, 2, 3, 3, 4, 4, 5]
class Solution:
    def containsDuplicates(self, nums):
        #create a hashmap
        hashmap = {}

        #loop through the numbers array
        for num in nums:

            #check if the numbers we've seen are already in the hashmap
            if num in hashmap:
                #if it is then return True
                return True
            
            #if its not in hashmap we add it to hashmap
            hashmap[num] = 1

        #return false if the loop finishes without finding duplicates.
        return False

sol = Solution()
print(sol.containsDuplicates(nums1))
print('\n')
print(sol.containsDuplicates(nums2))


    