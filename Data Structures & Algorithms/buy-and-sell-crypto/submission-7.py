class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxsofar = 0

        left, right = 0, 1


        while right < len(prices) - 1:

            if prices[left] < prices[right]:
                maxsofar = max(maxsofar, prices[right]-prices[left])
            else:
                left = right
            right += 1
            
        return maxsofar