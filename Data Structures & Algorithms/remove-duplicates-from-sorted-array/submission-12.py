class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        pointer = 0
        unique = 0

        while pointer < len(nums)-1:

            if nums[pointer] == nums[pointer+1]:
                nums = nums[:pointer] + nums[pointer+1:]

            else:
                unique += 1
                pointer = pointer -1
        

        return unique
        