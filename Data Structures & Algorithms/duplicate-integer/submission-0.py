class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashset = set()

        for i in nums:

            if i in hashset:
                return False
            else:
                hashset.add(i)

        return True

        
        