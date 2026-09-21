""" Rotate Array
Medium
Topics
Company Tags
You are given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7,8], k = 4

Output: [5,6,7,8,1,2,3,4]
Explanation:
rotate 1 steps to the right: [8,1,2,3,4,5,6,7]
rotate 2 steps to the right: [7,8,1,2,3,4,5,6]
rotate 3 steps to the right: [6,7,8,1,2,3,4,5]
rotate 4 steps to the right: [5,6,7,8,1,2,3,4]

Example 2:

Input: nums = [1000,2,4,-3], k = 2

Output: [4,-3,1000,2]
Explanation:
rotate 1 steps to the right: [-3,1000,2,4]
rotate 2 steps to the right: [4,-3,1000,2]


Constraints:

1 <= nums.length <= 100,000
-(2^31) <= nums[i] <= ((2^31)-1)
0 <= k <= 100,000 """

#this question is actually easy intuitively
#
nums = [1, 2, 3, 4, 5, 6, 7]
nums1 = [1, 2, 3, 4, 5, 6, 7]
class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k%n

        def helper(arr, left, right):
            while left<right:
                #swap
                arr[left], arr[right]=arr[right], arr[left]
                left+=1
                right-=1
            return arr
        
        #we need to swap the array once, then for the first k elements reverse that then reverse from k to n-1
        arr = helper(nums, 0, n-1)
        arr = helper(arr, 0, k-1)
        arr = helper(arr, k, n-1)
        return arr
sol = Solution()
print(sol.rotate(nums, 1))
#should be [7, 1, 2, 3, 4, 5, 6]

print("\n")
print(sol.rotate(nums1, 3)) #if you use the same array, the previous old values will be there
#arrays are mutable in python.
#should be [5,6,7,1,2,3,4]

#another solution would be 
#we do array slicing so we just add the array for the first k elements
#then add the array from the n-k elements which is the rest of the elements thats not first k
#nums[:] = nums[n-k:] + nums[:n-k]
#nums[n-k:] is the last elements
#nums[:n-k] is the first k elements, cuz 0 to n-k which where n-k is the number of the elements left
