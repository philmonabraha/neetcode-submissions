class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxatcurr = 0

        maximum = nums[0]
        
        for num in nums:

            maxatcurr = max(maxatcurr, 0)
            maxatcurr = maxatcurr + num
            maximum = max(maximum, maxatcurr)

        return maximum
        