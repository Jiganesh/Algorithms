#User function Template for python3
from typing import List

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # code here
         
        visited = [0] * V

        def detect_cycle(node, path_visited = [0] * V):
        
            
            visited [node] = 1
            path_visited [node] = 1
            
            for child in adj[node]:

                if visited[child] == 0 and path_visited[child] == 0:
                    if detect_cycle (child, path_visited): return True
                elif path_visited[child] == 1:
                    return True
                
                
            path_visited[node] = 0
            return False
                

        for i in range(V):
            if detect_cycle(i) == True:
                return True
                
        return False


