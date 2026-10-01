""" You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k 
that has the maximum average value and return this value. 
Any answer with a calculation error less than 10-5 will be accepted. """


""" Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000 """
nums = [1,12,-5,-6,50,3]
k = 4

class Solution(object):
    def findMaxAverage(self, nums, k):
        left = 0
        maxSum = -float('inf')
        sum = 0
        for right in range(len(nums)):
            sum+=nums[right]
            if right-left+1 > k:
                sum-=nums[left]
                left+=1
            if right-left + 1 == k:
                maxSum = max(maxSum, sum)
        
        return float(maxSum)/k

sol=Solution()
print(sol.findMaxAverage(nums, k))



