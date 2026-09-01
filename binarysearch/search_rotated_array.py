""" There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
"""
nums = [4,5,6,7,0,1,2]

class Solution():
    def search(self, nums, target):
        #binary search
        left = 0
        right = len(nums)-1

        while left<=right:
            #mid ptr
            mid = left+(right-left)//2

            if target == nums[mid]:
                return mid


            #check left array
            if nums[left] <= nums[mid]:
                #check if target in between this interval
                if nums[left] <= target <= nums[mid]:
                    #move right ptr
                    right = mid-1
                else: #means the target is in the right sorted array.
                    left = mid+1
            else: #in right sorted array

                #check if target in between mid and right
                if nums[mid] <= target <= nums[right]:
                    #move left ptr
                    left = mid+1
                else:
                    right = mid-1 #in left half
        return -1

sol = Solution()
print(sol.search(nums, 4)) #should be 0
print('\n')
print(sol.search(nums, 3)) #should be -1
print('\n')
print(sol.search(nums, 7)) #should be 3
 