class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [0 for i in range(len(nums))]
        suffix = [0 for i in range(len(nums))]

        for i in range(len(nums)):
            
            if i == 0:
                prefix[0] = 1
            
            elif i == len(len(nums) - 1 ):
                suffix[len(nums)-1] = 1
            else:
                prefix[i] = nums[i - 1] * prefix[i - 1]
                suffix[i] = nums[i + 1] * prefix[i + 1]

        result_array = []

        for num in range(len(nums)):
            result_array.append(prefix[num] * suffix[num])

        return result_array