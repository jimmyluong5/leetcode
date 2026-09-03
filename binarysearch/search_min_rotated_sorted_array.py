""" Find Minimum in Rotated Sorted Array
Medium
Topics
Company Tags
Hints
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Example 1:

Input: nums = [3,4,5,6,1,2]

Output: 1
Example 2:

Input: nums = [4,5,0,1,2,3]

Output: 0 """
nums = [4,5,0,1,2,3] #0

nums1 = [3,4,5,6,1,2] #1
class Solution():
    def search(self, nums):
        left = 0
        right = len(nums)-1
        min_val = 0
        while left<=right:
            #edge case if the array is size 1
            if left == right:
                return nums[left]
            
            #calc mid
            mid = left+(right-left)//2

            #if left val less than right return it
            if nums[left] < nums[right]:
                return nums[left]
            else:
                #two cases, small value either on mid or left of mid or right of mid
                if nums[mid] < nums[right]:
                    #check on the left of mid
                    min_val = nums[mid]
                    right = mid
                else: #if nums[mid] is larger than the smallest value must be on the right of nums mid
                        #so we move our searching space.
                    left = mid+1
        return min_val
sol = Solution()
print(sol.search(nums))
print('\n')
print(sol.search(nums1))


