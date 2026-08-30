class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for i in range(len(nums)):
            if nums[i] - target in hashmap:
                return [hashmap[nums[i] - target], nums[i]]

            hashmap[nums[i]] = i

            




        