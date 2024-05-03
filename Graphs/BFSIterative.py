#User function Template for python3

from typing import List
from collections import deque


class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        
        queue = deque([0])
        
        
        visited = [False]*V
        visited[0] = True
        
        result = []
        
        while queue:
            node =  queue.popleft()
            result.append(node)
            
            for child in adj[node]:
                if visited[child]==False:
                    visited[child]=True
                    queue.append(child)

        return result
            