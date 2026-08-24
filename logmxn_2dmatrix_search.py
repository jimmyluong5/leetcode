""" You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity. """
#we finna solve this the most optimal way (O log (mxn))
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]


class Solution():
    def search(self, matrix, target):
        #determine the col and row lengths
        n = len(matrix[0]) #length of a row
        m  = len(matrix) #length of a column

        #we finna turn this 2d array into 1d array
        left = 0
        right = (m*n)-1

        while left<=right:
            #create the middle ptr
            mid = left +(right-left)//2
            #create the row and col indices for matrix[row][col]
            row = mid//m #tells us the row number 6%4 = 1, if 4 or less, then we in the 0th row.
            col = mid%m #tells us how deep we into the row 6%4 = 2 (which is the third column from 0, 1, 2)
            
            if target>matrix[row][col]:
                left = mid+1
            elif target<matrix[row][col]:
                right = mid-1
            else:
                return True
        return False
sol = Solution()
print(sol.search(matrix,3))

