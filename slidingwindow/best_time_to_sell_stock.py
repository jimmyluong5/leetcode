""" You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6 """

prices = [10, 1, 5, 6, 7, 1]

class Solution():
    def maxProfit(self, prices):
        #we gonna do sliding window
        #assign a left and right pointer where right is ahead of left
        left = 0 
        right = 1
        max_profit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                #then calculate the profit
                profit = prices[right]-prices[left]
                max_profit = max(max_profit, profit)
            else:
                #move the left pointer to the right pointer, because right is lower than left
                left=right
            #move right pointer
            right +=1
        return max_profit
sol = Solution()
print(sol.maxProfit(prices))