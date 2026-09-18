""" 
Code
Testcase
Testcase
Test Result
75. Sort Colors
Attempted
Medium
Topics
premium lock icon
Companies
Hint
You are given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function. 

Input: nums = [2,0,2,1,1,0]

Output: [0,0,1,1,2,2]

Explanation:

The array has two 0s, two 1s, and two 2s. Sorting them in-place places all 0s first, then all 1s, then all 2s.


"""
nums = [2,0,2,1,1,0]
class Solution():
    def sortColors(self, nums): #i solved this using merge sort but thats not in place, so its technically cheating.def
        #do quicksort
        def quicksort(arr, left, right):
            if left < right:
                #we need the pivot index
                pi = partition(arr, left, right)

                #quicksort on the left and right subarrays
                quicksort(arr, left, pi-1)
                quicksort(arr, pi+1, right)
            return arr  

        def partition(arr, left, right):
            i = left
            j = right-1
            pivot = arr[right]
            
            while i < j:
                while i < right and arr[i]<pivot:
                    #we just move i
                    i+=1
                while j > left and arr[j] >= pivot:
                    j-=1
                
                if i < j:
                    #swap the values and move the ptrs
                    arr[i], arr[j] = arr[j], arr[i]
                    i+=1
                    j-=1
            
            if arr[i] > pivot:
                #we just swap the values
                arr[i], arr[right] = arr[right], arr[i]
            return i



        return quicksort(nums, 0, len(nums)-1)
sol = Solution()
print(sol.sortColors(nums))