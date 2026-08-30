class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1]*len(nums)
        suffix = [1]*len(nums)

        for i in range(1, len(nums)):
            num = nums[i]
            prefix[i] = prefix[i-1] * num
        
        for i in range(len(nums)-2, 0, -1):
            num = nums[i]
            suffix[i] = suffix[i+1] * num
        
        res = []
        for i in range(len(prefix)):
            res.append(prefix[i] * suffix[i])

        return res


        





        