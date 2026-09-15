class Solution:
    def findDuplicate(self, nums: List[int]) -> int:


        for i in range(len(nums)):

            if nums[nums[i]] < 0:
                return nums[i]

            curr = nums[i]
            nums[curr] = -1*nums[curr]
        