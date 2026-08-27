class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n
        
        for i in range(n):
            if color[i] == -1:
                queue = [i]
                color[i] = 0
            
            while queue:
                u = queue.pop(0)

                for v in graph[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    
                    elif color[v] == color[u]:
                        return False
                    
        return True
 
