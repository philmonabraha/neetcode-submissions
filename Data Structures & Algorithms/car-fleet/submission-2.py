class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        stack = []

        res = 0

        res_set = ()

        #how long it takes them to reach
        #speed = distance / time. time = target - distance /speed


        for i in range(position):

            time = ceil((target - distance) / speed)
            res_set.add(time)
        
        return len(res_set)


            






        