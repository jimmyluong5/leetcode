""" Given an integer array nums and an integer k, 
return true if there are two distinct indices i and j 
in the array such that nums[i] == nums[j] and abs(i - j) <= k. """

nums = [1,2,3,1]
k =3

class Solution():
    def containsDuplicate(self, nums, k):
        #create the hashset
        window = set()
        left = 0
        
        #loop through the array
        for right in range(len(nums)):
            #we need to check the window size 
            if right - left > k:
                #adjust the window size
                window.remove(nums[left])
                
                #move left pointer
                left+=1
            
            #check if we have seen the duplicate before
            if nums[right] in window:
                return True
            #else we need to add it to the window
            window.add(nums[right])
        return False

sol = Solution()
print(sol.containsDuplicate(nums, k))




nums1 = [1,2,3,1,2,3]
k1=2

#this is solution 2 using hashmap
class Solution2():
    def containsDup(self, nums, k):
        #create the hashmap
        map = {}
        
        #loop through the array
        for i, num in enumerate(nums):
            if num in map and i-map[num] <=k:
                return True
            #else we just add it to teh hashmap
            map[num] = i
        return False
print('\n')
sol2=Solution2()
print(sol2.containsDup(nums1, k1))
