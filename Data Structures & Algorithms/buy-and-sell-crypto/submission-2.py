class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxprofit = 0

        left, right = 0, 1


        while right < len(prices):

            if prices[right] > prices[left]:

                curr = prices[right] - prices[left]
                maxprofit = max(maxprofit, curr)
                right += 1

            else:
                left += 1
                right += 1

        return maxprofit

        





        


        
        