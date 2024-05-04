from collections import deque

class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        
        # Indegrees
        
        stack = []
        
        indegrees = [0] * V
        
        for parent in adj:
            for child in parent:
                indegrees[child]+=1
                
        # pick nodes with zero indegree
        queue = deque([])
        
        for i in range (V):
            if indegrees[i]==0:queue.append(i)
            
            
        # topological sort
        while queue:
            
            node = queue.popleft()
            stack.append(node)
            
            for child in adj[node]:
                indegrees[child] -=1
                
                if indegrees[child]==0:
                    queue.append(child)
                    
        return stack