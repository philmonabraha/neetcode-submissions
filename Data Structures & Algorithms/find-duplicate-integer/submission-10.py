class Solution:
    def findDuplicate(self, nums: List[int]) -> int:


        for i in range(len(nums)):

            curr = nums[i] - 1

            if nums[curr] < 0:
                return nums[i ]
            
            nums[curr] = -1 * nums[curr]
        