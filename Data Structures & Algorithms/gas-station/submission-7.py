class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        start = len(gas) - 1
        end = 0

        tank = gas[start] - gas[end]

        while start < end:

            if tank < 0:
                start -= 1
                tank = tank + gas[start] - cost[start]
            else:
                end += 1
                tank = tank + gas[end] - cost[end]

        return start if tank >=0 else -1



        