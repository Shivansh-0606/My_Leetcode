class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        for course , prereq in prerequisites:
            adj[prereq].append(course)
        
        state = [0] * numCourses
        
        def has_cycle(node:int)-> bool:

            if state[node] == 1:
                return True
            
            if state[node] == 2:
                return False
            
            state[node] = 1

            for neighbor in adj[node]:
                if has_cycle(neighbor):
                    return True
            
            state[node] = 2
            return False

        for course in range(numCourses):
            if state[course] == 0:
                if has_cycle(course):
                    return False
        
        return True



