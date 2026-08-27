class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hashset = set(nums)

        longestsofar = 0

        
        for num in nums:

            if num - 1 not in hashset:

                length = 1

                while num + length in hashset:
                    length += 1

                longestsofar = max(longestsofar, length)

        return longestsofar





            
            

  






            


        