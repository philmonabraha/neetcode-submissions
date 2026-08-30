class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        set_list = set(nums)

        maxsofar = 0

        for x in nums:

            curr = 1
            while x + 1 in set_list:
                curr += 1
            maxsofar = max(maxsofar, curr)
        
        return maxsofar
        