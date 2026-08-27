class Solution:
    def maxProfit(self, prices: List[int]) -> int:



        pointer1 = 0
        pointer2 = 0

        maxprofit = 0

        while pointer2 < len(prices):
            
            current_profit = prices[pointer2] - prices[pointer1]

            maxprofit = max(maxprofit, current_profit)

            if prices[pointer2] < prices[pointer1]:
                pointer1 = pointer2
            
            pointer2 += 1

        return maxprofit
        