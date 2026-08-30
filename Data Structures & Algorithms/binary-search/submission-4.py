class Solution:
    def search(self, nums: List[int], target: int) -> int:


        if nums[len(nums) //2] == target:
            return midpoint
        elif nums[len(nums) //2] < target:
            return self.search(nums[len(nums)//2+1:], target)
        else:
            return self.search(nums[:len(nums) //2], target)

        return -1;

        
        

        