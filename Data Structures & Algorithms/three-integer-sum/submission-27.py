class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        res = []
        tracker_set = set()

        for i in range(len(nums)):
            tracker1 = i
            tracker2 = i + 1
            tracker3 = len(nums) - 1

            while tracker2 < tracker3:

                if nums[tracker1] + nums[tracker2] + nums[tracker3] == 0:
                    if (nums[tracker1], nums[tracker2], nums[tracker3]) not in tracker_set:
                        tracker_set.add((nums[tracker1], nums[tracker2], nums[tracker3]))
                        res.append([nums[tracker1], nums[tracker2], nums[tracker3]])

                elif nums[tracker1] + nums[tracker2] + nums[tracker3] > 0:
                    tracker3 -= 1
                
                elif nums[tracker1] + nums[tracker2] + nums[tracker3] < 0:
                    tracker2 += 1

        return res

        

            



            



    

        
        