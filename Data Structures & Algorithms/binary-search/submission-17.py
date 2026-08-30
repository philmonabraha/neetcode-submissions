class Solution:
    def search(self, nums: List[int], target: int) -> int:


        left, right = 0, len(nums) - 1

        while left <= right:

            if nums[left] == target:
                return left
            elif target < nums[left]:
                left = (right - left) // 2
            else:
                right = (right - left) // 2
        
        return left