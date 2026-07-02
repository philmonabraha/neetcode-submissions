class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


        result = [0] * len(temperatures)

        unsolved = []


        for i in range(len(temperatures)):

            while unsolved and temperatures[i] > temperatures[unsolved[-1]]:

                x = unsolved.pop()
                result[x] = (i - x)

            unsolved.append(i)

        return result

            

        
        