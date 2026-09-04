class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        stack = []

        res = 0

        res_set = ()

        #how long it takes them to reach
        #speed = distance / time. time = target - distance /speed


        for i in range(len(position)):

            time = math.ceil((target - position[i]) / speed[i])
            res_set.add(time)
        
        return len(res_set)


            






        