class Solution:
    def findMin(self, nums: List[int]) -> int:



        left, right = 0, len(nums) - 1

        while left < right:

            mid = left + (right - left) // 2

            if mid > left:
                left = mid 
            else:
                right = mid 

        return nums[left]
        