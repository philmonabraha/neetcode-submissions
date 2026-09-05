class Solution:
    def findDuplicate(self, nums: List[int]) -> int:


        for i in range(len(nums)):

            curr = abs(nums[i]) - 1

            if nums[curr] < 0:
                return abs(nums[i])
            
            nums[curr] = -1 * nums[curr]
        