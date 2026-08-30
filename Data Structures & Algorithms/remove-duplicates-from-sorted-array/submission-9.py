class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        pointer = len(nums) - 1
        unique = 0

        while pointer > 0:

            if nums[pointer] == nums[pointer-1]:
                nums = nums[:pointer] + nums[pointer:]
                l1 = l1 -1

            else:
                unique += 1
                l1 = l1 -1
        

        return unique
        