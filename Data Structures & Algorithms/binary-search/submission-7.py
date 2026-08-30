class Solution:

    def search(self, nums:List[int], target: int):

        mid = len(nums) // 2

        while mid < len(nums) and mid >= 0:



            if nums[mid] == target:
                return mid

            if mid == 0 or mid == len(s) - 1:
                return -1
            
            if target > nums[mid]:
                mid = mid + (len(s) - mid) // 2
            else:
                mid = mid // 2
            #if not found


        



        