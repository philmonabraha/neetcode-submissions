class Solution:
    def findDuplicate(self, nums: List[int]) -> int:


        for i in range(len(nums)):

            if nums[abs(nums[i])-1] < 0:
                return nums[i]
        
            nums[nums[i-1]] = -1 * abs(nums[nums[i-1]])

        return 0