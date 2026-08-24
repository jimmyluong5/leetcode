""" You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity. """
#we finna solve this my way

#which is perform binary search on each row
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

class Solution():
    def search(self, matrix, target):
        #find the length of a row and a col
        n = len(matrix[0])
        m = len(matrix)

        
        for i in range(m):
            #create the left and right pointers
            left = 0
            right = n-1
            while left<=right:
                #create the middle index
                mid = left+(right-left)//2

                #simple binary search.
                if target>matrix[i][mid]:
                    #move the left ptr up
                    left = mid+1
                elif target<matrix[i][mid]:
                    right = mid-1
                else:
                    return True
            return False

sol = Solution()
print(sol.search(matrix,3))

#this is O(m*log(n))
#because the inner while loop is log(n)
#outer for loop is O(m)

