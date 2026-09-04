import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canfinish(rate):

            time = h

            for item in piles:
                x = math.ceil(item/rate)
                time -= x

            return time >= 0


        left, right = min(piles), max(piles)

        while left <= right:
            
            mid = left + (right - left)//2 

            if canfinish(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
            




    

        

        