""" Search a 2D Matrix
Medium
Topics
Company Tags
Hints
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

Output: true


"""
matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
class Solution():
    def search(self, matrix, target):
        #find the length of the row and the column
        n = len(matrix[0])
        m = len(matrix) #length of the columns

        #we need to iterate on each row and create the pointers for each row
        for i in range(m):
            #create the left, right pointers
            left = 0
            right = n-1
            
            #binary search
            while left<=right:
                mid = left+(right-left)//2
                if target>matrix[i][mid]:
                    #move the left pointer
                    left = mid+1
                elif target<matrix[i][mid]:
                    right = mid-1
                else:
                    return True
        return False

sol = Solution()
print(sol.search(matrix,2))