class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:



        hash1 = {}
        setofnums = set(nums)

        maxsofar = 0


        for num in nums:

            m = 1

            if num - 1 not in setofnums:

                temp = num

                while temp + 1 in setofnums:
                    m += 1

                if m > maxsofar:
                    maxsofar = m

        
        return maxsofar


        