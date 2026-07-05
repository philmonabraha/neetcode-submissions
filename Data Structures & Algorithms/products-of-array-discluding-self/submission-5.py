class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        
        productuntil = [1] * len(nums)
        productafter = [1] * len(nums)

        for index in range(len(nums)):
            if index != 0:
                productuntil[index] = nums[index-1] * productuntil[index - 1]
        
        for index in range(len(nums)-1, 0, - 1):
            if index != len(nums)-1:
                productafter[index] = nums[index-1] * productafter[index - 1]

        output = [1]*len(nums)

        for index in range(len(productuntil)):
            output[index] = productuntil[index] * productafter[index]

        return output
        







        