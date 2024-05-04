#User function Template for python3
from typing import List
from collections import deque

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # code here
        
        
        # Indegrees 
        indegree = [0] * V 
        
        for parent in adj:
            for child in parent:
                indegree[child]+=1
        
        queue = deque([])
        
        
        # add nodes with 0 indegree
        for i in range(V):
            if indegree[i] == 0 : queue.append(i)
            
        
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for child in adj[node]:
                
                indegree[child]-=1
                
                if indegree[child]==0:
                    queue.append(child)
                    
        # If len is not same there is cycle  
        return len(result) != V