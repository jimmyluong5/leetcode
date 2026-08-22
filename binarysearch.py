""" Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 
 """
nums = [1,2,3,4,5,6,6,8,9,10,14,19,20,21]
class Solution():
    def binary_search(self, nums, target):
        #create ptrs
        left = 0
        right = len(nums)-1

        while left<=right:
            #calculate the middle index
            mid = left + (right-left)//2

            if target > nums[mid]:
                left = mid+1
            elif target < nums[mid]:
                right = mid-1
            else:
                return mid
        return -1

sol = Solution()
print(sol.binary_search(nums,14))
print(sol.binary_search(nums,10))


