class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


        result = []

        unsolved = []


        for i in range(len(temperatures)):

            while unsolved and temperatures[i] > unsolved[-1]:

                x = unsolved.pop()
                result.append(i - x)

            unsolved.append(i)

        return result

            

        
        