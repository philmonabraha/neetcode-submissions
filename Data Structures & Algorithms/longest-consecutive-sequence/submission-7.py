class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        set_list = set(nums)

        maxsofar = 0

        for x in nums:
            
            curr = 1
            val = x
            if val - 1 not in set_list:
                while val + 1 in set_list:
                    curr += 1
                    val = val + 1
                maxsofar = max(maxsofar, curr)
        
        return maxsofar
        