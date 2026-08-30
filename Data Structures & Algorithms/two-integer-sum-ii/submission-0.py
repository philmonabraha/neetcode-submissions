class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        pointer1 = 0
        pointer2 = len(numbers) - 1

        while (pointer1 < pointer2):

            if nums[pointer1] + nums[pointer2] == target:
                return [pointer1, pointer2]

            if nums[pointer2] > target:
                pointer2 -= 1
            
            else:

                pointer1 += 1



        