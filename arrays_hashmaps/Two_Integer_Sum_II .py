""" Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space. """

arr = [1, 2, 3, 4]
class Solution():
    def twosum(self, nums, target):
        #two pointer approach with binary search structure
        left = 0
        right = len(nums)-1
        while left <=right:
            if target>nums[left]+nums[right]:
            #our calculation is too small, move the left ptr up
                left +=1
            elif target < nums[left]+nums[right]:
                #our calculation too large, move right ptr down.
                right-=1

            else:
                #return the indices +1
                return [left+1, right+1]
        return [left+1, right+1]
sol = Solution()
print(sol.twosum(arr, 4)) #should be [1,3]


