class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

         

        pre_map = {}

        for item in prerequisites:
            x = item[0]
            y = item[1]

            if x not in pre_map:
                pre_map[x] = [y]
            else:
                premap[x].append(y)

        queue = deque()
        for i in range(numCourses):
            if i in pre_map:
                queue.append(i)
            
        visited = set()
        
        while queue:

            curr = queue.popleft()

            if curr in visited:
                return False

            for preq in pre_map[curr]:
                queue.append(preq)
            
            visited.add(curr)

        return True
                



        