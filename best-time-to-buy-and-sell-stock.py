class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP=0
        buy=0

        for i in range(len(prices)):
            if prices[i] < prices[buy]:
                buy = i
            if prices[i] - prices[buy] > maxP:
                maxP = prices[i]-prices[buy]
    
        return maxP

        # O(N) Time complexity, when n is the number of elements in prices.
        # O(1) Space