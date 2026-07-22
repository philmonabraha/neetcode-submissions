class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxsofar = 0

        left, right = 0, 1


        while right < len(prices) - 1:


            while prices[left] < prices[right]:
                maxsofar = max(maxsofar, prices[right]-prices[left])
                right += 1

            left += 1
            right += 1
            
        return maxsofar