class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP=0
        buy=0

        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                maxP+=prices[i-1]-prices[buy]
                buy = i
        if buy != len(prices)-1:
            maxP+=prices[-1]-prices[buy]
        return maxP


        # TC: O(N), when N is the number of elements in prices arr.
        # SC: O(1)
