class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for i in range(len(nums)):
            
            if target - nums[i] in hashmap:

                return [hashmap[nums[i] - target], i]

            hashmap[nums[i]] = i

        return []