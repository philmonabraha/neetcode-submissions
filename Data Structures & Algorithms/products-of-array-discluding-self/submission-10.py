class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1 for i in range(len(nums))]
        suffix = [1 for i in range(len(nums))]

        for i in range(1, len(nums)):
                prefix[i] = nums[i - 1] * prefix[i - 1]
                suffix[len(nums) - i - 1] = nums[len(nums) - i] * suffix[len(nums) - i]

        result_array = []

        for num in range(len(nums)):
            result_array.append(prefix[num] * suffix[num])

        return result_array