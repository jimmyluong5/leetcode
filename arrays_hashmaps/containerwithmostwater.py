""" You are given an integer array heights where heights[i] represents the height of the 
ith bar.You may choose any two bars to form a container. 
Return the maximum amount of water a container can store. 
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49"""

heights = [1,8,6,2,5,4,8,3,7]
class Solution():
    def maxArea(self, heights):
        n=len(heights)
        left=0
        right =n-1
        max_area = 0
        while left<right:
            #we need to find the minHeight
            minHeight = min(heights[left], heights[right])

            if minHeight == heights[left]:
                left+=1
            else:
                right-=1
            
            #calculate the area and max area
            area = minHeight * (right-left+1)
            max_area=max(max_area, area)
        return max_area


sol=Solution()
print(sol.maxArea(heights)) #prints 49



