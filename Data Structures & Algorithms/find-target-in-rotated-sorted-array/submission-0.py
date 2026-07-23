class Solution:
    def search(self, nums: List[int], target: int) -> int:



        left, right = 0 , len(nums) - 1


        while left < right:


            mid = left + (right - left)//2

            if nums[mid] == target:
                return mid

            elif nums[mid] >= nums[left] and target in range(nums[left], nums[right]):
                right = mid + 1
            
            elif nums[mid] >= nums[left] and target not in range(nums[left], nums[right]):
                left = mid


        return -1

            




        
        