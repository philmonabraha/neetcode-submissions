class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i+1:[] for i in range(n)}       
        for u, v, w in times:
            graph[u].append((v,w))
 
        heap = [(0,k)]
        distances = {}

        count = 1

        while heap:

            dist, node = heapq.heappop(heap)

            if node in distances:
                continue

            distances[node] = dist

            for nei, weight in graph[node]:

                if nei not in distances:
                    heapq.heappush(heap, (dist+weight,nei))


        return -1 if len(distances) != n else max(distances.values())




        