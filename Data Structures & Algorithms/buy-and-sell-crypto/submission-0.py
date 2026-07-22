class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxsofar = 0

        left, right = 0, 1


        while right < len(prices) - 1:


            while price[left] < price[right]:
                maxsofar = max(maxsofar, price[right]-price[left])
                right += 1

            left += 1
            

        
        