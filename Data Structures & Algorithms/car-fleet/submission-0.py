class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        pair = []

        for i in range(len(position)):
            pair.append([position[i], speed[i]])

        pair.sort()

        fleet = 0
        current = []

        for item in pair:

            distance = item[0]
            s = item[1]
            timetoreach = ceil((target - distance)/s)

            if len(current) == 0 or timetoreach > current[-1]:
                current.append(timetoreach)

        return len(current)

            


        