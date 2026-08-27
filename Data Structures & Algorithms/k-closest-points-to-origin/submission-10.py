import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dictionary = {}
        heap = []

        # Build heap and dictionary
        for point in points:
            distance = point[0] ** 2 + point[1] ** 2   # no sqrt needed

            if distance not in dictionary:
                dictionary[distance] = [point]
                heapq.heappush(heap, distance)
            else:
                dictionary[distance].append(point)

        result = []
        i = 0

        while i < k:
            d = heapq.heappop(heap)

            if len(dictionary[d]) > 1:
                j = 0
                while i < k and j < len(dictionary[d]):
                    result.append(dictionary[d][j])
                    i += 1
                    j += 1
            else:
                result.append(dictionary[d][0])
                i += 1

        return result