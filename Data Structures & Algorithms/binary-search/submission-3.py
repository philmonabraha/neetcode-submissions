class Solution:
    def search(self, nums: List[int], target: int) -> int:

        midpoint = len(nums) //2

        if nums[midpoint] == target:
            return midpoint
        elif nums[midpoint] < target:
            return self.search(nums[midpoint+1:], target)
        else:
            return self.search(nums[:midpoint], target)



        return -1;

        
        

        