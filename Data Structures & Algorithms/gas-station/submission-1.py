class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        i = 0

        while i < len(gas)- 1:

            if total + (gas[i] - cost[i]) < 0:
                total = 0
            else:
                total = total + (gas[i] - cost[i])
            
            i += 1

        return i




        