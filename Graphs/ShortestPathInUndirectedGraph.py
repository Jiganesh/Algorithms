#User function Template for python3
from collections import defaultdict, deque

class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        
        distances = [float("inf") for i in range (n)]
        
        
        graph = defaultdict(list)


        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
            
        visited = [0] * n
        def find_distance(node):
            
            queue = deque([(0, node)])
            distances[node] = 0
            
            while queue:
                distance ,node = queue.popleft()
                visited[node]=True
                
                for child in graph[node]:
                    if visited[child] == False:
                        distances[child] = min(distances[child], distances[node]+1)
                        
                        queue.append((distance+1, child))
        
        
        
        find_distance(src)

        return [-1 if i == float("inf") else i for i in distances]