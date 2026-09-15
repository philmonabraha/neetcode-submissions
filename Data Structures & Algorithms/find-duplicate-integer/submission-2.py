class Solution:
    def findDuplicate(self, nums: List[int]) -> int:


        for i in range(len(nums)):

            if nums[nums[i]-1] < 0:
                return i

            curr = nums[i] - 1
            nums[curr] = -1*nums[curr]
        