class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        added = set()

        result = []


        for i in range(len(nums)):

            first = nums[i]

            for j in range(len(nums)):
                for k in range(len(nums)):

                    if i != j and k != j:
                        second = nums[j]
                        third = nums[k]

                        if second + third == -first and tuple(i, j, k) not in added:
                            result.append([i,j,k])
                            added.add(tuple(i,j,k))

        return result

        



        