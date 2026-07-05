class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        added = set()

        hash1 = []

        result = []

        for i in range(len(nums)):           
            hash1.append([nums[i], i])

        hash1.sort()

        for i in range(len(hash1)):

            left = i + 1
            right = len(nums) - 1

            while left < right:

                num1 = hash1[left][0]
                num2 = hash1[right][0]
                num3 = hash1[i][0]

                if num1+num2 > -num3:
                    right = right - 1
                elif num1+num2 < -num3:
                    left = left + 1
                elif num1+num2 == -num3:
                    result.append([hash1[i][1], hash1[left][1], hash1[right][1]])
                    left += 1
                    right -= 1

        
        return result








        