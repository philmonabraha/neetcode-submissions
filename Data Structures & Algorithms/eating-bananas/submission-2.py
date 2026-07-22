import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        def check(rate):

            hrs = h

            for pile in piles:
                current = math.ceil (pile / rate)
                hrs = hrs - current

            if hrs >= 0:
                return True
            else:
                return False

            #return true if we can finish eating the banana with this rate
            #how to implement the algo?

        
        left, right = min(piles), max(piles)

        while left < right:

            mid = left + (right - left) // 2

            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
        