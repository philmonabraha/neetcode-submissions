class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        marked = [False for i in nums]

        hashmap = {}

        result = []

        for i in range(len(nums)):

            if nums[i] not in hashmap:
                hashmap[nums[i]] = [i]
            else:
                hashmap[nums[i]] = hashmap[nums[i]] + [i]

        for i in range(len(nums)):

            for j in range(1, len(nums)):

                if 0 - (nums[i] + nums[j]) in hashmap and hashmap[0 - (nums[i] + nums[j])]:
               
                    index = hashmap[0 - (nums[i] + nums[j])].pop()


                    if marked[i] == False and marked[j] == False and marked[index] == False:
                        result.append([nums[index], nums[i], nums[j]])
                        marked[i] = True
                        marked[j] = True
                        marked[index] = True

        return result
        
        