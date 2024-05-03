#User function Template for python3
from typing import List
from collections import deque


class Solution:
    
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, number_of_nodes: int, graph: List[List[int]]) -> List[int]:

        visited = [False] * number_of_nodes
        
        bfs_traversal_result = []
        
        def bfs_recursive(queue):
            
            if not queue : return # Base Condition 
        
            node = queue.popleft()
            visited[node] = True
            
            bfs_traversal_result.append(node)

            for child in graph[node]:
                if visited[child] == False:
                    visited[child] = True
                    queue.append(child)
            
            bfs_recursive(queue)
        
        bfs_recursive(deque([0]))
        return bfs_traversal_result