class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        result = []
        added = set()

        nums = sorted(nums)

        for t in range(len(nums)-2):

            target = nums[t]

            left = t
            right = len(nums)

            while left < right:

                if nums[left] + nums[right] == -target:
                    if [left, right, target].sort() not in added:
                        result.append([left, right, target])
                        added.add([left, right, target].sort())
                
                elif nums[left] + nums[right] > - target:
                    right -=1
                
                else:
                    left += 1

        return result

                






        