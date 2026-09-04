class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        paired = []
        for i in range(len(position)):
            paired.append([position[i], speed[i]])

        paired.sort(reverse=True)

        #how long it takes them to reach
        #speed = distance / time. time = target - distance /speed

        stack = [(target - position[0]) / speed[0]]
        res = 0

        for i in range(1, len(position)):

            time = (target - position[i]) / speed[i]

            if time < stack[-1]:

                stack.append(time)
        
        return len(stack)


            






        