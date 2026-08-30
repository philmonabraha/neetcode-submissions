class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        resultarray = [0 for i in range(len(temperatures))]

        for i in range(len(temperatures)):
            
            while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:

                resultarrray[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)

        return resultarray


        