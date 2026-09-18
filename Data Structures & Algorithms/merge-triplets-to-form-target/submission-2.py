class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        matched = [False, False, False]

        for x,y,z in triplets:

            if x > target[0] or y > target[1] or z > target[2]:
                continue
            
            for i in range(3):
                if x == target[i]:
                    matched[i] = True

        return matched[0] and matched[1] and matched[2]




        