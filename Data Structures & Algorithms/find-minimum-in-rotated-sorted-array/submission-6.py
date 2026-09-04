class Solution:
    def findMin(self, nums: List[int]) -> int:


        left, right = 0, len(nums) - 1
   
        while nums[right] < nums[left]:

            mid = left + (right - left )//2

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid -1 
            
        return nums[left]




        