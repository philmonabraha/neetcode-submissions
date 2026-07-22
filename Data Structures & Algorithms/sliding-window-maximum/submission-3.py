class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:



        left, right = 0, k


        maximum = []

        while right <= len(nums):


            currentmax = -float("infinity")
            
            for i in range(k):
                index = left + i
            
                if nums[index] > currentmax:
                    currentmax = nums[index]

            maximum.append(currentmax)

            left +=1
            right +=1

        return maximum






        