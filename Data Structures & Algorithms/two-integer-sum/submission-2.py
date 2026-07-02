class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map1 = {}

        for i in range(len(nums)):

            if nums[i] not in map1:

                map1[nums[i]] = [i]
            else:

                map1[nums[i]].append(i)


        for index in range(len(nums)):

            current = nums[index]

            if target - current in map1:

                if map1[target - current][0] == index:
                    if len(map1[target - current]) > 1:
                        return [index, map1[target - current][1]]
                else:
                    return [index, map1[target - current][0]]
