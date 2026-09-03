class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        paired = []
        for i in range(len(position)):
            paired.append([position[i], speed[i]])

        paired.sort(reverse=True)

        #how long it takes them to reach
        #speed = distance / time. time = target - distance /speed

        stack = []
        res = 0

        for i in range(len(paired)):

            time = (target - paired[i][0]) / paired[i][1]

            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)


            






        