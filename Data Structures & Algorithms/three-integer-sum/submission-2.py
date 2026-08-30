class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        marked = [False for i in nums]

        hashmap = {}

        result = []

        for i in range(len(nums)):

            if nums[i] not in hashmap:
                nums[i] = [i]
            else:
                nums[i] = nums[i] + [i]

        for i in range(len(nums)):

            for j in range(len(nums)):

                if 0 - nums[i] + nums[j] in hashmap:
               
                    index = hashmap[0 - nums[i] + nums[j]].pop()

                    if marked[i] == False and marked[j] == False and marked[index] == False:
                        result.append([index, i, j])
                        marked[i] == True
                        marked[j] == True
                        marked[index] == True


        return result
        
        