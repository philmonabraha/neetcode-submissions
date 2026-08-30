class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for i in nums:
            num = nums[i]

            diff = target - num
            if diff in hashmap:
                return [i, hashmap[diff]]
            hashmap[num] = i

        
        