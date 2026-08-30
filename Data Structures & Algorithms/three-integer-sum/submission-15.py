class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        result = []
        added = set()

        nums = sorted(nums)

        for t in range(len(nums)-2):

            target = nums[t]

            left = t
            right = len(nums) - 1

            while left < right:

                if nums[left] + nums[right] == -target:
                    if [nums[left], nums[right], target].sort() not in added:
                        result.append([nums[left], nums[right], target])
                        added.add([nums[left], nums[right], target].sort())
                    left += 1
                
                elif nums[left] + nums[right] > - target:
                    right -=1
                
                else:
                    left += 1

        return result

                






        