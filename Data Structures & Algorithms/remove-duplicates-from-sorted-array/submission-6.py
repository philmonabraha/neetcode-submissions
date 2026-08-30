class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l1 = len(nums) - 1
        unique = 0

        while l1 > 1:

            if nums[l1] == nums[l1-1]:
                nums = nums[:l1-1] + nums[l1:]
                l1 = l1 -1

            else:
                unique += 1
                l1 = l1 -1
        

        return unique
        