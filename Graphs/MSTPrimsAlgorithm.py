#User function Template for python3
import heapq

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        
    
        pq = [(0, 0)] 
        summation = 0

        visited = [0] * V
        
        while pq:
            
            weight, node  = heapq.heappop(pq)
            
            if visited[node] == 1:
                continue
            
            visited[node] = 1
            summation += weight
            
            for child, w in adj[node]:
                if visited[child]==0:
                    heapq.heappush(pq, (w, child))
                    
        return summation
                    
            