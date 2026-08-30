class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if nums[midpoint] == target:
            return midpoint
        elif nums[midpoint] < target:
            return search(nums[midpoint+1:])
        else:
            return search(nums[:midpoint])



        return -1;

        
        

        